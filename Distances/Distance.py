from abc import ABC, abstractmethod


class Distance(ABC):
    """
    Abstract base class to compute the distance between two points.

    Attributes:
        point1: The first point, which can be of any type that supports
                distance calculation.
        point2: The second point, which can be of any type that supports
                distance calculation.
    """

    def __init__(self, point1, point2):
        """
        Initializes the Distance object with two points.

        Args:
            point1: The first point.
            point2: The second point.
        """
        try:
            self.point1 = point1
            self.point2 = point2
        except Exception as e:
            raise ValueError(
                "Failed to initialize Distance with the given points."
            ) from e

    @abstractmethod
    def compute_distance(self):
        """
        Abstract method to compute the distance between point1 and point2.

        This method must be implemented by subclasses to perform the
        actual distance calculation.

        Returns:
            The distance between point1 and point2.

        Raises:
            NotImplementedError: This method must be implemented by
                                 subclasses.
        """
        try:
            pass  # Subclasses should implement this method
        except NotImplementedError as e:
            raise NotImplementedError(
                "The compute_distance method must be implemented by "
                "subclasses."
            ) from e
        except Exception as e:
            raise RuntimeError(
                "An unexpected error occurred while computing the distance."
            ) from e
