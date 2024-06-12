#def solution(numer1, denom1, numer2, denom2):
 #   up=numer1*denom2+numer2*denom1
  #  down=denom1*denom2
   # answer=[]
    #return answer
    
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def solution(numer1, denom1, numer2, denom2):
    # 두 분수의 분모의 최소공배수를 구함
    lcm_denom = lcm(denom1, denom2)
    
    # 각 분수의 분자에 대응하는 분모의 비율을 유지하기 위해 곱셈 수행
    numer1 *= lcm_denom // denom1
    numer2 *= lcm_denom // denom2
    
    # 두 분수의 분자를 더함
    sum_numer = numer1 + numer2
    
    # 최대공약수를 이용하여 기약분수로 만듦
    gcd_val = gcd(sum_numer, lcm_denom)
    
    # 기약분수로 만든 후 반환
    return [sum_numer // gcd_val, lcm_denom // gcd_val]
