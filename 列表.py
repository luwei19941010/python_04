#-*-coding:utf-8-*-
# Author:Lu Wei

'''
users=['老王','小李','小黑','晓红']
count=0
for i in users:
    print(count,i)
    count+=1


users=['老王','小李','小黑','晓红']
len_new=len(users)#len长度为4
#index=0
for index in range(0,len_new):#range 范围取值 0,1,2,3
    print(index,users[index])
'''


##########列表独有功能#############
''''
#.append() 追加在列表最后
users=[]
while True:
    name=input('请输入姓名:')
    users.append(name)
    print(users)

users=[]
for i in range (0,3):
    name=input('请输入姓名:')
    users.append(name)
print(users)
username=input('username:')
password=input('password:')
for item in users:
    result=item.split(',')
    user=result[0]
    psw=result[1]
    if username==user and password == psw:
        print('OK')
    else:
        print('NO')

#.insert()在指定索引位置进行插入
users=['老王','小李','小黑','晓红']
users.insert(2,'luwei')
print(users)

'''
#.remove(元素)
users=['老王','小李','小黑','小黑','晓红']
users.remove('小黑')#出现多个，删除第一个。
print(users)

#.pop(索引位置)
users=['老王','小李','小黑','小黑','晓红']
users.pop()#默认删除最后一个元素
users.pop(1)#删除索引对应的元素
print(users)

#clear() 清除所有表项
users=['老王','小李','小黑','小黑','晓红']
users.clear()
print(users)
users=('luwei','yaoting',99,88,77)
print(users[0:3:2])
