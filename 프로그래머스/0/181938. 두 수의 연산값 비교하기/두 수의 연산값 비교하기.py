def solution(a, b):
    ans1=int(f'{a}{b}')
    ans2=2*a*b
    if ans1>=ans2:
        return ans1
    else:
        return ans2