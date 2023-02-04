n=int(input())
for i in range (1,n+1):
    for j in range(n-i+1):  #for j in range(i,n):
        print("*",end="")
    print()
#1 Decreasing triangle
n=int(input())
for i in range (n):
    for j in range(n):
        print("*",end="")
    print()
#2 square
n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print()
#3 Increasing Triangle
n=int(input())
for i in range(n):
    for j in range(i+1):
        print(" ", end="")
    for k in range(i,n):
        print("*",end="")
    print()
#4 Right side triangle vise versa =>chnage for loop
n=int(input())
for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")
    for k in range(i,n):
        print("*",end=" ")
    for h in range(i,n-1): # odd increasing pattern for even don;t do n simply print("* ",)
        print("*", end=" ")
    print()
#5 reverse pyramid
n=int(input())
for i in range(n):
    for j in range(i,n):
        print(" ", end=" ")
    for k in range(i):
        print("*",end=" ")
    for h in range(i+1): # odd increasing pattern for even
        print("*", end=" ")
    print()
#6 pyramid or hill pattern
n=int(input())
for i in range(n-1):
    for j in range(i,n):
        print(" ", end=" ")
    for k in range(i+1):
        print("*",end=" ")
    for h in range(i): # odd increasing pattern for even
        print("*", end=" ")
    print()
for i in range(n):
    for j in range (i+1):
        print(" ",end=' ')
    for k in range(i,n):
        print("*",end=' ')
    for h in range(i,n-1):
        print("*",end=' ')
    print()
#7 pattern for diamond


