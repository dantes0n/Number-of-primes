import sys
n = int(input("Please enter the amount of first natural numbers .\n"))
if n == 0:
    print("Program stopped by the user")
    sys.exit()
else:
    p = 0
    for i in range(0,n-1):
        s = 0
        for j in range(0,i+2):
            if (i+2)%(j+1) == 0:
                s += 1
        if s == 2:
            p += 1

    print(p, "of those numbers are primes .\n")
while n != 'stop':
    n = int(input("Please enter the amount of first natural numbers .\n"))
    if n == 0:
        print("Program stopped by the user")
        sys.exit()

    else:
        p = 0
        for i in range(0,n-1):
            s = 0
            for j in range(0,i+2):
                if (i+2)%(j+1) == 0:
                    s += 1
            if s == 2:
                p += 1

        print(p, "of those numbers are primes .\n")
