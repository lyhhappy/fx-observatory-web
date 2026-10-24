'use client';
import {useId,useRef,useState} from 'react';
import {workflow} from '@/lib/content';
export function Workflow(){
 const [index,setIndex]=useState(2);const id=useId();const buttons=useRef<(HTMLButtonElement|null)[]>([]);
 function move(key:string){if(key==='Home')return 0;if(key==='End')return workflow.length-1;if(key==='ArrowRight'||key==='ArrowDown')return (index+1)%workflow.length;if(key==='ArrowLeft'||key==='ArrowUp')return (index+workflow.length-1)%workflow.length;return null;}
 return <><div className="workflow-tabs" role="tablist" aria-label="处理步骤">{workflow.map((step,i)=><button key={step.title} ref={element=>{buttons.current[i]=element;}} id={id+'-tab-'+i} role="tab" aria-selected={index===i} aria-controls={id+'-panel'} tabIndex={index===i?0:-1} onClick={()=>setIndex(i)} onKeyDown={event=>{const next=move(event.key);if(next!==null){event.preventDefault();setIndex(next);buttons.current[next]?.focus();}}}><span>{String(i+1).padStart(2,'0')}</span>{step.title}</button>)}</div><div id={id+'-panel'} className="workflow-detail" role="tabpanel" aria-labelledby={id+'-tab-'+index} tabIndex={0}><h3>{workflow[index].title}</h3><p>{workflow[index].body}</p></div></>;
}
