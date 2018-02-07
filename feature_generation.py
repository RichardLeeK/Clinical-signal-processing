import scipy.stats as stat
import numpy as np

def from_oa_date():
  return datetime(1899, 12, 30, 0, 0, 0, tzinfo=pytz.utc) + timedelta(days=v)

# Basic statistics
def mean(iter, mode='ari'):
  # iter: iteration
  # mode: ari (arithmetic mean), har (harmonic mean), geo (geometric mean)
  if mode == 'ari':
    return float(sum(iter)) / float(len(iter))
  elif mode == 'har':
    return stat.hmean(iter)
  elif mode == 'geo':
    return stat.gmean(iter)
  else:
    return 0

def standard_deviation(iter):
  return np.std(iter)

def variance(iter):
  return np.var(iter)

def skewness(iter):
  return stat.skew(iter)

def kurtosis(iter):
  return stat.kurtosis(iter)

def s_t_n(iter):
  return stat.signaltonoise(iter)

def range_time(x_iter):
  return (from_oa_date(x_iter[-1]) - from_oa_date(x_iter[0])).total_seconds 

# Curve fitting parameters
def poly_fit(x_iter, y_iter, dim):
  z = np.polyfit(x_iter, y_iter, dim)
  return z

# Histogram
def gen_histogram(y_iter):
  interval = int(round(len(y_iter) / np.log2(len(y_iter) + 1)))
  histogram = []
  for i in range(0, int(len(y_iter) / interval)):
    bin = []
    for j in range(0, interval):
      if j + i * interval == len(y_iter): break
      bin.append(y_iter[j + i * interval])
    histogram.append(mean(bin, 'ari'))
  return histogram

# Percentile
def percentile(y_iter):
  return [np.percentile(y_iter, 25), np.percentile(y_iter, 50), np.percentile(y_iter, 75), np.percentile(y_iter, 75) - np.percentile(y_iter, 25)]

# Auto-correlation
def correlation(x_iter, y_iter, mode):
  if mode == 'aut':
    return np.correlate(x_iter, y_iter, mode='full') / np.sum(np.array(x_iter) ** 2)
  elif mode == 'pea':
    return stat.pearsonr(x_iter, y_iter)[0]
  elif mode == 'spe':
    return stat.spearmanr(x_iter, y_iter).correlation
  elif mode == 'ken':
    return stat.kendalltau(x_iter, y_iter).correlation
  else:
    return 0

# Inter-correlation
def gen_feature(x_iter, y_iter):
  feature = []
  mean_feature = [mean(y_iter, 'ari'), mean(y_iter, 'har'), mean(y_iter, 'geo')]
  stat_feature = [standard_deviation(y_iter), skewness(y_iter), kurtosis(y_iter), s_t_n(y_iter), ]