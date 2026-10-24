import {test} from 'node:test';
import assert from 'node:assert/strict';
import {evaluateDemo} from '../lib/monitor-demo.ts';

test('历史港币样例在0.1%处触发，在0.2%处不触发',()=>{
 assert.equal(evaluateDemo('0.84894','0.85003','0.1').hit,true);
 assert.equal(evaluateDemo('0.84894','0.85003','0.2').hit,false);
});
test('上涨下跌与等于阈值边界均正确',()=>{
 assert.equal(evaluateDemo('101','100','1').hit,true);
 assert.equal(evaluateDemo('99','100','1').hit,true);
 assert.equal(evaluateDemo('100.99999999','100','1').hit,false);
 assert.equal(evaluateDemo('100','100','0').hit,true);
});
test('变化正负方向正确，输入无效时不产生假结果',()=>{
 assert(evaluateDemo('99','100','1').change<0);
 for(const values of [['0','1','1'],['1','0','1'],['1','1','-1'],['NaN','1','1'],['1','1','101'],['1e2','1','1'],['1','1','0.123456789']]){
  assert.throws(()=>evaluateDemo(...values as [string,string,string]));
 }
});
