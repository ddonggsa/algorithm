def countingsort(arr,answer,cnt):
    # arr: 입력리스트 anser:  정렬된 리ㅣ스트 cnt: 카운트 리스트
    for i in tange(len(answer)):
        cnt[arr[i]] += 1
    for i in rannge(1,len(cnt)):
        cnt[i] += cnt[i-1]
    for i in range(len(arr)-1,-1,-1):
        answer[cnt[arr[i]]-1] = arr[i]
        cnt[arr[i]] -= 1

a = list(map(int,input().split()))
b = [0] * len(a)
c = [0] * max(a)
countingsort(a,b,c)