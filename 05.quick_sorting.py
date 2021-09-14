def quick_sorting(arr):
  if len(arr)<=1:
      return arr
  pivot = arr[0] # 첫번째 값을 피봇으로 지정
  small = []
  big = []

  for i in range(1,len(arr)):# 첫번째 값제외하고 마지막 값까지 반복
      if arr[i]<pivot:
          small.append(arr[i])
      else:
          big.append(arr[i])

  return quick_sorting(small) +[pivot] + quick_sorting(big)# 재귀함수로 제일 작은수, 큰수 솎아내기

a = list(map(int,input().split()))
print(quick_sorting(a))
