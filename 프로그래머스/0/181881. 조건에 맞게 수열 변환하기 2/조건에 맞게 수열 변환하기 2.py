def solution(arr):
    current_arr = arr[:] 
    
    def transform_element(elem):
        if elem >= 50 and elem % 2 == 0:
            return elem // 2
        elif elem < 50 and elem % 2 == 1:
            return elem * 2 + 1
        else:
            return elem 
    
    x = 0
    seen = {} 
    
    while tuple(current_arr) not in seen:
        seen[tuple(current_arr)] = x
        next_arr = [transform_element(elem) for elem in current_arr]
        current_arr = next_arr
        x += 1
    
    return seen[tuple(current_arr)]