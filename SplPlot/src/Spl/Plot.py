'''
Created on 2013/10/23

@author: tshimizu
'''



def splitLine(l):
    data = l.lstrip().rstrip().split()
    return data



inFile = '/home2/tshimizu/ES/MMC_AERO/case4/probes/p.dat'
rho = 1.205

f = open(inFile,'r')
datas = []

for line in f:
    datas.append(splitLine(line))
    
for d in datas:
    n = 0
    for i in d:
        n = n + 1
        if n == 1:
            print i,
        else:
            print float(i) * rho,
    print "\n",

if __name__ == '__main__':
    pass