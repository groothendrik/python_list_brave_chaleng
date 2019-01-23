#Every Three Nums

def every_three_nums(start):
  return list(range(start, 101, 3))
  if start > 100:
    return []
print(every_three_nums(91))