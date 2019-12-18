
#-*-coding:utf-8-*-
# Author:Lu Wei

###########1. .startswith/endswith########
name='luwei'
#判断是否已lu开头
flag=name.startswith('lu')
print(flag)
#判断是否已ei结束
flag1=name.endswith('ei')
print(flag1)


##########2. format##########

name='我叫{0}，年龄：{1}'.format('oldboy',73)
print(name)


##########3. encode##########
name='陆威'#解释器读取到内存后，按照unicode编码存储：8个字节
v1=name.encode('utf-8')
print(v1)
v2=name.encode('gbk')
print(v2)

#########4. jion############
name='luwei' #l_u_w_e_i
result='_'.join(name)#循环每个元素，并在元素和元素直接加入连接符
print(result)

#########公共功能#############
#########1.步长##############
name='luweiluwei'
val=name[0:-1:2]#格式name[x:y:z] z为步长值可以为负，表示从左
val1=name[-1:0:-1]
print(val1)
##########笔试题，请将字符串反转#############
val2=name[::-1]
print(val2)
