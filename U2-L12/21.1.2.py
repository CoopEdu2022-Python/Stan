file=open('python读写案例.txt',mode='r')
print(file.closed)
print(file.encoding)
print(file.mode)
print(file.name)
file.write()
file.read()
file.seek()
file.flush()
file.isatty()#如果文件连接终端返回True,不然返回False
file.tell()#返回文件位置
file.readline()
file.readlines()
file.writelines
file.close()