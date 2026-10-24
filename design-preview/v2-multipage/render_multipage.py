"""Multipage design boards. No website or backend is implemented."""
from pathlib import Path
header=(Path(__file__).parent.parent/'render_design.py').read_text(encoding='utf-8').split('\nim,p=start(1440,3700)')[0]
exec(compile(header,'design_helpers','exec'))
OUT=Path(__file__).parent
ASSETS=Path('C:/Users/14383/Desktop/汇率智能体/docs/证据')
def nav(p,active='首页'):
 p.drawImage(QRectF(48,14,84,84),QImage(str(OUT.parent/'assets'/'product-logo.png')))
 txt(p,144,25,340,60,'汇率观察站',30,b=True)
 for x,s in [(550,'首页'),(650,'效果预览'),(805,'技术实现'),(960,'下载'),(1050,'意见反馈')]:
  txt(p,x,25,130,60,s,21,GREEN if s==active else MUTED,s==active)
 rect(p,1210,22,180,66,INK,8,INK)
 txt(p,1210,22,180,66,'Windows 下载',18,'#FFFFFF',True,Qt.AlignmentFlag.AlignHCenter)
 rule(p,0,112,1440)
def shot(p,name,x,y,w,h,crop=None):
 image=QImage(str(ASSETS/name))
 if crop:image=image.copy(*crop)
 scaled=image.scaled(int(w),int(h),Qt.AspectRatioMode.KeepAspectRatio,Qt.TransformationMode.SmoothTransformation)
 p.drawImage(QRectF(x+(w-scaled.width())/2,y+(h-scaled.height())/2,scaled.width(),scaled.height()),scaled)
def intro(p,crumb,title,sub):
 txt(p,64,123,1300,30,crumb,14,MUTED)
 txt(p,64,160,1300,70,title,45,b=True)
 txt(p,64,245,1300,55,sub,18,MUTED)
def panel(p,x,y,w,title,body):
 rect(p,x,y,w,170);txt(p,x+24,y+18,w-48,43,title,23,b=True);txt(p,x+24,y+73,w-48,75,body,17,MUTED)
def foot(p,y):
 rule(p,64,y,1312);txt(p,64,y+20,1300,45,'静态审核稿 · 所有行情与运行结果为历史记录 · 点击与页面跳转待确认后实现',14,MUTED)
def detail(name,title,sub,screenshot,crop,metric_title,metric,body):
 im,p=start(1440,1450);nav(p,'效果预览');intro(p,'首页 / 效果预览 / '+title,title,sub)
 rect(p,64,335,930,650,'#EAF0ED');shot(p,screenshot,80,351,898,618)
 pill(p,1024,335,160,'原应用历史截图')
 txt(p,1024,399,352,55,metric_title,25,b=True)
 txt(p,1024,470,352,125,metric,38,GREEN,True)
 txt(p,1024,625,352,190,body,18,MUTED)
 button(p,1024,860,352,'放大查看界面',False)
 txt(p,64,1030,1100,55,'细节看得清，效果才有说服力。',30,b=True)
 rect(p,64,1110,630,230);shot(p,screenshot,80,1126,598,198,crop)
 txt(p,730,1110,635,65,'完整界面 + 重点放大',24,b=True)
 txt(p,730,1190,635,110,'正式网站中，完整截图可点击放大；重点区域支持切换说明。\n截图不做功能改造，不把尚未验证的能力写成成功效果。',18,MUTED)
 foot(p,1375);save(im,p,name)

im,p=start(1440,1650);nav(p)
pill(p,64,130,190,'桌面项目 / Windows')
txt(p,64,195,800,170,'让汇率波动，\n有迹可循。',68,b=True)
txt(p,64,395,740,75,'真实银行数据、清晰提醒规则、可追溯运行记录。\n从界面到实现，完整认识这个汇率监控项目。',21,MUTED)
button(p,64,510,235,'进入效果预览');button(p,320,510,200,'下载 Windows 版',False)
rect(p,850,150,525,440,'#E7EEEA');shot(p,'v2_exe_records.png',870,170,485,400,(930,205,630,640))
txt(p,64,670,1200,60,'先看实际效果，再了解如何实现。',36,b=True)
for i,(title,file,desc) in enumerate([('行情监控','v2_source_window.png','币种、买卖价与历史基准'),('AI 助手','v2_exe_assistant.png','独立对话界面与能力边界'),('预警与记录','v2_exe_records.png','触发依据、模型说明与通知状态')]):
 x=64+i*443;rect(p,x,775,423,410);shot(p,file,x+12,790,399,262)
 txt(p,x+20,1067,380,40,title,23,b=True);txt(p,x+20,1120,380,35,desc,15,MUTED)
panel(p,64,1250,630,'了解项目实现','进入独立技术页，查看采集、精确计算、规则判断、模型说明与落盘流程。')
panel(p,744,1250,630,'体验之后，留下建议','进入独立反馈页；姓名必填，电话或邮箱至少填写一项，其他内容选填。')
foot(p,1515);save(im,p,'01-home.png')

im,p=start(1440,1850);nav(p,'效果预览');intro(p,'首页 / 效果预览','把应用的效果，展开来看。','这里是效果展示入口，每个模块都可以进入独立详情页；网页不执行真实监控或模型请求。')
items=[('行情监控','v2_source_window.png','官方现汇买入、卖出价与涨跌幅。','查看监控详情'),('AI 助手','v2_exe_assistant.png','对话入口、可用工具与修改确认机制。','查看助手详情'),('预警记录','v2_exe_records.png','具体预警、来源时间与渠道状态。','查看预警详情'),('Agent 流程','v2_source_flow.png','采集、计算、模型说明与持久化。','查看技术实现')]
for i,(title,file,desc,cta) in enumerate(items):
 x=64+(i%2)*680;y=340+(i//2)*660
 rect(p,x,y,630,610);shot(p,file,x+16,y+16,598,395)
 txt(p,x+24,y+430,580,48,title,28,b=True);txt(p,x+24,y+490,580,40,desc,17,MUTED)
 txt(p,x+24,y+548,580,40,cta+'  →',17,GREEN,True)
foot(p,1725);save(im,p,'02-effects-overview.png')

detail('03-monitoring-detail.png','行情监控效果','展示官方牌价、双向涨跌与比较基准；保留原应用真实界面。','v2_source_window.png',(275,242,880,450),'当前价、基准与时间','买入 / 卖出\n分别比较','截图取自 2026-10-21 的历史运行。每轮默认 60 秒检查；银行时间与程序检查时间分别展示。\n\n只展示监控，不预测价格。')
detail('04-ai-assistant-detail.png','AI 助手效果','展示原版的真实入口和工具设计，明确区分已实现界面与实际联调证据。','v2_exe_assistant.png',(270,135,1290,300),'界面已具备','查询记录\n拟定变更','原版包含查询行情、读取预警、拟定规则变更三类工具。\n\n这张截图只证明对话入口，不证明工具已真实调用成功；不编造对话成功案例。')
detail('05-alerts-detail.png','预警与记录效果','用一条实际历史预警，展示价格、阈值、时间和通知状态如何对应。','v2_exe_records.png',(1012,330,520,470),'港币现汇买入预警','下跌约 0.13%\n提醒线 0.1%','2026-10-23 17:23 的历史记录中，港币买入方向达到阈值，界面标记模型参与，桌面通知已提交。\n\n“已提交”不代表实际阅读；邮件记录不等于已收件。')

im,p=start(1440,1700);nav(p,'技术实现');intro(p,'首页 / 技术实现','一条提醒，经过哪些步骤？','可逐步展开的工作流程，配合原应用的运行摘要。')
for i,s in enumerate(['官方当前与历史报价','日期与单位处理','精确阈值判断','模型说明 / 规则兜底','记录与通知']):
 x=64+i*267;rect(p,x,340,247,95,INK if i==2 else '#FFFFFF');txt(p,x+18,348,210,30,str(i+1).zfill(2),14,GREEN if i!=2 else '#C6DCD1');txt(p,x+18,382,215,40,s,18,'#FFFFFF' if i==2 else INK,True)
rect(p,64,475,1310,730,'#EAF0ED');shot(p,'v2_source_flow.png',80,491,1278,698)
txt(p,64,1240,1000,55,'确定性规则负责判断，模型负责结构化说明。',29,b=True)
txt(p,64,1315,1280,75,'LangGraph 连接采集、计算、阈值与说明步骤。SQLite 保存比较结果、预警及通知状态；模型失败时明确采用规则兜底。',20,MUTED)
for i,(title,body) in enumerate([('PySide6','桌面交互'),('HTTPX','官方接口采集'),('精确有理数','阈值边界判断'),('SQLite','本机记录与追溯')]):
 x=64+i*337;txt(p,x,1445,315,42,title,23,b=True);txt(p,x,1500,315,42,body,16,MUTED)
foot(p,1590);save(im,p,'06-technical.png')

im,p=start(1440,1280);nav(p,'下载');intro(p,'首页 / 下载','在 Windows 上，亲自体验。','桌面应用公开下载入口。应用截图、流程和使用说明可先浏览。')
rect(p,64,350,820,380,INK)
pill(p,100,380,165,'Windows 桌面版','#324B43','#FFFFFF')
txt(p,100,450,730,65,'汇率观察站',43,'#FFFFFF',True)
txt(p,100,535,730,55,'完整程序 ZIP · 保留 _internal 目录',21,'#D7E2DD')
button(p,100,625,370,'下载 Windows 版',False)
panel(p,925,350,450,'仅支持 Windows','macOS、Linux、Android 和 iOS 不提供安装版本。手机可以浏览本网站。')
txt(p,925,565,450,120,'版本、发布日期、文件大小及校验值，待正式准备发布包时核实后填写。',18,MUTED)
txt(p,64,790,1200,55,'从下载到开始监控',32,b=True)
for i,(a,b) in enumerate([('解压完整文件夹','不要仅复制 EXE，保留配套资源。'),('打开应用','启动 ExchangeRateAgent.exe。'),('点击开始监控','联网读取官方报价，按规则判断。')]):
 x=64+i*450;txt(p,x,895,400,45,str(i+1).zfill(2)+'  '+a,24,b=True);txt(p,x,965,405,65,b,18,MUTED)
txt(p,64,1090,1300,50,'遇到问题？进入意见反馈页，留下联系方式和问题描述。',19,GREEN)
foot(p,1170);save(im,p,'07-download.png')

# Sitemap is a design board, not a router implementation.
im,p=start(1440,1020)
txt(p,64,35,1320,70,'多页面网站结构',40,b=True)
txt(p,64,115,1320,45,'首页提供概览；效果、技术、下载与反馈各自有独立页面。',20,MUTED)
rect(p,550,205,340,75,INK);txt(p,550,205,340,75,'首页  /',26,'#FFFFFF',True,Qt.AlignmentFlag.AlignHCenter)
groups=[('效果预览 /showcase',['行情监控详情','AI 助手详情','预警记录详情']),('技术实现 /technology',['工作流程','技术栈与边界']),('下载 /download',['Windows 下载','启动方法']),('反馈 /feedback',['联系方式','体验、建议、问题'])]
for i,(title,children) in enumerate(groups):
 x=64+i*338;rect(p,x,375,310,82,'#E8F0ED');txt(p,x+18,384,277,62,title,21,GREEN,True)
 for j,s in enumerate(children):rect(p,x,495+j*77,310,60);txt(p,x+18,501+j*77,277,48,s,19)
rect(p,64,800,1310,120,INK);txt(p,90,815,1260,80,'私有管理 /admin    →    登录后查看反馈、联系方式和处理状态\n与公开展示页分开；反馈内容不对访客公开。',21,'#FFFFFF')
txt(p,64,955,1300,35,'本轮只新增多页面静态设计，不实现页面跳转、下载、登录或数据提交。',15,MUTED)
save(im,p,'00-sitemap.png')
QImage(str(OUT/'05-alerts-detail.png')).copy(0,0,1440,118).save(str(OUT/'08-navigation-closeup.png'))
