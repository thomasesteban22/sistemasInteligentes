from abc import ABC, abstractmethod
class Distance(ABC):
  def __init__(self, point1, point2):
    self.point1 = point1
    self.point2 = point2
  @abstractmethod
  def compute_distance(self):
    pass