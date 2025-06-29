# 自制免费验证码
利用https://moemail.app/自制免费验证码

第一步：打开https://moemail.app/并注册账户
第二步：注册一个邮箱
第三步：用这个邮箱给一个邮箱发送消息（什么消息都可以），记得抓包
第四步（下面的是叫你如何找都id和cookie）：
请求URL：moemail.app/api/emails/{id}/send
...
请求标头：
...
cookie {cookie}
