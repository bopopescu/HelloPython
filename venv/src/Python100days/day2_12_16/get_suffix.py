def getSuffix(fileName,hasDot=True):
    pos=fileName.rfind('.')
    if 0<pos<len(fileName)-1:
        index=pos if hasDot else pos+1
        return fileName[index:]
    return ''

if __name__=='__main__':
    print(getSuffix('asdfsdf'))