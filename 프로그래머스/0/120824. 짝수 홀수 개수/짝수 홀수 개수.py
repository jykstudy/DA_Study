def solution(num_list):
    answer = []
    odd=[]
    even=[]
    for i in num_list:
        if i%2!=0:
            odd.append(i)
        if i%2==0:
            even.append(i)
    answer.append(len(even))
    answer.append(len(odd))
    return answer