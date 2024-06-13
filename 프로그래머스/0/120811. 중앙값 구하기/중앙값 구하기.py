def solution(array):
    array=sorted(array)
    mid=len(array)//2
    if len(array)%2==0:
        answer=(array[mid-1]+array[mid])/2
    else:
        answer=array[mid]
    
    return answer