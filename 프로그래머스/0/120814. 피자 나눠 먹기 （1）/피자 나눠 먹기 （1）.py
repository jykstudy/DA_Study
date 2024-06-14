def solution(n):
    if n//7==0:
        answer=1
    elif n//7>0 and n%7!=0:
        answer=(n//7)+1
    elif n//7>0 and n%7==0:
        answer=n//7
    return answer