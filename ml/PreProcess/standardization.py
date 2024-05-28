# Standardization
def standardization(x, flag=False):
  mean = x.mean(axis=0)
  std = x.std(axis=0)
  x = (x-mean)/std
  if flag==False:
    return x
  else:
    return [x, mean, std]

class standard:
  def __init__(self):
    self.mean = None
    self.std = None

  def forward(self, x):
    # xは2次元のnumpy配列を想定
    if self.mean is None or self.std is None:
      data = standardization(x, flag=True)
      self.mean = data[1]
      self.std = data[2]
      return data[0]
    else:
      return (x-self.mean)/self.std

  def reverse(self, x):
    # xは標準化された2次元のnumpy配列を想定
    if self.mean is None or self.std is None:
      return "標準化されていません"
    x = x*self.std + self.mean
    return x