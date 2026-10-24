'use client';
import Link from 'next/link';
import {usePathname} from 'next/navigation';
import {useState,useEffect,useRef} from 'react';
const links=[['/','首页'],['/showcase','效果预览'],['/technology','技术实现'],['/download','下载与问题'],['/feedback','意见反馈']];
export function Shell({children}:{children:React.ReactNode}){
 const path=usePathname();const [open,setOpen]=useState(false);const [compact,setCompact]=useState(false);const menuButton=useRef<HTMLButtonElement>(null);const header=useRef<HTMLElement>(null);
 useEffect(()=>setOpen(false),[path]);
 useEffect(()=>{
  if(path.startsWith('/admin'))return;
  // 收起和展开使用不同位置，避免页头高度变化导致反复切换。
  function update(){setCompact(previous=>previous?window.scrollY>8:window.scrollY>64);}
  update();window.addEventListener('scroll',update,{passive:true});
  return ()=>window.removeEventListener('scroll',update);
 },[path]);
 useEffect(()=>{
  if(!open)return;
  function escape(event:KeyboardEvent){if(event.key==='Escape'){setOpen(false);menuButton.current?.focus();}}
  function outside(event:PointerEvent){if(!header.current?.contains(event.target as Node))setOpen(false);}
  document.addEventListener('keydown',escape);document.addEventListener('pointerdown',outside);
  return ()=>{document.removeEventListener('keydown',escape);document.removeEventListener('pointerdown',outside);};
 },[open]);
 if(path.startsWith('/admin'))return <main id="main">{children}</main>;
 return <><header className={compact?'site-header is-compact':'site-header'} ref={header} onBlur={event=>{if(!event.currentTarget.contains(event.relatedTarget as Node))setOpen(false);}}><div className="nav-inner">
  <Link href="/" className="brand"><img src="/images/logo.png" alt="" width="132" height="132"/><span>汇率观察站</span></Link>
  <button ref={menuButton} className="menu-toggle" onClick={()=>setOpen(!open)} aria-expanded={open} aria-controls="main-nav"><span className={'menu-symbol'+(open?' is-open':'')} aria-hidden="true"><i/><i/></span>{open?'关闭':'菜单'}</button>
  <nav id="main-nav" className={open?'nav-links open':'nav-links'} aria-label="主导航">{links.map(([url,label])=>{const active=url==='/'?path==='/':path.startsWith(url);return <Link key={url} href={url} onClick={()=>setOpen(false)} className={active?'active':''} aria-current={active?'page':undefined}><span className="nav-label"><span>{label}</span><span aria-hidden="true">{label}</span></span><span className="nav-dot" aria-hidden="true"/></Link>;})}</nav>
  <Link className="button nav-download" href="/download">Windows 下载</Link>
 </div></header><main id="main">{children}</main><footer className="footer wrap"><div><Link href="/" className="footer-brand"><img src="/images/logo.png" alt="" width="30" height="30"/><span>汇率观察站</span></Link><p>一个关于数据、规则与 AI 协作的桌面项目。</p></div><div className="footer-links"><Link href="/download">下载与问题</Link><Link href="/feedback">意见反馈</Link><Link href="/privacy">隐私说明</Link><Link href="/admin">管理入口</Link></div></footer></>;
}
