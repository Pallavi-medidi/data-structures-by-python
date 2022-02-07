def Bubblesort(list) :
   for i in range(len(list)-1, 0, -1) :
      for j in range(i) :
         if list[j] > list[j + 1] :
            temp = list[j]
            list[j] = list[j + 1]
            list[j + 1] = temp
   return list

l = [5, 7, 8,4, 3,1, 2,90]
print(Bubblesort(l))

            
   
