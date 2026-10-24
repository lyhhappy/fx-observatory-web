import fs from 'node:fs';import crypto from 'node:crypto';
const manifest=JSON.parse(fs.readFileSync('local-data/downloads/manifest.json','utf8'));
const response=await fetch('http://127.0.0.1:3000/api/download');if(response.status!==200)throw Error('Download unavailable');
const hash=crypto.createHash('sha256');let bytes=0;
for await(const chunk of response.body){bytes+=chunk.byteLength;hash.update(chunk);}
if(bytes!==manifest.bytes||hash.digest('hex')!==manifest.sha256)throw Error('Downloaded archive does not match');
const home=await (await fetch('http://127.0.0.1:3000')).text();if(!home.includes('logo.png')||!home.includes('/showcase'))throw Error('Homepage missing expected components');
fs.writeFileSync('docs/本地验收记录.md',`# 本地验收记录\n\n日期：2026-10-24。实现 Next.js 多页面站点，不配置或部署云端资源。\n\n- 7项输入与请求来源测试通过。\n- TypeScript检查、Next.js生产构建通过。\n- 10个页面HTTP响应正常。\n- 未登录读取和删除反馈被拒绝，跨来源提交被拒绝。\n- 姓名与联系方式校验、实际反馈提交、管理员登录、标记已处理、独立SQLite连接读取持久化结果、删除验收记录通过。\n- 测试只使用明确标记的本地验收反馈，完成后已删除。\n- Windows完整程序ZIP解压校验通过，本地下载${bytes}字节，流式SHA256与源包一致。未复制个人数据库、邮件配置或独立密钥文件。\n- 浏览器客户端静态产物扫描未发现本地管理员密码和会话签名密钥。\n- 原应用Git main工作区保持干净。\n\n## 未验收范围\n\n浏览器访问授权未通过，因此未完成实际浏览器视觉、手机布局、截图放大、菜单切换或键盘交互验收。已写对应代码，不将HTTP成功等同于UI验收。\nSupabase云端数据库、RLS、Auth及Vercel部署均未配置、未联调。后续按用户要求在本地代码确认后处理。\n\n## 使用入口\n\n本地地址：http://127.0.0.1:3000。当前运行的是生产构建。停止后可双击根目录启动本地网站.cmd，以开发模式运行。管理员入口/admin，本机密码见隐藏文件.env.local；不要提交或公开该文件。\n`, 'utf8');
console.log('PASS: Download stream integrity, bytes:',bytes,'; local verification report saved.');
