
list = [1,22,3,3,4,5,'hello', 'hello']
result = dict((i,list.count(i)) for i in list if list.count(i)>1)
print(result)






