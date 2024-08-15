from Distances.Distance import Distance


class EuclideanDistance(Distance):
    """
    Class to compute the Euclidean distance between two points.

    Inherits from the Distance class and overrides the distance
    computation method to use the Euclidean metric, which is the
    square root of the sum of the squared differences between the
    coordinates of the points.

    Attributes:
        point1 (Point): The first point for distance calculation.
        point2 (Point): The second point for distance calculation.
    """

    def __init__(self, point1, point2):
        """
        Initializes the EuclideanDistance instance.

        Args:
            point1 (Point): The first point.
            point2 (Point): The second point.
        """
        try:
            super().__init__(point1, point2)
        except TypeError as e:
            raise ValueError(
                "Invalid arguments provided to EuclideanDistance."
            ) from e

    def compute_distance(self):
        """
        Computes the Euclidean distance between the provided points.

        The Euclidean distance is defined as the square root of the
        sum of the squared differences between the corresponding
        coordinates of the two points.

        Returns:
            float: The Euclidean distance between point1 and point2.

        Raises:
            ValueError: If the points are not of the same dimension or
                        contain invalid data.
            TypeError: If the values in the points are not numeric.
        """
        try:
            # Extract values from points
            values1 = self.point1.get_values()
            values2 = self.point2.get_values()

            if len(values1) != len(values2):
                raise ValueError(
                    "Points must have the same number of dimensions."
                )

            # Calculate the Euclidean distance
            distance = sum(
                (a - b) ** 2 for a, b in zip(values1, values2)
            ) ** 0.5

            return distance

        except AttributeError as e:
            raise ValueError(
                "Points must have valid get_values method."
            ) from e
        except TypeError as e:
            raise TypeError(
                "Point values must be numeric."
            ) from e
        except ValueError as e:
            raise ValueError(
                "Error in computing Euclidean distance: " + str(e)
            ) from e
        except Exception as e:
            raise RuntimeError(
                "An unexpected error occurred while computing distance."
            ) from e
