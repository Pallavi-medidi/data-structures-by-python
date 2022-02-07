def Mergesort(li) :
  if len(li) <= 1 :
    return li
  middle = len(li) // 2
  left_list = li[:middle]
  right_list = li[middle:]
  left_list = Mergesort(left_list)
  right_list = Mergesort(right_list)
  return list(Merge(left_list, right_list))


def Merge(left_half, right_half) :
  result = []
  while len(left_half) != 0 and len(right_half) != 0 :
    if left_half[0] < right_half[0] :
      result.append(left_half[0])
      left_half.remove(left_half[0])
    else :
      result.append(right_half[0])
      right_half.remove(right_half[0])
  if len(left_half) == 0 :
    result += right_half
  else :
    result += left_half
  return result

l = [4, 5, 6, 1, 90, 23, 1]
print(Mergesort(l))
