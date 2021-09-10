#insertion sorting
a = list(map(int,input().split()))
for i in range(1,len(a)):
    for j in range(i,0,-1):
        if a[j-1]>a[j]:
            a[j],a[j-1]=a[j-1],a[j]
        else:
            break

print(a)

#insertion sorting ing
a = list(map(int,input().split()))
for i in range(1,len(a)):
    print(a)
    for j in range(i,0,-1):
        if a[j-1]>a[j]:
            a[j],a[j-1]=a[j-1],a[j]
        else:
            break


