data = list(map(int,input().split()))
isSort = False # 정렬이 완료되었나 기억하는 변수, True로 변경되면 정렬이 완료됨을 의미한다.
radix = 1      # 큐에 넣어줄 자리수의 위치를 기억하는 변수, 1 => 10 => 100 => 1000

# 정렬이 완료될 때 까지 반복한다.
while not isSort:
    isSort = True
    # 정렬할 숫자의 기수(진법)의 크기만큼 큐로 사용할 리스트를 만든다.
    queueList = [[] for i in range(10)]
    print('radix: {}'.format(radix))
    
    # 정렬할 데이터의 개수만큼 반복하며 데이터를 큐에 넣어준다.
    for n in data:
        # 큐에 넣어줄 자리수에 해당되는 숫자만 뽑아낸다.
        digit = n // radix % 10
        # 큐에 숫자를 넣어준다.
        queueList[digit].append(n)
        # 정렬 작업이 완료되었나 검사한다.
        if isSort and digit > 0:
            isSort = False    
    # 큐에 저장된 데이터를 0번 큐의 데이터부터 차례대로 꺼내서 data 리스트에 다시 저장한다.
    index = 0
    # queueList에 저장된 0번 큐를 numbers 리스트에 저장한 다음 반복을 시작해서 9번 큐를 numbers 리스트에 저장한 후 반복한 다음 종료한다.
    for numbers in queueList:
        # 각각의 큐에 해당되는 리스트에 저장된 데이터 개수만큼 반복하며 data 리스트를 수정한다.
        for number in numbers:
            data[index] = number
            index += 1
    print(data)    
    # 다음 자리수를 큐에 넣기 위해서 radix에 저장된 숫자에 10을 곱한다.
    radix *= 10

