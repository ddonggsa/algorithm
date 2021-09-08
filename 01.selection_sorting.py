#select_sorting
a = list(map(int,input().split()))
for i in range(0,len(a)-1):
    max_idx = i
    for j in range(i+1,len(a)):
      if a[j]>a[max_idx]:
          max_idx = j
    a[i],a[max_idx] = a[max_idx],a[i]
print(a)
#select_sorting_ing(과정을 보여줌)
a = list(map(int,input().split()))
for i in range(len(a)):
    print(a)
    max_idx = i
    for j in range(i,len(a)):
      if a[j]>a[max_idx]:
          max_idx = j
    a[i],a[max_idx] = a[max_idx],a[i]

  
