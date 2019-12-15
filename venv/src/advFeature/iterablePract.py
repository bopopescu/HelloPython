def findMinAndMax(L):
    if L==[]:
        return (None,None)
    max=L[0]
    min=L[0]
    for num in L:
        if int(num)>=max:
            max=num
        if int(num)<=min:
            min=num
    return min,max

# 测试
if findMinAndMax([]) != (None, None):
    print(findMinAndMax([]))
    print('测试失败!1')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!2')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!3')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!4')
else:
    print('测试成功!')

for i,value in enumerate(['a','b','c']):
    print(i,value)