'use client';
import {useState} from 'react';
const currencies=[
 {code:'CNY',name:'人民币',description:'计价基准：页面中的报价，以人民币 / 1 单位外币表示。',position:'cny'},
 {code:'USD',name:'美元',description:'基础监控币种：现汇买入与卖出，可以分别设置提醒线。',position:'usd'},
 {code:'EUR',name:'欧元',description:'对照指定历史日期，查看当前牌价的上涨与下跌幅度。',position:'eur'},
];
const points=Array.from({length:850},(_,i)=>{const z=1-2*(i+.5)/850;const radius=Math.sqrt(1-z*z);const phi=i*2.399963;return {x:250+220*radius*Math.cos(phi),y:250+220*z,opacity:.2+.7*(Math.sin(phi)+1)/2};});
export function Globe(){
 const [selected,setSelected]=useState(0);const [paused,setPaused]=useState(false);
 return <div className="globe"><div className="globe-stage"><svg viewBox="0 0 500 500" className={paused?'is-paused':''} aria-hidden="true">{points.map((v,i)=><circle key={i} cx={v.x} cy={v.y} r="1.7" opacity={v.opacity}/>)}</svg>{currencies.map((currency,i)=><button key={currency.code} className={'currency '+currency.position} aria-label={'查看'+currency.name+'说明'} aria-pressed={selected===i} onClick={()=>setSelected(i)}>{currency.code}</button>)}</div><div className="globe-caption"><div aria-live="polite"><strong>{currencies[selected].name} / {currencies[selected].code}</strong><p>{currencies[selected].description}</p></div><button className="orbit-toggle" onClick={()=>setPaused(!paused)} aria-pressed={paused}>{paused?'继续动效':'暂停动效'}</button></div><span className="globe-hint">点击球体上的币种，了解监控方式</span></div>;
}
