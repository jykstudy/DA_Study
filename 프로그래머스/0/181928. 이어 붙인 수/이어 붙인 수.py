def solution(num_list):
    oddlist=[]
    evenlist=[]
    for i in num_list:
        if i%2!=0:
            oddlist.append(str(i))
        else:
            evenlist.append(str(i))
    odd_str = ''.join(oddlist)
    even_str = ''.join(evenlist)                        
    return int(odd_str)+int(even_str)
    