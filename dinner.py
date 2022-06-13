#创建个list 用于存放被邀请人的信息
import self as self

dinner =['张伟','王斌','李四']
print(dinner)
## dinner.a
print(dinner[0])
print('诚挚的邀请您：'+dinner[0]+'、'+dinner[1]+'、'+dinner[2]+' 来参加晚宴！')
# 查询
print("无法参与晚宴的客户是："+dinner[1])
# 修改
dinner[1]='贺五'
print('诚挚的邀请您：'+dinner[0]+'、'+dinner[1]+'、'+dinner[2]+' 来参加晚宴！')
print('我找到了一个更大的餐桌')
# 添加，指定位置，具体值的元素
dinner.insert(0,'斗五')
print(dinner)
dinner.insert(4,'斗五22')
print(dinner)
# 列尾部添加 ， 固定的
dinner.append('末尾用户')
print('诚挚的邀请您：'+dinner[0]+'、'+dinner[1]+'、'+dinner[2]+'、'+dinner[3]+'、'+dinner[4]+'、'+dinner[5]+' 来参加晚宴！')
print("不好意思，因餐桌无法及时送到，只能邀请两位用户参加！！！")
# 弹出
pop_dinner1=dinner.pop(5)
print('非常抱歉，无法邀请您参加晚宴：'+pop_dinner1)
pop_dinner4=dinner.pop(4)
print('非常抱歉，无法邀请您参加晚宴：'+pop_dinner4)
pop_dinner3=dinner.pop(3)
print('非常抱歉，无法邀请您参加晚宴：'+pop_dinner3)
pop_dinner2=dinner.pop(2)
print('非常抱歉，无法邀请您参加晚宴：'+pop_dinner2)
print(dinner)
#删除
dinner.remove('斗五')
print(dinner)
del dinner[0]
print(dinner)
