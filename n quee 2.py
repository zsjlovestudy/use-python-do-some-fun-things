#coding:utf-8
#Define 'N' queens problem:
n = 8
#initiate:
chest = [[0] * n for i in range(n)] #define the matrix
result = [] #put all the results in the list.
tmp = [] #put the queens' position in tmp as "1-D" list.
queen = 0 #check the queens has been put.
c = 0 #calculate the solutions.

#define reset function:
def reset():
        global chest, tmp, queen
        chest = [[0] * n for i in range(n)]
        tmp = []
        queen = 0

#define the position (x,y) can put the queen or not:
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

#define the main loop to put the queens:
def main():
        global c
        if len(tmp) == n:
                result.append(tmp)
                c += 1
                print ('Solution %d:' % c)
                show = [[0] * n for i in range(n)]
                for i in range(n):
                        show[i][tmp[i]] = 1
                        print (show[i])
                print ()
                reset()
        for i in range(n):
                y = i
                x = len(tmp)
                if check(x,y) and tmp+[y] not in result:
                        tmp.append(y)
                        chest[x][y] = 1
                        main()
                        try:
                                chest[x][y] = 0
                                tmp.remove(y)
                        except:
                                print ('Total Solution %d, done!' % len(result))
                                exit()

if __name__ == "__main__":
        main()