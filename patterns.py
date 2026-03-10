def right_angle_numbers(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
n=int(input())
right_angle_numbers(n)
def inverted_triangle(n):
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print(j,end=" ")
        print()
inverted_triangle(n)
def floyds_triangle(n):
    num=1
    for i in range(1,n+1):
        for j in range(i):
            print(num,end=" ")
            num+=1
        print()
floyds_triangle(n)
def diamond_numbers(n):
    for i in range(1,n+1):
        print(" "*(n-i),end='')
        for j in range(1,i+1):
            print(j,end=" ")
        print()
    for i in range(n,0,-1):
        print(" "*(n-i),end='')
        for j in range(1,i+1):
            print(j,end=" ")
        print()
def diamond(n):
    for i in range(1,n+1):
        print(" "*(n-i)+"* "*i)
    for i in range(n,0,-1):
        print(" "*(n-i)+"* "*i)
diamond_numbers(n)
def hour_glass_numbers(n):
    for i in range(n,0,-1):
        print(" "*(n-i),end='')
        for j in range(1,i+1):
            print(j,end=" ")
        print()   
    for i in range(1,n+1):
        print(" "*(n-i),end='')
        for j in range(1,i+1):
            print(j,end=" ")
        print()
def pyramid(n):
    for i in range(1,n+1):
        print(" "*(n-i),end='')
        for j in range(1,i+1):
            print(j,end=" ")
        print()
pyramid(n)
def hour_glass(n):
    for i in range(n,0,-1):
        print(" "*(n-i)+"* "*i)
    for i in range(1,n+1):
        print(" "*(n-i)+"* "*i)
hour_glass(n)
def pascal_triangle(n):
    def fact(n):
        return 1 if n==0 else n*fact(n-1)
    for i in range(n):
        '''for j in range(n-i-1):
            print(" ",end=" ")'''
        for j in range(i+1):
            print(fact(i)//(fact(j)*fact(i-j)),end=" ")
        print()
hour_glass_numbers(n)
pascal_triangle(n)
def hollow_square(n):
    n = 5
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
def hollow_triangle(n):
    n = 5
    for i in range(1,n+1):
        for j in range(1,i+1):
            if i == 0 or j == 1 or i == n or j==i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
hollow_triangle(n)
def hollow_pyramid(n):
    for i in range(1, n + 1):
    # Print spaces
        for j in range(n - i):
            print(" ", end=" ")

    # Print stars and spaces inside
        for j in range(2 * i - 1):
            if j == 0 or j == 2 * i - 2 or i == n:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
hollow_pyramid(n)
hollow_square(n)
diamond(n)
def hollow_diamond(n):
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        for j in range(1, i + 1):
            if j == 1 or j == i :
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    for i in range(n - 1, 0, -1):
        print(" " * (n - i), end="")
        for j in range(1, i + 1):
            if j == 1 or j == i or i == 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
hollow_diamond(n)
