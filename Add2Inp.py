"""
此程序将节点集、幅值及预定义温度场自动写入job.inp文件.
license:NWPU-zhxd
"""

try:
    inp_file = open( "chushijob.inp", "r" )
except IOError:
    print('chushijob.inp文件不存在!\n请拷贝inp文件并重命名为chushijob.inp!')
    sys.exit(2)
try:
    amplitude_file = open("Amplitude.txt","r")
except IOError:
    print('Amplitude.txt文件不存在!')
    sys.exit(2)
try:
    nset_file = open('NSet.txt', 'r')
except IOError:
    print('Nset.txt文件不存在!')
    sys.exit(2)
try:
    pretemp_file = open('PreTemper.txt', 'r')
except IOError:
    print('PreTemper.txt文件不存在!')
    sys.exit(2)

inp_content = inp_file.readlines()
amplitude_content = amplitude_file.readlines()
nset_content = nset_file.readlines()
pretemp_content = pretemp_file.readlines()
inp_file.close()
amplitude_file.close()
nset_file.close()
pretemp_file.close()

# 添加Nset到inp文件
s=[s for s in inp_content if '*Nset, nset=Set-' in s]
nset_index = inp_content.index(s[0])
inp_content[nset_index: nset_index+2] = nset_content

#添加Amplitude到inp文件
s=[s for s in inp_content if '*Amplitude' in s]
nset_index = inp_content.index(s[0])
inp_content[nset_index: nset_index+2] = amplitude_content

#添加PreTemper到inp文件
s=[s for s in inp_content if '*Temperature' in s]
nset_index = inp_content.index(s[0])
inp_content[nset_index: nset_index+2] = pretemp_content

#写最终job.inp文件，此文件可直接ABAQUS仿真
f = open('job.inp', 'w')
for i in inp_content:
    f.write(i)
f.close()
