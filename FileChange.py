"""
读取ProCAST温度场数据，输出符合ABAQUS
input syntax rules 格式的节点集、幅值及预定义场
License：nwpu-zhxd
"""
import sys

time_step_interval = int(sys.argv[1])

try:
    f_time_log = open('t.log')
except IOError:
    print('t.log文件不存在!')
    sys.exit(2)

try:
    f_temp = open('t.ntl')
except IOError:
    print('t.ntl文件不存在!')
    sys.exit(2)

f_time = open('time.txt', 'w')
#starttime=datetime.datetime.now()
if f_time_log:
    content = f_time_log.readlines()

    for line in content:
        list_1 = line.split(sep=',')
        #print(list_1)
        list_2=list_1[1].split()
        #print(list_2)
        f_time.write(list_2[2])
        f_time.write('\n')

f_time.close()
f_time_log.close()

f_time = open('time.txt')
f1=open('Amplitude.txt','w')
f2=open('Nset.txt','w')
f3=open('PreField.txt','w')

f_temp.readline()
lis1=f_temp.readline().split()
npoints=int(lis1[0])
ntime=int(lis1[4])
# print(npoints)
# print(ntime)
f_temp.readline()


for i in range(npoints):
    str1=f_temp.read(int(ntime)*14+8+int(ntime)//5+1)
    lis2=str1.split()
    d=int(lis2[0])
    #f1.write(r'*Amplitude, ')
    f1.write('*Amplitude, name=Amp-%d, time=TOTAL TIME\n' % d)
    #f2.write(r'*Nset, ')
    f2.write('*Nset, nset=data%d, instance=PART-1-1\n%d,\n'%(d, d))
    #f3.write(r'*Temperature, ')
    f3.write('*Temperature, op=NEW, amplitude=Amp-%d\ndata%d, 1.\n' % (d,d))
    #f3.write('data%d, 1.\n' % d)
    kn = 0
    for j in range(1, ntime+1, time_step_interval):
        kn += 1
        t=f_time.readline()
        #t1=ConvertELogStrToValue(t)
        t=t.strip('\n')
        t=float(t)
        # print(t1)
        p=float(lis2[j])
        f1.write('%15.2f, %15.2f' % (t, p))
        if (kn % 4)==0:
            f1.write('\n')
        else:
            if ((j+time_step_interval)>ntime) and ((ntime % 4) !=0):
                f1.write('\n')
                break
            else:
                f1.write(',')
        for i in range(time_step_interval-1):
            t=f_time.readline()

    f_time.seek(0)
#endtime = datetime.datetime.now()
#print((endtime - starttime).seconds)
f_temp.close()
f_time.close()
f1.close()
f2.close()
f3.close()
