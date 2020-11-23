import random

def Cpunto(p1,p2):
    x = random.randint(0, (len(p1)-1))
    h1 = [] 
    h2 = []
    for i in range(x):
        h1.append(p1[i]) 
        h2.append(p2[i])
    for n in range(x,len(p2)): 
        h1.append(p2[n])
        h2.append(p1[n])
    return h1, h2