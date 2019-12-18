day04数据类型（2）

##### 今日内容

###### 列表

###### 元组



###### 补充

- ​	.startswitch（'XX'）#判断是否已XX开头

  

- ​    .endwith（‘XX'）#判断是否已XX结头

  

- ​    .format （‘X’，‘Y'）字符串格式化

  

- ​    .encode('编码')

  

- ​    .jion字符串拼接

  

- ​    切片升级知识点--->步长  公共功能

  

  

##### 内容详细

##### 1.列表

​	如果想要表示两个同学 users=’陆威，姚婷‘

​	以后想要表示多个’事物‘，可以使用列表。

```
users=['luwei','yaoting',99]
```

###### 公共功能

​	与字符串类似

- len

  ```
  users=['luwei','yaoting',99]
  val=len（users）
  print（val）#3
  ```

- 索引

  ```
  users=['luwei','yaoting',99]
  val=users[0]
  --->'luwei'
  ```

- 切片

  ```
  users=['luwei','yaoting',99]
  val=users[0:1]
  --->'luwei','yaoting'
  ```

- 删除(数字/布尔/字符串除外)---特指del

  ```
  users=['luwei','yaoting',99]
  #方式一 独有功能
  users.pop(1)
  print(users)
  
  #方式二 公共功能
  del users[1]
  print(users)
  ```

  注意：

  ​		1.字符串本身不能修改或删除【不可变类型】

  ​		2.列表是可变类型。

- 修改（字符串/数字/布尔除外）

  ```
  users=['luwei','yaoting',99]
  users[2]=66
  users[0]='laowang'
  users[0][2]-->'w'
  ```

- 步长

  ```
  users=['luwei','yaoting',99]
  val=user[0:2:2]
  -->'luwei',99
  ```

- for循环

  实现输出 （0，老王）（1，小李）（2，小黑）（3，晓红）
  
  ```
users=['老王','小李','小黑','晓红']
  count=0
  for i in users:
      print(count,i)
      count+=1
  ```
  
  ```
  users=['老王','小李','小黑','晓红']
  len_new=len(users)#len长度为4
  #index=0
  for index in range(0,len_new):#range 范围取值 0,1,2,3
      print(index,users[index])
  ```
  
  

###### 独有功能

- .append（）

  在列表最后追加一个元素

  ```
  users=[]
  while True:
      name=input('请输入姓名:')
      users.append(name)
      print(users)
  ```

  示例

  ```python
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
  ```

- .insert（索引，‘元素’）

  在指定索引位置进行插入。

  ```
  users=['老王','小李','小黑','晓红']
  users.insert(2,'luwei')
  print(users)
  -->['老王', '小李', 'luwei', '小黑', '晓红']
  ```



- .remove('元素')

  删除

  ```
  users=['老王','小李','小黑','小黑','晓红']
  users.remove('小黑')#出现多个，删除第一个。
  print(users)
  -->['老王', '小李', '小黑', '晓红']
  ```

- .pop(‘索引’)

  删除

  ```
  users=['老王','小李','小黑','小黑','晓红']
  users.pop()#默认删除最后一个元素
  users.pop(1)#删除索引对应的元素
  print(users)
  -->['老王', '小黑', '小黑']
  ```

  

- .clear()

  删除所有元素

  ```
  users=['老王','小李','小黑','小黑','晓红']
  users.clear()
  print(users)
  -->[]
  ```



列表总结

- 增
  - append/insert

- 删
  - remove/pop/clear/del user[2]

- 改
  - users[3]='新值'

- 查
  - 索引/切片

列表嵌套

```
users=['luwei',0,Ture,[11,22,33,'oldboy']]
users[3]-->[11,22,33,'oldboy']
users[3][3]-->'oldboy'
users[3][3][-1]-->'y'
users[3]='newone' #可以修改，列表是可变类型
users[3][3][-1]='X'#不可以修改，字符串为不可变类型
```



##### 2.元组（tuple）

1.元组格式书写

```
users=['luwei','yaoting',99]	#[]为列表，可变类型
users=('luwei','yaoting',99)	#()为元组，不可变类型(还有int/bool)
```

2.公共功能

​	1.索引（排除: int/bool）

```
users=('luwei','yaoting',99)
print(users[1])
-->yaoting
```

​	2.切片（排除: int/bool）

```
users=('luwei','yaoting',99,88,77)
print(users[0:2])
-->'luwei','yaoting',99
```

​	3.步长（排除: int/bool）

```
users=('luwei','yaoting',99,88,77)
print(users[0:3:2])
-->'luwei,99
```

​	4.修改（排除: int/bool/str/tuple）

​	5.删除（排除:int/bool/str/tuple）

​	6.for循环（排除: int/bool）

```
users=('luwei','yaoting',99,88,77)
for item in users:
	print(item)
```

​	7.len（排除: int/bool）

```
users=('luwei','yaoting',99,88,77)
print(len(users))
-->5
```

3.独有功能(无)

4.特殊：元组中的元素不可被修改

```python
v1=(11,22,33)
v1[1]=999 #错误 元组中的元素不可被修改
v1=999	  #正确 把（11，22，33）看为一个整体

#元组可以被嵌套
v1=(11,22,33,(44,55,66),(11,2,(88,99),3))

#嵌套
v2=[11,22,33,(1,2,3)]
v2[3][1]=99  #错误，元组中的元素不可被修改
v2[3]=999 	#正确，列表中元素可以被修改

#嵌套
v3=(11,22,33,[11,22,33])
v3[3]=99    #错误，元组中的元素不可被修改
v3[3][1]=10 #正确，列表中的元素可被修改
```



##### day04总结

1.解释型语言和编译型语言区别

###### 2.字符串功能

- 独有功能

  ​		1.startswith/endswith

  ​		2.upper/lower

  ​		3.isdigit

  ​		4.strip/rstrip/lstrip

  ​		5.replace

  ​		6.split/rsplit/lsplit

  ​		7.format

  ​		8.encode

  ​		9.jion

- 公共功能

  ​		1.索引

  ​		2.切片

  ​		3.步长

  ​		4.for循环

  ​		5.len

  ​		6.range

- 特性

  ​	不可变，所以字符串元素不可被修改删除



###### 3.列表（可变）

- 公共

  ​	1.索引

  ​	2.切片

  ​	3.步长

  ​	4.修改

  ​	5.删除（del）

  ​	6.for循环

  ​	7.len

  ​	8.extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）

- 独有

  ​	1.append

  ​	2.insert

  ​	3.remove

  ​	4.pop

  ​	5.clear

- 特性

  列表为可变型，可以嵌套

###### 4.元组

- 公共

  ​	1.索引

  ​	2.切片

  ​	3.步长

  ​	4.for循环

  ​	5.len

- 独有功能-无

- 特性

  元组中的元素不可被修改，元组可以嵌套