import {cookies} from 'next/headers';import {createHmac,timingSafeEqual} from 'node:crypto';import {cloud,mode} from './store';
export function signature(value:string){const secret=process.env.SESSION_SECRET;if(!secret||secret.length<32)throw Error('请配置足够长的 SESSION_SECRET。');return createHmac('sha256',secret).update(value).digest('hex');}
export function equal(a:string,b:string){const aa=Buffer.from(a),bb=Buffer.from(b);return aa.length===bb.length&&timingSafeEqual(aa,bb);}
export function localToken(){const value=String(Date.now()+8*3600000);return value+'.'+signature(value);}
export async function authorized(){const token=(await cookies()).get('fx_admin')?.value;if(!token)return false;if(mode()==='supabase'){try{const {data,error}=await cloud(true).auth.getUser(token);return !error&&!!process.env.ADMIN_USER_ID&&data.user?.id===process.env.ADMIN_USER_ID;}catch{return false;}}const [time,mac]=token.split('.');return !!mac&&Number(time)>Date.now()&&equal(signature(time),mac);}
export {sameOrigin} from './origin';
export function visitorKey(request:Request,kind:string){const ip=process.env.VERCEL?request.headers.get('x-forwarded-for')?.split(',')[0]?.trim()||'unknown':'local';return signature(kind+':'+ip);}
