export type FeedbackInput={name:string;phone:string;email:string;experience:string;suggestion:string;problem:string;consent:boolean;website?:string};
export type Feedback=FeedbackInput & {id:string;created_at:string;status:'new'|'done'};
export function validateFeedback(input:unknown):FeedbackInput {
 if(!input || typeof input!=='object' || Array.isArray(input))throw Error('请填写有效反馈。');
 const raw=input as Record<string,unknown>; const result:Record<string,string>={};
 for(const key of ['name','phone','email','experience','suggestion','problem']){
  const value=raw[key]??'';if(typeof value!=='string')throw Error('字段格式不正确。');
  result[key]=value.trim();if(value.length>(['experience','suggestion','problem'].includes(key)?3000:key==='email'?254:key==='name'?80:32))throw Error('填写内容过长。');
 }
 if(!result.name)throw Error('请填写姓名或称呼。');
 if(!result.phone&&!result.email)throw Error('电话或邮箱至少填写一个。');
 if(result.email&&!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(result.email))throw Error('请填写有效邮箱。');
 if(result.phone&&!/^[+()\d\s-]{7,32}$/.test(result.phone))throw Error('请填写有效联系电话。');
 if(raw.consent!==true)throw Error('请先确认联系方式使用说明。');
 if(raw.website)throw Error('无法提交，请重试。');
 return {...result,consent:true} as FeedbackInput;
}
