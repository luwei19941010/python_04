#-*-coding:utf-8-*-
# Author:Lu Wei

#1.简述解释性语言和编译型语言的区别？
'''
解释型语言 解释一条代码执行一条代码，执行速度慢，调试简单，可快平台。
编译型语言 将代码全部编译完成之后在执行，执行速度快，调试麻烦，不可快平台。

#2.列举你了解的Python的数据类型？
int,bool,str,列表list,元组tuple

#3.写代码，有如下列表，按照要求实现每一个功能。
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
#3.1计算列表的长度并输出
print(len(li))
#3.2请通过步长获取索引为偶数的所有值，并打印出获取后的列表
print(li[2::2])
#3.3列表中追加元素"seven",并输出添加后的列表
li.append('seven')
print(li)
#3.4请在列表的第1个位置插入元素"Tony",并输出添加后的列表
li.insert(0,'Tony')
print(li)
#3.5请修改列表第2个位置的元素为"Kelly",并输出修改后的列表
li[1]='Kelly'
print(li)
#3.6请将列表的第3个位置的值改成 "太白"，并输出修改后的列表
li[2]="太白"
print(li)
#3.7请将列表 l2=[1,"a",3,4,"heart"] 的每一个元素追加到列表li中，并输出添加后的列表
l2=[1,"a",3,4,"heart"]
for item in l2:
    li.append(item)
print(li)
li.extend(l2)
print(li)
#3.8请将字符串 s = "qwert"的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
s='qwert'
li.extend(s)
print(li)
#3.9请删除列表中的元素"ritian",并输出添加后的列表
li.remove('ritian')
print(li)
#4.0请删除列表中的第2个元素，并输出删除元素后的列表
li.pop(1)
print(li)
#4.1请删除列表中的第2至第4个元素，并输出删除元素后的列表
del li[1:4]
print(li)

#请用三种方法实现字符串反转 name = "小黑半夜三点在被窝玩愤怒的小鸟"（步长、while、for）
#步长
name = "小黑半夜三点在被窝玩愤怒的小鸟"
print(name[::-1])
#while
index=1
name1=''
len_new=len(name)
while index<=len_new:
    num=len_new-index
    name1=name1+(name[num])
    index+=1
print(name1)
#for
name2=''
len_new1=len(name)-1
for i in name:
    name2+=name[len_new1]
    len_new1-=1
print(name2)

#5.写代码，有如下列表，利用切片实现每一个功能
li = [1, 3, 2, "a", 4, "b", 5,"c"]
#5.1通过对li列表的切片形成新的列表 [1,3,2]
print(li[0:3])
#5.2通过对li列表的切片形成新的列表 ["a",4,"b"]
print(li[3:6])
#5.3通过对li列表的切片形成新的列表 [1,2,4,5]
print(li[::2])
#5.4通过对li列表的切片形成新的列表 [3,"a","b"]
print(li[1:6:2])
#5.5通过对li列表的切片形成新的列表 [3,"a","b","c"]
print(li[1::2])
#5.6通过对li列表的切片形成新的列表 ["c"]
print(li[-1])
#5.7通过对li列表的切片形成新的列表 ["b","a",3]
print(li[-3::-2])


#6.请用代码实现循环输出元素和值：users = ["武沛齐","景女神","肖大侠"] ，如：
# 0 武沛齐
# 1 景女神
# 2 肖大侠
users = ["武沛齐","景女神","肖大侠"]
#1.
for item in users:
    print(users.index(item),item)
#2.
count=0
for item in users:
    print(count,item)
    count+=1


#7.请用代码实现循环输出元素和值：users = ["武沛齐","景女神","肖大侠"] ，如：
# 1 武沛齐
# 2 景女神
# 3 肖大侠
users = ["武沛齐","景女神","肖大侠"]
#1.
count=1
for item in users:
    print(count,item)
    count+=1


#8.写代码，有如下列表，按照要求实现每一个功能。
lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]

#8.1将列表lis中的"k"变成大写，并打印列表。
lis[3][2][0]=lis[3][2][0].upper()
print(lis)
#8.2将列表中的数字3变成字符串"100"
lis[1]='100'
lis[3][2][1][1]='100'
print(lis)
#8.3将列表中的字符串"tt"变成数字 101
lis[3][2][1][0]=101
print(lis)
#8.4在 "qwe"前面插入字符串："火车头"
lis[3].insert(0,'火车头')
print(lis)



#9.写代码实现以下功能
#9.1如有变量 googs = ['汽车','飞机','火箭'] 提示用户可供选择的商品：
while True:
    googs = ['汽车','飞机','火箭']

    for item in googs:
        print(googs.index(item),',',item)
    num=int(input('请选择：'))
    print(googs[num])

googs = ['汽车','飞机','火箭']
for i in range(0,goods)
    print (i,goods[i])



#10.请用代码实现,利用下划线将列表的每一个元素拼接成字符串"a_l_e_x"
li = "alex"
li_new='_'.join(li)
print(li_new)


#11.利用for循环和range找出 0 ~ 100 以内所有的偶数，并追加到一个列表。
li=[]
for i in range(0,101):
    if i%2==0:
        li.append(i)
print(li)




#12.利用for循环和range 找出 0 ~ 50 以内能被3整除的数，并追加到一个列表。
li=[]
for i in range(0,51):
    if i%3==0:
        li.append(i)
print(li)

#13.利用for循环和range 找出 0 ~ 50 以内能被3整除的数，并插入到列表的第0个索引位置，最终结果如下：
li=[]
for i in range(0,51):
    if i%3==0:
        li.insert(0,i)
print(li)



#14.查找列表li中的元素，移除每个元素的空格，并找出以"a"开头，并添加到一个新列表中,最后循环打印这个新列表。
li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", "  aqc"]
li1=[]
for i in li:
    li[li.index(i)]=i.strip()
for i in li:
    if i.startswith('a'):
        li1.append(i)
print(li1)


#15.判断是否可以实现，如果可以请写代码实现。

li = ["alex",[11,22,(88,99,100,),33] ,"WuSir", ("ritian", "barry",), "wenzhou"]
#请将 "WuSir" 修改成 "武沛齐"
li[2]="武沛齐"
print(li)
#请将 ("ritian", "barry",) 修改为 ['日天','日地']
li[3]=['日天','日地']
print(li)
#请将 88 修改为 87
li[1][2]=(87,99,100,)
print(li)
#请将 "wenzhou" 删除，然后再在列表第0个索引位置插入 "文周"
li.pop()
li.insert(0,"文周")
print(li)



while True:
    googs = ['汽车','飞机','火箭']
    for  i  in range(0,len(googs)):
        print(i+1,googs[i])

    choice=int(input('choice num:'))
    print(googs[choice-1])

value=[]
for i in range(0,9,1):
    value.append(i)
print(value)

for i in range(10,0,-1):
    value.append(i)
print(value)

'''





















