def solution(num_list):
    mul_num=1
    sum_num=0
    for i in num_list:
        mul_num*=i
        sum_num+=i
        
    if mul_num<sum_num**2:
        return 1
    else:
        return 0