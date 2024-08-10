from Distances.Distance import Distance


class EuclideanDistance(Distance):
  def __init__(self, point1, point2):
    super().__init__(point1, point2)
  def compute_distance(self):
    return sum((a - b) ** 2 for a, b in zip(self.point1.get_values(), self.point2.get_values())) ** 0.5