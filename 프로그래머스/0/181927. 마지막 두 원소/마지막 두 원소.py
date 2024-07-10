def solution(num_list):
    if num_list[-1]>num_list[-2]:
        nextnum = num_list[-1] - num_list[-2]
        num_list.append(nextnum)
    else:
        nextnum = num_list[-1]*2
        num_list.append(nextnum)
    return num_list