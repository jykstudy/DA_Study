def solution(my_string, n):
    answer=[]
    for i in my_string:    
        put=i*n
        answer.append(put)
    return ''.join(answer)