// 单次比较演示：本地样例，不连接银行、模型或通知服务。
const SCALE=100000000n;
function fixed(value:string){
 if(!/^\d+(\.\d{1,8})?$/.test(value)||value.length>20)throw Error('请输入有效的非负数字，最多8位小数。');
 const [whole,fraction='']=value.split('.');
 return BigInt(whole)*SCALE+BigInt(fraction.padEnd(8,'0'));
}
export function evaluateDemo(current:string,baseline:string,threshold:string){
 const price=fixed(current),base=fixed(baseline),limit=fixed(threshold);
 if(price<=0n||base<=0n||price>1000000n*SCALE||base>1000000n*SCALE||limit>100n*SCALE)throw Error('报价须大于0且不超过100万，提醒线为0～100%。');
 const difference=price-base;
 return {hit:(difference<0n?-difference:difference)*100n*SCALE>=base*limit,change:Number(difference)/Number(base)*100};
}
export const demoQuotes={
 HKD:{name:'港币',buy:{current:'0.84894',baseline:'0.85003'},sell:{current:'0.85234',baseline:'0.85343'}},
 USD:{name:'美元',buy:{current:'6.65721',baseline:'6.66130'},sell:{current:'6.68523',baseline:'6.68933'}},
 EUR:{name:'欧元',buy:{current:'7.44052',baseline:'7.45741'},sell:{current:'7.49278',baseline:'7.50979'}},
};
