import os
import math,urllib.request,time

if not os.path.exists('tb'):
    os.mkdir('tb')
    os.mkdir('tb2')
    print(os.listdir(os.getcwd()))
    # print(os.getcwd())
    if not os.path.exists('tb/test.txt'):
        f = open('tb/test.txt','w')
        f.write("hello~~~~")
        f.close()


        #只能删除空的目录
        os.removedirs('tb2')

#返回时间戳
print(time.time())
print(time.asctime())
#time.localtime() 返回时间元组
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

#返回2天前的当前时间
two_days_before = time.time() - 60*60*24*2

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(two_days_before)))

print(urllib.request.urlopen("http://www.baidu.com").status)

print(math.ceil(5.5))
print(math.floor(4.3))
print(math.sqrt(9))

