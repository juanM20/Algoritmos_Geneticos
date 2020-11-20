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

def CMintercambio(p1):
    x = random.randint(0, (len(p1)-1))
    y = random.randint(0, (len(p1)-1))
    mp1 = [] 
    while x == y:
        x = random.randint(0, (len(p1)-1))
        y = random.randint(0, (len(p1)-1))
    else:
        a = p1[x]
        b = p1[y]
        p1[y] = a
        p1[x] = b
    return p1
         
            

if __name__ == "__main__":
    p1 = [1,0,1,0,1,1]
    p2 = [0,0,1,1,0,0]
    h1, h2 = Cpunto(p1,p2)
    CMintercambio(p1)
    print(h1,h2,p1)
    pass


