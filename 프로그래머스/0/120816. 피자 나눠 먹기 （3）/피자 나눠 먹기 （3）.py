def solution(slice, n):
    if n//slice==0:
        answer=1
    if n//slice>0 and n%slice==0:
        answer=n//slice
    if n//slice>0 and n%slice!=0:
        answer=(n//slice)+1
    return answer