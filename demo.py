
def file_create(filename, content):
    filepath = 'C://temp/'
    fullpath = filepath + filename + '.txt'
    file = open(fullpath, 'w')
    file.write(content)
    file.close()



file_create('hello', 'hello world!!!')
