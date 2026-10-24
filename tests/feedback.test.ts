import {test} from 'node:test';import assert from 'node:assert/strict';import {validateFeedback} from '../lib/feedback.ts';
const base={name:'测试访客',email:'test@example.com',consent:true};
test('姓名加邮箱即可提交，体验建议问题都选填',()=>{assert.equal(validateFeedback(base).problem,'');});
test('允许姓名加电话',()=>assert.equal(validateFeedback({name:'A',phone:'13800000000',consent:true}).email,''));
test('缺少姓名或联系方式拒绝',()=>{assert.throws(()=>validateFeedback({...base,name:''}));assert.throws(()=>validateFeedback({name:'A',consent:true}));});
test('邮箱、电话、超长内容和未同意均拒绝',()=>{for(const input of [{...base,email:'bad'},{...base,phone:'abc'},{...base,problem:'x'.repeat(3001)},{...base,consent:false},{...base,name:2}])assert.throws(()=>validateFeedback(input));});
test('机器人字段与非对象输入被拒绝',()=>{assert.throws(()=>validateFeedback({...base,website:'spam'}));assert.throws(()=>validateFeedback(null));});
