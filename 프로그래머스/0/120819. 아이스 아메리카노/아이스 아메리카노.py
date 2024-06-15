def solution(money):
    answer = []
    num=money//5500
    answer.append(num)
    left=money%5500
    answer.append(left)
    return answer