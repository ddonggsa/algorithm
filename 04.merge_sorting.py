def merge_sort(arr):
    if len(arr)<=1:#만약 배열 길이가 1이하면 그대로 출력
        return arr
    mid = len(arr)//2 #버림나눗셈
    left = arr[:mid] # 왼쪽 정렬
    right = arr[mid:] #오른쪽 정렬
    left1=merge_sort(left)
    right1=merge_sort(right) #더 쪼개줌->재귀함수
    return merge(left1,right1)

def merge(left,right):
    a = 0;
    b = 0;
    array = []#새로운 리스트 형성

    while (a<len(left)) and (b<len(right)):#왼쪽 오른쪽 배열이 하나도 남지않을때까지 반복
        if left[a] < right[b]:#만약 왼쪽 배열의 a번째 배열보다 오른쪽 b번째 배열이 클 경우 왼쪽 배열이 그대로 왼쪽에 존재해야함
            array.append(left[a])#그래서 빈 array리스트에  left[a]를 붙여준다.
            a+=1 #a크기를 늘리면서 크기비교 
        else:#만약 왼쪽 배열의 a배열보다 오른쪽 b번째 배열이 작을 경우 오른쪽 배열이 왼쪽으로 와야함
            array.append(right[b])#그래서 빈  array리스트에 right[b]를 붙여준다.
            b+=1 #b크기를 늘리면서 크기비교
    while(a<len(left)):
          array.append(left[a])
          a+=1
    while(b<len(right)):
          array.append(right[b])
          b+=1
    return array

a = list(map(int,input().split()))
print(merge_sort(a))
    