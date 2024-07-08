def solution(num_list):
    sum_odd = sum(num_list[0::2])
    sum_even = sum(num_list[1::2])
    if sum_odd>=sum_even:
        return sum_odd
    elif sum_even>sum_odd:
        return sum_even