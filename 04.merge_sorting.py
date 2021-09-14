def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2 #버림나눗셈
    left = arr[:mid] # 왼쪽 정렬
    right = arr[mid:] #오른쪽 정렬
    left1=merge_sort(left)
    right1=merge_sort(right) #더 쪼개줌
    return merge(left1,right1)

def merge(left,right):
    a = 0;
    b = 0;
    array = []

    while (a<len(left)) & (b<len(right)):
        if left[a] < right[b]:
            array.append(left[a])
            a+=1
        else:
            array.append(right[b])
            b+=1
    while(a<len(left)):
          array.append(left[a])
          a+=1
    while(b<len(right)):
          array.append(right[b])
          b+=1
    return array

a = list(map(int,input().split()))
print(merge_sort(a))
    