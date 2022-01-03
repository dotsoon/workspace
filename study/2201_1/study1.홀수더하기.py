t = int(input())
 
for test_case in range(1,t+1):
    li = map(int, input().split())  # 모든 숫자들을 리스트에 저장
    answer = 0                      # 합을 구하기 위 한 변수
    for i in li:                    # 입력받은 숫자들을 한개씩 비교
        if i%2!=0:                  #2로 나누어떨어지지않으면 홀수, answer변수에 더해주기
            answer += i
    print("#"+str(test_case),str(answer))