#bubblw_sorting
a = list(map(int,input().split()))
for i in range(len(a)-1):
    for j in range(len(a)-1-i):
        if a[j]<a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
print(a)

#bubble_sorting_ing
a = list(map(int,input().split()))
for i in range(len(a)-1):
    print(a)
    for j in range(len(a)-1-i):
        if a[j]<a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
