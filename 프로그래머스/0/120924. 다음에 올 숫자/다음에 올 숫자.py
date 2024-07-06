def solution(common):
    if common[1] - common[0] == common[2] - common[1]:
        difference = common[1] - common[0]
        return common[-1] + difference
    elif common[1] / common[0] == common[2] / common[1]:
        ratio = common[1] / common[0]
        return common[-1] * ratio