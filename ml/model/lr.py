# Linear Regression
import numpy as np

class simple_linear_regression:
  def __init__(self):
    self.output = None
    self.param = None

  def estimate(self, x):
    # xは2次元のnumpy配列を想定
    if self.param is None:
      return "Please do the learning beforehand"
    if x.ndim == 1:
      np.append(x, 1)
      x = x.reshape(1, -1)
    ones = np.ones((x.shape[0], 1))
    x = np.concatenate([ones, x], axis=1)  # bias項を追加
    self.output = x @ self.param
    return self.output

  def learn(self, x, y):
    # xは2次元のnumpy配列, yは1次元のnumpy配列を想定
    if x.ndim == 1:
      x = x.reshape(1, -1)
    ones = np.ones((x.shape[0], 1))
    x = np.concatenate([ones, x], axis=1) # bias項を追加
    self.param = np.linalg.pinv((x.T)@x)@(x.T)@y
    return self.param