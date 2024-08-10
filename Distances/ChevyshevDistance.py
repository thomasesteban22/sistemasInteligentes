from Distances.Distance import Distance


class ChevyshevDistance(Distance):
  def __init__(self, point1, point2):
    super().__init__(point1, point2)
  def compute_distance(self):
    return max(abs(a - b) for a, b in zip(self.point1.get_values(), self.point2.get_values()))