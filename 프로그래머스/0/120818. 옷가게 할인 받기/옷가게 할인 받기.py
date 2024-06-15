def solution(price):
    if price<100000:
        answer=price
    elif price<300000:
        answer=int(0.95*price)
    elif price<500000:
        answer=int(0.9*price)
    elif price>=500000:
        answer=int(0.8*price)
    return answer