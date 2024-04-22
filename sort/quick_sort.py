def quick_sort(x, start, end):
  piv = x[start]
  i = start
  j = end
  while True:
    while x[i] < piv:
      i += 1
    while x[j] > piv:
      j -= 1
    if i >= j:
      break
    x[i], x[j] = x[j], x[i]
    i += 1
    j -= 1
  if start < i-1:
    quick_sort(x, start, i-1)
  if end > j+1:
    quick_sort(x, j+1, end)
  return x

x = list(map(int, list(input())))
print("x")
print(x)
print("")
print("sorted_x")
print(quick_sort(x, 0, len(x)-1))
