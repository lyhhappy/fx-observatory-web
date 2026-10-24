import type {Metadata} from 'next';import './globals.css';import {Shell} from '@/components/Shell';
export const metadata:Metadata={title:{default:'汇率观察站 · 官方牌价监控',template:'%s | 汇率观察站'},description:'一个关于官方银行牌价、精确提醒规则与 AI 协作的 Windows 桌面项目。查看真实界面、实现流程，下载体验并留下建议。'};
export default function RootLayout({children}:{children:React.ReactNode}){return <html lang="zh-CN"><body><a className="skip" href="#main">跳到主要内容</a><Shell>{children}</Shell></body></html>}
