def solution(order):
    total=0
    for i in order:
        if 'americano' in i or i == 'anything':
            total += 4500
        elif 'cafelatte' in i:
            total += 5000
    return total