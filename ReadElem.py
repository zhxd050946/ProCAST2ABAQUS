import re

n=0
f1=open('mokeele.txt','w')
with open('moke.inp') as f:
    content=f.readlines()
    #print(content)
    for line in content:
        ind = re.search('ELEMENT',line)
        if ind !=None:
            # print(ind)
            break
        else:
            n=n+1

    k=0
    for line in content[n+1:]:
        k+=1
        list_1=line.split()
        f1.write(list_1[0])
        if k%16==0:
            f1.write('\n')
        else:
            f1.write(' ')
f1.close()
