def Bubblesort(list) :
   for i in range(len(list)) :
      for j in range(0, len(list) - i -1) :
         if list[j] > list[j + 1] :
            list[j], list[j + 1] = list[j + 1], list[j]
   return list

l = [5, 7, 8,4, 3,1, 2,90]

            
   
