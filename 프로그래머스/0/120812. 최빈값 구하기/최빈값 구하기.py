def solution(array):
    frequency_dict = {}
    
    for num in array:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1
    
    max_freq = 0
    modes = []
    
    for key, value in frequency_dict.items():
        if value > max_freq:
            max_freq = value
            modes = [key]
        elif value == max_freq:
            modes.append(key)

    if len(modes) > 1:
        return -1
    else:
        return modes[0]