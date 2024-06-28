def solution(arr, flag):
    X = []
    for i in range(len(arr)):
        if flag[i]:
            X.extend([arr[i]]*(arr[i]*2))
        else:
            if arr[i] <= len(X):
                    X = X[:-arr[i]]
            else:
                    X = []
    return X