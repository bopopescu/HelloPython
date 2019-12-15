def trim(str):
    if str[:1]==' ':
        return trim(str[1:])
    if str[-1:]==' ':
        return trim(str[:-1])
    return str

s='    sjhfkja asdfj '

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

print(None=='')