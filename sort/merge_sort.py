def merge_sort(x):
  n = len(x)
  if n<=1:
    return x
  left = merge_sort(x[:n//2])
  right = merge_sort(x[n//2:])
  i = 0
  j = 0
  ans = []
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      ans.append(left[i])
      i += 1
    else:
      ans.append(right[j])
      j += 1
  if i < len(left):
    ans += left[i:]
  if j < len(right):
    ans += right[j:]
  return ans

x = list(map(int, list(input())))
print("x")
print(x)
print("")
print("sorted_x")
print(merge_sort(x))
