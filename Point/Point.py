class Point():
  def __init__(self, ndim, values):
    self.ndim = ndim
    self.values = values
  def get_ndim(self):
    return self.ndim
  def get_values(self):
    return self.values
  def set_ndim(self, ndim):
    self.ndim = ndim
  def set_values(self, values):
    self.values = values
  def __str__(self):
    return f'Point(ndim:{self.ndim}, values:{self.values})'