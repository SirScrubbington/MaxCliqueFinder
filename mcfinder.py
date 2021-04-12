import random
from os import getcwd
from os import listdir
from os.path import isfile, join

cwd = getcwd() + '/data'

files = [f for f in listdir(cwd) if isfile(join(cwd, f))]
loaded=False

def GenList(f):
    nodes = 0
    updates = 0

    # Adjacency List:
    n = dict()

    for line in f:
        l = line.split()
        if l[0] == 'c':
            # Comment, no action
            pass
        elif l[0] == 'p':
            # Used to validate data
            nodes = int(l[2])
            updates = int(l[3])
            for i in range(nodes + 1):
                n[i] = list()
            pass
        elif l[0] == 'e':
            n[int(l[1])].append(int(l[2]))
            n[int(l[2])].append(int(l[1]))
            pass
    return n

def GenMatrix(n):
    keys = sorted(n.keys())
    s = len(keys)
    M = [[0] * s for i in range(s)]

    for k, v in [(keys.index(k), keys.index(v)) for k, row in n.items() for v in row]:
        M[k][v] = 2 if (k == v) else 1
    return M

def FindMaxClicque(L,M,p):
    clique=[]
    clique.append(p)

    inclique=True

    upper=p+1
    lower=p-1

    while upper < len(L) or lower > 0:
        if lower > 0:

            if inclique==True:
                clique.append(lower)
            pass
            inclique=True
        if upper < len(L):
            for i in range(len(L[upper])):
                print(L[upper][i])
                pass
            print("pass")
            if inclique==True:
                clique.append(upper)
            pass
            inclique=True

        upper+=1
        lower-=1

    return clique

def RandomRestart(L,M):
    length = 0
    largest = list()

    for i in range(1):
        c = FindMaxClicque(L, M, random.randint(1,800))
        if len(c) > length:
            largest = c
            length = len(c)

    return largest

print("Welcome to Graph Maximum Clicque Finder!\nFiles in Directory:\n")

while loaded == False:
    for i in range(len(files)):
        print(i,files[i])
    try:
        index = int(input("\nEnter the number: "))
        f = open(files[index],'r')
        print("Successfully loaded",files[index],".")
        loaded=True
    except FileNotFoundError:
        print("File not found. Was it misspelt?")

L = GenList(f)
M = GenMatrix(L)

length = 0

c = RandomRestart(L,M)

print(c)
print(len(c))