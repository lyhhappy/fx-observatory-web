import Link from 'next/link';
import {Gallery} from '@/components/Gallery';
import {Globe} from '@/components/Globe';
import {MonitorPlayground} from '@/components/MonitorPlayground';
import {Workflow} from '@/components/Workflow';
import {showcases} from '@/lib/content';
export default function Home(){return <>
 <section className="hero wrap"><div className="hero-copy"><span className="badge">桌面项目 / Windows</span><h1>让汇率波动，<br/>有迹可循。</h1><p>真实银行数据、清晰提醒规则、可追溯运行记录。<br className="desktop-only"/>从界面到实现，完整认识这个汇率监控项目。</p><div className="actions"><Link className="button" href="/showcase">进入效果预览</Link><Link className="button secondary" href="/download">下载 Windows 版</Link></div></div><Globe/></section>
 <section className="wrap intro-strip"><div><h3>官方牌价</h3><p>农业银行公开接口</p></div><div><h3>双向规则</h3><p>现汇买入与卖出独立判断</p></div><div><h3>有据可查</h3><p>保存来源、时间与触发依据</p></div></section>
 <section id="intro-video" className="wrap section intro-video" aria-labelledby="intro-video-title"><div className="section-heading"><div><p className="eyebrow">项目介绍视频</p><h2 id="intro-video-title">用一段视频，认识汇率观察站。</h2><p>从汇率监测到预警提醒，了解应用的功能与使用场景。</p></div><a className="text-link" href="/videos/fx-agent-introduction.mp4" download>下载介绍视频 ↓</a></div><div className="intro-video-player"><video controls playsInline preload="metadata" aria-label="实时汇率监测预警智能体介绍" aria-describedby="intro-video-caption"><source src="/videos/fx-agent-introduction.mp4" type="video/mp4"/>你的浏览器不支持视频播放，请使用上方链接下载观看。</video></div><p id="intro-video-caption" className="fine">点击播放，可调节音量、拖动进度或全屏观看。</p></section>
 <MonitorPlayground/>
 <div className="wrap"><Gallery/></div>
 <section className="wrap section"><div className="section-heading"><div><p className="eyebrow">应用效果</p><h2>先看实际效果，<br/>再了解如何实现。</h2></div><Link className="text-link" href="/showcase">查看全部效果 →</Link></div><div className="cards three">{showcases.map(item=><Link href={'/showcase/'+item.slug} className="feature-card" key={item.slug}><div className="card-image"><img src={'/images/'+item.image} alt={item.title+'历史界面'} loading="lazy"/></div><div className="card-content"><h3>{item.title}</h3><p>{item.description}</p><span className="text-link">查看详情 →</span></div></Link>)}</div></section>
 <section className="wrap section"><div className="section-heading"><div><p className="eyebrow">点击步骤，了解处理过程</p><h2>一次波动，如何变成一条提醒？</h2></div><Link className="text-link" href="/technology">深入技术实现 →</Link></div><Workflow/></section>

 <section className="wrap split-links"><Link href="/technology"><h3>工程细节，经得起追问。</h3><p>理解采集、精确判断、模型说明和记录之间的关系。</p><span className="text-link">技术实现 →</span></Link><Link href="/feedback"><h3>体验之后，告诉我。</h3><p>好用的细节、改进建议或问题，都会成为下一步的参考。</p><span className="text-link">留下反馈 →</span></Link></section>
 <section className="wrap download-banner"><div><h2>在 Windows 上，亲自体验。</h2><p>先认识项目，再下载完整应用。</p></div><Link className="button light" href="/download">下载 Windows 版</Link></section>
</>}
