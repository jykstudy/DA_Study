#def solution(str1, str2):
 #   unique_str1=''.join(set(str1))
 #   unique_str2=''.join(set(str2))
 #   answer = (unique_str1+unique_str2)*len(str1)
 #   return answer
#''.join(set(str1)): set() - 고유 문자 추출
def solution(str1, str2):
    answer=[]
    for i in range(len(str1)):
            answer.append(str1[i])
            answer.append(str2[i])
    return ''.join(answer)