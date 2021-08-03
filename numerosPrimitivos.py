for n in range(2, 200):
    for x in range(2, n):
        if n % x == 0:
            #print(n, ' igual ', x, '*', n//x)
            break;
    else: 
        print(n)