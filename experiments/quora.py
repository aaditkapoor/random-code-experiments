from collections import deque




"""
    Idea is to form a circular array. In other words iterate until one cycle is
    reached. This eliminates the constrait problem.
"""
def indexes(arr,k):
    d = deque(arr)
    indexes = []
    copy=arr.copy()
    while d:
        if len(arr[k-1::k]) == 0:
            #print("empty")
            pass
        else:
            print(arr[k-1::k])
            for index in arr[k-1::k]:
                indexes.append(copy.index(index))
        arr.append(d.popleft())
        if len(d) == 0:
            
            break
    #print(d)
    #print(arr)

    # set to remove duplicate indexes
    return (list((set(indexes))))
        
