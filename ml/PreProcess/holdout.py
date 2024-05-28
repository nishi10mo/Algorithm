# holdout
import random
import numpy as np

def holdout(x, y, ratio, seed):
  # xは2次元のnumpy配列, yは1次元のnumpy配列を想定
  # ratioはトレーニングデータの割合
  y = y.reshape(-1, 1)
  data = np.concatenate([x, y], axis=1)
  n = data.shape[0]
  random.seed(seed)
  all = list(range(0, n))
  train = random.sample(all, k=math.floor(n*ratio))
  test = list(set(all) - set(train))
  train_data = data[train]
  test_data = data[test]
  train_x = train_data[:, 0:-1]
  train_y = train_data[:, -1]
  test_x = test_data[:, 0:-1]
  test_y = test_data[:, -1]
  return [train_x, train_y, test_x, test_y]
