# 汇率观察站网站

独立 Next.js 多页面网站。原 Python 应用不变。

## 本地使用

1. 双击「启动本地网站.cmd」，或在本目录执行 npm run dev。
2. 打开 http://127.0.0.1:3000。
3. 反馈保存到 local-data/feedback.sqlite，管理员入口 /admin。
4. 本机管理员密码见本目录隐藏文件 .env.local 的 LOCAL_ADMIN_PASSWORD；不要上传该文件或在聊天粘贴密码。Supabase 模式改用其管理员账户。

首页、效果总览、三个效果详情、技术页、下载页、反馈、隐私说明和私有管理入口均独立。截图来自原应用历史记录，不是实时行情。网页不调用 DeepSeek 或银行接口。

## 检查

npm test；npm run typecheck；npm run build。
本地数据库使用 Node.js 24 的 node:sqlite，请使用 Node.js 24 LTS。

## Vercel + Supabase 上线准备

1. 创建自己的免费 Supabase 项目，在 SQL 编辑器执行 supabase/schema.sql。
2. 禁用公开注册，只手动创建维护者账户。记录其用户 UUID 作为 ADMIN_USER_ID。
3. 在 Vercel 导入本项目的独立仓库，使用 Next.js 框架设置。配置 DATA_MODE=supabase、SUPABASE_URL、SUPABASE_PUBLISHABLE_KEY、SUPABASE_SECRET_KEY、ADMIN_USER_ID、至少32字符的 SESSION_SECRET。
4. 上述变量全部只在服务器使用。不要加 NEXT_PUBLIC_ 前缀。访问管理接口时服务器验证 Supabase 用户并检查固定管理员 UUID。匿名角色没有反馈表读写权限，只有服务器处理反馈提交。
5. DOWNLOAD_URL 设置已发布的 HTTPS 完整包链接。建议 GitHub Releases 承载大型安装包，不将安装包或运行数据提交网站源码。Supabase 免费存储单文件上限50MB，原应用压缩包可能超过此限制。
6. 上线后逐项验证反馈提交、管理员权限、状态变更、删除及下载，才能宣称云端联调通过。

本次只本地搭建，不创建云端项目、不购买服务、不自动发布。免费方案有流量与使用限制，Supabase 免费项目可能因长期不活跃暂停。使用前核实官方当前额度；不承诺永久免费或持续可用。

## 数据与安全

- .env.local、local-data、安装包、浏览器测试结果均被 Git 忽略。
- Vercel 禁止本地数据库模式；缺少云配置会明确报错，不假装保存。
- 提交和登录有基于摘要的15分钟频率控制；反馈仅供单个维护者查看，删除需二次确认。
- 本地包仅从原程序 EXE 和 _internal 制作，不复制原数据库、邮箱配置、独立密钥文件及日志。原程序内置API行为保留；不会把其密钥显示到网页。
- 官网内容不含虚构客户、认证或未经验证的真实AI对话成功案例。
