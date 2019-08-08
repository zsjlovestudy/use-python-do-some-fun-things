import itertools as it
n = 6
blank = n*n
chest = [[0]*n for i in range(n)]
comb = it.combinations(list(range(blank)),n)

def check(x,y):
        if max(chest[x]) == 1:
                return False
        if max([chest[i][y] for i in range(n)]) == 1:
                return False
        for i in range(n):
                for j in range(n):
                        if i+j == x+y or i-j == x-y:
                                if chest[i][j] == 1:
                                        return False
        return True

queen = 0
c = 0
for each in comb:
        for e in each:
                x = e//n
                y = e%n
                if check(x,y):
                        chest[x][y] = 1
                        queen += 1
                else:
                        chest = [[0]*n for i in range(n)]
                        queen = 0
                        break
        if queen == n:
                c += 1
                print ('Solution %d:' % c)
                for q in chest:
                        print (q)
                print ('*'*20)
                chest = [[0]*n for i in range(n)]
                queen = 0