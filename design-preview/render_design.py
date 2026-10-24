"""Static design boards only; no website, API, or interactive application."""
import os, math, random
from pathlib import Path
os.environ['QT_QPA_PLATFORM']='offscreen'
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QImage,QPainter,QColor,QFont,QFontDatabase,QPen,QPainterPath
from PySide6.QtCore import QRectF,Qt
app=QApplication([])
font_id=QFontDatabase.addApplicationFont('C:/Windows/Fonts/msyh.ttc')
font=QFontDatabase.applicationFontFamilies(font_id)[0]
OUT=Path(__file__).parent
APP=Path('C:/Users/14383/Desktop/汇率智能体/docs/证据/v2_source_window.png')
INK='#151D20'; MUTED='#647175'; GREEN='#176D62'; LINE='#DDE3E1'; BG='#F7F9F8'
def start(w,h):
 im=QImage(w,h,QImage.Format.Format_RGB32);im.fill(QColor(BG));p=QPainter(im);p.setRenderHint(QPainter.RenderHint.Antialiasing);return im,p
def txt(p,x,y,w,h,s,size=18,c=INK,b=False,align=Qt.AlignmentFlag.AlignLeft):
 f=QFont(font);f.setPixelSize(size);f.setWeight(QFont.Weight.Bold if b else QFont.Weight.Normal);p.setFont(f);p.setPen(QColor(c));p.drawText(QRectF(x,y,w,h),align|Qt.AlignmentFlag.AlignVCenter|Qt.TextFlag.TextWordWrap,s)
def rect(p,x,y,w,h,fill='#FFFFFF',r=14,border=LINE):
 p.setPen(QPen(QColor(border),1));p.setBrush(QColor(fill));p.drawRoundedRect(QRectF(x,y,w,h),r,r)
def rule(p,x,y,w):
 p.setPen(QPen(QColor(LINE),1));p.drawLine(x,y,x+w,y)
def pill(p,x,y,w,s,fill='#E8F0ED',c=GREEN):
 rect(p,x,y,w,34,fill,17,fill);txt(p,x+12,y,w-24,34,s,13,c)
def button(p,x,y,w,s,dark=True):
 rect(p,x,y,w,52,INK if dark else '#FFFFFF',7,INK if dark else LINE);txt(p,x,y,w,52,s,16,'#FFFFFF' if dark else INK,True,Qt.AlignmentFlag.AlignHCenter)
def nav(p,w=1440):
 txt(p,64,20,270,45,'汇率观察站',22,b=True)
 txt(p,630,20,550,45,'功能介绍      工作流程      技术实现      意见反馈',15)
 button(p,w-230,17,166,'下载 Windows 版')
 rule(p,0,86,w)
def section(p,y,title,sub=''):
 txt(p,80,y,1200,64,title,40,b=True)
 if sub:txt(p,80,y+70,1250,45,sub,17,MUTED)
def footer(p,y,w=1440):
 rule(p,64,y,w-128);txt(p,64,y+20,w-128,40,'汇率观察站    /    一个关于数据、规则与 AI 协作的桌面项目',15,MUTED)
 txt(p,64,y+65,w-128,35,'设计预览 · 待审核    |    仅 Windows 版    |    网页不提供在线汇率与交易功能',13,MUTED)
def save(im,p,name):p.end();im.save(str(OUT/name))

im,p=start(1440,3700);nav(p)
pill(p,80,140,182,'Windows 桌面应用')
txt(p,80,199,850,170,'让汇率波动，\n有迹可循。',70,b=True)
txt(p,80,387,710,72,'从银行官方牌价，到每一次提醒的依据。\n把自动监控、阈值提醒与 AI 助手，放进一个桌面窗口。',21,MUTED)
button(p,80,494,220,'下载 Windows 版');button(p,318,494,180,'查看项目流程',False)
txt(p,80,556,720,35,'仅支持 Windows  ·  完整程序包  ·  解压后启动',14,MUTED)
# Particle globe is a proposed static key visual; animation comes after approval.
random.seed(32)
for _ in range(1800):
 a=random.uniform(0,2*math.pi);z=random.uniform(-1,1);r=math.sqrt(1-z*z);x=r*math.cos(a);depth=r*math.sin(a)
 if depth < -.42:continue
 px=1113+205*x;py=345+205*z
 p.setPen(Qt.PenStyle.NoPen);p.setBrush(QColor('#498878' if depth>.3 else '#C9D9D2'));p.drawEllipse(QRectF(px,py,2+depth,2+depth))
pill(p,1215,183,83,'CNY');pill(p,900,414,83,'USD');pill(p,1228,477,83,'EUR')
rule(p,80,632,1280)
for x,v,s in [(80,'官方牌价','农业银行公开接口'),(420,'双向规则','现汇买入与卖出独立判断'),(850,'有据可查','保存来源、时间与触发依据')]:
 txt(p,x,653,350,40,v,23,b=True);txt(p,x,697,380,30,s,15,MUTED)
rect(p,80,785,1280,850,'#EBF0EE',20,'#EBF0EE')
txt(p,110,798,900,45,'一个窗口，看清每一步变化。',25,b=True)
pill(p,110,858,110,'行情监控',INK,'#FFFFFF');txt(p,247,858,900,34,'AI 助手       预警记录       Agent 流程       连接设置',15,MUTED)
p.drawImage(QRectF(110,915,1220,683),QImage(str(APP)))
txt(p,110,1595,1220,26,'历史运行截图 · 非实时行情。正式页面支持切换与点击放大。',12,MUTED)
section(p,1690,'监控不止于价格。','数据从哪里来、提醒为什么发生，都能找到依据。')
for i,(title,body) in enumerate([('官方当前与历史牌价','区分银行发布时间与程序检查时间，按指定历史日期进行比较。'),('精确判断，分别提醒','买入与卖出分别设线；涨跌达到阈值后，记录本次触发依据。'),('AI 助手与规则协作','对话查询本机记录、协助拟定修改；模型失败时保留规则提醒。')]):
 x=80+i*437
 rule(p,x,1835,405);txt(p,x,1860,405,50,title,25,b=True);txt(p,x,1928,390,100,body,18,MUTED)
 txt(p,x,2030,390,40,'展开功能说明  ＋',15,GREEN)
section(p,2135,'一条提醒，如何产生？','点击步骤查看输入、处理方式与输出。')
steps=['获取官方报价','选择历史基准','计算并判断','模型说明／兜底','通知与留痕']
for i,s in enumerate(steps):
 x=80+i*258;rect(p,x,2285,238,90,INK if i==2 else '#FFFFFF',10,INK if i==2 else LINE)
 txt(p,x+20,2292,200,29,str(i+1).zfill(2),13,'#C3D4CC' if i==2 else MUTED)
 txt(p,x+20,2325,200,35,s,18,'#FFFFFF' if i==2 else INK,True)
rect(p,80,2400,1280,170)
txt(p,110,2415,390,50,'精确计算与阈值判断',27,b=True)
txt(p,550,2420,760,115,'对同一币种、同一买卖方向比较当前价与历史基准。\n按涨跌幅绝对值判断是否达到提醒线；缺少数据时明确暂停。',19,MUTED)
section(p,2640,'工程细节，经得起追问。','项目展示以实际实现和运行证据为依据。')
for i,(title,body) in enumerate([('Python / PySide6','桌面界面与后台采集'),('LangGraph','编排采集、计算与说明'),('SQLite','记录比较、预警与渠道状态'),('模型事实校验','检查输出字段，失败则兜底')]):
 x=80+i*327;txt(p,x,2785,310,45,title,23,b=True);txt(p,x,2845,300,40,body,16,MUTED)
rule(p,80,2930,1280)
txt(p,80,2960,1280,55,'边界也说清楚：60 秒轮询；关闭程序即停止；当前为农行单一来源。',19)
rect(p,80,3100,1280,260,INK,18,INK)
txt(p,120,3130,850,75,'在 Windows 上，亲自体验。',43,'#FFFFFF',True)
txt(p,120,3222,870,80,'了解实际界面与操作，也欢迎留下你的使用体验。\n完整下载说明会在发布前核实并展示。',19,'#C8D3D0')
button(p,1060,3175,250,'下载 Windows 版',False)
txt(p,1060,3250,250,40,'提交体验与建议',17,'#FFFFFF',False,Qt.AlignmentFlag.AlignHCenter)
footer(p,3460);save(im,p,'01-desktop-home.png')

# Mobile design uses its own text/layout rather than shrinking the desktop.
im,p=start(440,2330)
txt(p,24,18,300,45,'汇率观察站',21,b=True);txt(p,369,18,55,45,'菜单',16)
rule(p,0,80,440);pill(p,24,108,180,'Windows 桌面应用')
txt(p,24,160,392,145,'让汇率波动，\n有迹可循。',47,b=True)
txt(p,24,325,392,86,'从银行官方牌价，到每一次提醒的依据。\n在桌面上完成监控、提醒与记录。',18,MUTED)
button(p,24,440,392,'下载 Windows 版')
txt(p,24,505,392,55,'当前手机不能运行此应用。\n可在 Windows 电脑上打开本页下载。',13,MUTED)
rect(p,24,600,392,330,'#EBF0EE')
txt(p,40,615,360,45,'真实界面，先看再下载。',23,b=True)
p.drawImage(QRectF(40,677,360,202),QImage(str(APP)))
txt(p,40,884,360,32,'点击放大 · 历史截图',13,MUTED)
txt(p,24,990,392,90,'价格背后，\n每一步都有依据。',33,b=True)
for i,(a,b) in enumerate([('官方数据','当前与历史牌价，不混淆数据时间。'),('双向提醒','买入、卖出独立设线，达到条件再提醒。'),('AI 协作','查询记录、拟定修改，确认后才保存。')]):
 y=1120+i*145;rule(p,24,y,392);txt(p,24,y+16,360,42,a,24,b=True);txt(p,24,y+64,380,60,b,17,MUTED)
txt(p,24,1595,392,65,'从采集到提醒',31,b=True)
for i,s in enumerate(steps):
 y=1680+i*59;txt(p,24,y,50,45,str(i+1).zfill(2),16,GREEN);txt(p,80,y,330,45,s,19)
rect(p,24,2010,392,190,INK)
txt(p,44,2025,350,50,'用过之后，告诉我。',28,'#FFFFFF',True)
txt(p,44,2086,350,45,'使用体验、改进建议或问题反馈。',15,'#D4DFDA')
button(p,44,2140,350,'填写反馈',False)
txt(p,24,2240,392,55,'移动端设计预览 · 不含真实提交与下载',12,MUTED)
save(im,p,'02-mobile-home.png')

im,p=start(1440,1120);nav(p)
txt(p,80,155,480,120,'你的体验，\n让下一步更清楚。',48,b=True)
txt(p,80,305,440,125,'无论是一个好用的细节，还是一次不顺畅的操作，都欢迎告诉我。',21,MUTED)
rule(p,80,480,430)
txt(p,80,510,430,90,'反馈仅供项目维护者查看。\n联系方式用于必要时沟通，不在网站公开。',17,MUTED)
pill(p,80,642,150,'反馈表单预览')
rect(p,600,140,760,895)
txt(p,635,160,690,48,'意见反馈',28,b=True)
txt(p,635,215,690,40,'姓名必填；电话或邮箱至少填写一项。',16,MUTED)
def field(x,y,w,title,placeholder,h=52):
 txt(p,x,y,w,30,title,15,b=True);rect(p,x,y+39,w,h,'#FAFCFB',7);txt(p,x+15,y+43,w-30,min(h-6,50),placeholder,15,'#85918C')
field(635,275,690,'姓名 *','请输入你的姓名或称呼')
field(635,390,330,'电话','请输入联系电话');field(995,390,330,'邮箱','name@example.com')
txt(p,635,488,690,28,'电话或邮箱至少填写一个；另一项可留空。',13,GREEN)
field(635,540,690,'使用体验（选填）','哪些地方好用，或哪些操作不够顺畅？',70)
field(635,670,330,'改进建议（选填）','你希望增加或改进什么？',100)
field(995,670,330,'问题反馈（选填）','操作步骤、现象或报错…',100)
txt(p,635,842,690,50,'□  我已了解联系方式仅用于处理本次反馈。',14,MUTED)
button(p,635,915,690,'提交反馈')
footer(p,1060);save(im,p,'03-feedback-form.png')

im,p=start(1440,1020)
p.fillRect(0,0,235,1020,QColor(INK))
txt(p,25,22,200,60,'汇率观察站',25,'#FFFFFF',True)
txt(p,25,84,200,35,'私有管理',14,'#B8C7C0')
rect(p,16,175,203,52,'#324C43',8,'#324C43');txt(p,35,175,170,52,'反馈收件箱',17,'#FFFFFF',True)
txt(p,35,920,180,60,'返回介绍页\n退出登录',15,'#C8D4CC')
txt(p,275,27,800,65,'反馈收件箱',32,b=True)
pill(p,1200,40,180,'仅管理员可访问')
txt(p,275,108,1000,40,'查看访客体验与建议，跟进每一次反馈。',17,MUTED)
pill(p,275,178,100,'全部  3',INK,'#FFFFFF');pill(p,392,178,110,'未处理  2');pill(p,520,178,110,'已处理  1')
txt(p,1080,178,310,34,'示例数据 · 非真实访客',13,MUTED)
rect(p,275,245,600,650);rect(p,900,245,495,650)
txt(p,300,260,540,40,'最近反馈',20,b=True)
samples=[('访客 A','截图可以放大，查看更方便。','使用体验','未处理'),('访客 B','希望下载说明里加入启动步骤。','改进建议','未处理'),('访客 C','首次打开时不清楚如何开始监控。','问题反馈','已处理')]
for i,(name,body,kind,status) in enumerate(samples):
 y=325+i*167
 if i==0:rect(p,290,y-5,570,150,'#EDF4F0',9,'#EDF4F0')
 txt(p,310,y+5,210,36,name,19,b=True);txt(p,658,y+5,180,36,status,14,GREEN)
 txt(p,310,y+53,520,55,body,16)
 txt(p,310,y+111,520,25,kind+'    ·    示例日期',12,MUTED)
txt(p,930,267,430,40,'反馈详情',23,b=True)
txt(p,930,325,430,34,'访客 A',22,b=True)
txt(p,930,375,430,80,'联系方式（示例）\nreviewer@example.com',16,MUTED)
rule(p,930,480,430)
txt(p,930,505,430,35,'使用体验',17,b=True)
txt(p,930,550,425,90,'截图可以放大，查看更方便。\n整体介绍清楚，能快速了解应用。',18)
txt(p,930,665,430,70,'改进建议：未填写\n问题反馈：未填写',15,MUTED)
button(p,930,780,265,'标记为已处理');button(p,1210,780,155,'删除',False)
txt(p,275,937,1100,40,'管理页设计预览 · 登录后才可读取反馈 · 联系方式不公开',14,MUTED)
save(im,p,'04-private-admin.png')
