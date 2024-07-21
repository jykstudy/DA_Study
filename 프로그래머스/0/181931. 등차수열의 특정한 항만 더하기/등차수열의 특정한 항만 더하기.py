def solution(a, d, included):
    total_sum = 0
    
    for i in range(len(included)):
        if included[i]:
            total_sum += a + i * d  # 등차수열의 i+1번째 항을 계산하여 더함
    
    return total_sum