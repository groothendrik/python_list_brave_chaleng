#Combine Sort

def combine_sort(lst1, lst2):
  combined_list = lst1 + lst2
  sorted_list = sorted(combined_list)
  return sorted_list

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))