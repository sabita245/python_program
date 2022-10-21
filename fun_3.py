#recursive fun to calculate sum of 0 to 10. o/p:55
def recursive(n):
    if n:
        return n+recursive(n-1)
    else:
        return 0
    # sum=0
    # for i in range(n+1):
    #     sum=sum+i
    # return sum
print(recursive(10))
