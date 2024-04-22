def select_sort(x):
  if len(x)==1:
    return x
  for i in range(1, len(x)):
    for j in range(0, i):
      if x[i] < x[j]:
        tmp = x[i]
        del x[i]
        x.insert(j, tmp)
        break
  return x

x = list(map(int, list(input())))
print("x")
print(x)
print("")
print("sorted_x")
print(select_sort(x))
