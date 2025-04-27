if __name__ == '__main__':
    N = int(input())

    list = list()
    opt = ''
    x = pos = 0
    for i in range(N):
        cmd = input().split(' ')
        
        opt = cmd[0]
        print(opt, x, pos)
        if opt == 'print':
            print(list)
        elif opt == 'append':
            x = int(cmd[1])
            list.append(x)

        elif opt == 'insert':
            x = int(cmd[2])
            pos = int(cmd[1])
            list.insert(pos, x)

        elif opt == 'remove':
            x = int(cmd[1])
            list.remove(x)

        elif opt == 'pop':
            list.pop()
        elif opt == 'sort':
            list.sort()
        else:
            list.reverse()
