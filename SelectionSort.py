def SelectionSort(lst, n) :
    for i in range(n) :
        mi = i
        for j in range(i, n) :
            if lst[mi] > lst[j] :
                lst[mi], lst[j] = lst[j], lst[mi]
    return lst
    
print(SelectionSort([2,3,4,5,1], 5))
                
            
