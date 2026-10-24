import fs from 'node:fs';
import path from 'node:path';
import Link from 'next/link';
export const dynamic='force-dynamic';
export const metadata={title:'下载与问题'};
const questions=[
 ['支持哪些系统？需要安装 Node.js 或 Python 吗？','下载包适用于 Windows 64 位系统，已包含应用运行所需的 Python 环境，无需额外安装 Node.js 或 Python。macOS、Linux、Android 和 iOS 暂无安装版本。'],
 ['解压后打不开，或者提示缺少文件怎么办？','请先将整个 ZIP 完整解压，再运行 ExchangeRateAgent.exe。EXE 和 _internal 文件夹必须保留在同一目录，不要直接从压缩包中启动，也不要只复制 EXE。若仍有提示，请记录提示内容并通过反馈页提交。'],
 ['行情一直显示“待获取”，或银行时间没有变化？','先确认网络可用，再点击“开始监控”。应用默认每 60 秒检查一次。银行尚未更新时，银行发布时间可能保持不变；查看程序检查时间，可以区分“正在检查”和“银行有新报价”。'],
 ['为什么提示历史基准缺失，不能比较涨跌？','指定日期没有有效的同方向报价时，应用会暂停该项比较。可以改选一个有报价的历史日期，或选择上一个法定工作日。选择“昨天”不会自动改用其他日期，也不会把缺少的报价当作零。'],
 ['第一次提醒后，为什么不再继续报警？','提醒后需要重设该方向的提醒线。若点击“稍后处理”或直接关闭弹窗，该方向会暂停报警，报价仍会继续采集。重新设置并保存提醒线后可恢复；同时核对买入、卖出方向是否选对。'],
 ['AI 助手没有响应，还能监控吗？','规则监控可以独立于模型运行。先开始监控，让助手有本机报价和记录可查询；再检查网络与“连接设置”中的模型状态。使用自己的账户时，还需检查密钥、账户额度和模型权限。预警说明生成失败时会使用规则兜底，持续报错可提交错误提示。'],
 ['预警显示“已提交”，为什么没有收到邮件？','“已提交”表示交给窗口或邮件服务器，不代表已到收件箱。请确认已开启邮件提醒、邮箱 SMTP 服务和授权码配置正确，再发送测试提醒，并检查收件箱与垃圾邮件。桌面和邮件状态需要分别查看。'],
 ['关闭窗口后，还会继续监控吗？','当前版本关闭窗口就退出程序，不提供托盘常驻监控。需要持续监控时，请保持应用运行；重新打开后点击“开始监控”。']
];
export default function Download(){
 let info:{bytes:number;sha256:string;prepared_at:string}|null=null;
 try{info=JSON.parse(fs.readFileSync(path.join(process.cwd(),'local-data/downloads/manifest.json'),'utf8'));}catch{}
 const ready=!!info||!!process.env.DOWNLOAD_URL;
 return <div className="wrap"><div className="page-intro"><p className="breadcrumb"><Link href="/">首页</Link> / 下载与问题</p><h1>在 Windows 上，亲自体验。</h1><p>下载完整程序文件夹，解压后打开应用。使用中遇到问题，可以在本页查找解释与处理方法。</p></div>
 <div className="download-grid"><section className="download-package"><span className="badge">Windows 64 位桌面版</span><h2>汇率观察站</h2><p>完整程序 ZIP · 无需另外安装 Python</p>{ready?<a href="/api/download" className="button light">下载 Windows 版 ↓</a>:<p>下载包尚未发布，请稍后再来。</p>}{info&&<><p className="fine">大小：{(info.bytes/1024/1024).toFixed(1)} MiB · 包准备日期：{info.prepared_at.slice(0,10)}</p><details><summary>查看 SHA-256 校验值</summary><code className="hash">{info.sha256}</code></details></>}</section><aside><h2>完整解压，再启动。</h2><p>保留同目录的 <code>_internal</code>，不要只移动 EXE。需要网络才能取得银行报价和调用模型。</p><p className="boundary-note">应用仅支持 Windows。macOS、Linux、Android 和 iOS 暂无安装版本。网站下载的是原版程序，不含个人运行数据库与邮箱配置。</p><a className="text-link download-help-link" href="#download-questions">查看常见问题 ↓</a></aside></div>
 <section className="section"><h2>从下载到开始监控</h2><div className="tech-grid steps-three">{[['01','完整解压','将 ZIP 解压到你有写入权限的文件夹。'],['02','打开应用','运行 ExchangeRateAgent.exe，保留配套目录。'],['03','开始监控','点击开始监控，读取官方报价并设置提醒线。']].map(([n,title,body])=><article key={n}><span className="step-number">{n}</span><h3>{title}</h3><p>{body}</p></article>)}</div></section>
 <section className="section" id="download-questions"><div className="section-heading"><div><p className="eyebrow">下载与使用帮助</p><h2>可能遇到的问题</h2></div><p>展开问题，查看原因和处理方法。</p></div><div className="download-faq detail-features">{questions.map(([question,answer])=><details key={question}><summary>{question}</summary><p>{answer}</p></details>)}</div><div className="download-support"><p>仍未解决？请附上 Windows 版本、出现时间、操作步骤和提示内容，方便定位。</p><Link className="text-link" href="/feedback">遇到问题？留下反馈 →</Link></div></section>
 </div>;
}