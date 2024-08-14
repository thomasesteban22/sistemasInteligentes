from Distances.Distance import Distance


class ChevyshevDistance(Distance):
    """
    Class to compute the Chebyshev distance between two points.

    Inherits from the Distance class and overrides the distance computation method
    to use the Chebyshev metric, which is the maximum absolute difference between
    the coordinates of the points.

    Attributes:
        point1 (Point): The first point for distance calculation.
        point2 (Point): The second point for distance calculation.
    """

    def __init__(self, point1, point2):
        """
        Initializes the ChevyshevDistance instance.

        Args:
            point1 (Point): The first point.
            point2 (Point): The second point.
        """
        try:
            super().__init__(point1, point2)
        except TypeError as e:
            raise ValueError("Invalid arguments provided to ChevyshevDistance.") from e
        except Exception as e:
            raise RuntimeError("An unexpected error occurred during initialization.") from e

    def compute_distance(self):
        """
        Computes the Chebyshev distance between the provided points.

        The Chebyshev distance is defined as the maximum absolute difference
        between the corresponding coordinates of the two points.

        Returns:
            float: The Chebyshev distance between point1 and point2.

        Raises:
            ValueError: If the points have different dimensions or contain invalid data.
            TypeError: If the values in the points are not numeric.
            AttributeError: If the points do not have a valid get_values method.
            RuntimeError: For any other unexpected errors.
        """
        try:
            # Extract values from points
            values1 = self.point1.get_values()
            values2 = self.point2.get_values()

            if len(values1) != len(values2):
                raise ValueError("Points must have the same number of dimensions.")

            # Calculate the Chebyshev distance
            distance = max(abs(a - b) for a, b in zip(values1, values2))

            return distance

        except AttributeError as e:
            raise ValueError("Points must have a valid get_values method.") from e
        except TypeError as e:
            raise TypeError("Point values must be numeric.") from e
        except ValueError as e:
            raise ValueError("Error in computing Chebyshev distance: " + str(e)) from e
        except Exception as e:
            raise RuntimeError("An unexpected error occurred while computing the distance.") from e
