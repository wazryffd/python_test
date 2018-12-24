'''
数据json格式化保存、读取
'''
import json

dic = {'name':'ffd', 'age':'18', 'height':'175'}

f = open('a.txt','w')
j_data = json.dumps(dic)
f.write(j_data)
f.close()
print(j_data)
print(type(j_data))


f_read = open('a.txt','r')
j_read_data = json.loads(f_read.read())
print(j_read_data)
print(type(j_read_data))
f.close()
