def solution(strArr):
    result = []
    for index, value in enumerate(strArr):
        if index % 2 == 0:
            result.append(value.lower())
        else:
            result.append(value.upper())
    return result