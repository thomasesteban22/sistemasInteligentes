class Point:
    """
    Represents a point in an n-dimensional space.

    Attributes:
        ndim (int): The number of dimensions of the point.
        values (list or tuple): The coordinates of the point in each dimension.
    """

    def __init__(self, ndim, values):
        """
        Initializes a Point instance.

        Args:
            ndim (int): The number of dimensions of the point.
            values (list or tuple): The coordinates of the point in each dimension.
        """
        try:
            if not isinstance(ndim, int) or ndim <= 0:
                raise ValueError("Number of dimensions must be a positive integer.")
            if not (isinstance(values, list) or isinstance(values, tuple)):
                raise TypeError("Values must be provided as a list or tuple.")
            if len(values) != ndim:
                raise ValueError("The length of values must match the number of dimensions.")

            self.ndim = ndim
            self.values = values

        except TypeError as e:
            raise ValueError("Invalid type provided during initialization.") from e
        except ValueError as e:
            raise ValueError("Invalid value provided during initialization.") from e
        except Exception as e:
            raise RuntimeError("An unexpected error occurred during initialization.") from e

    def get_ndim(self):
        """
        Returns the number of dimensions of the point.

        Returns:
            int: The number of dimensions.
        """
        return self.ndim

    def get_values(self):
        """
        Returns the coordinates of the point.

        Returns:
            list or tuple: The coordinates of the point in each dimension.
        """
        return self.values

    def set_ndim(self, ndim):
        """
        Sets the number of dimensions of the point.

        Args:
            ndim (int): The new number of dimensions for the point.
        """
        try:
            if not isinstance(ndim, int) or ndim <= 0:
                raise ValueError("Number of dimensions must be a positive integer.")

            self.ndim = ndim

        except ValueError as e:
            raise ValueError("Invalid value provided for number of dimensions.") from e
        except Exception as e:
            raise RuntimeError("An unexpected error occurred while setting the number of dimensions.") from e

    def set_values(self, values):
        """
        Sets the coordinates of the point.

        Args:
            values (list or tuple): The new coordinates of the point.
        """
        try:
            if not (isinstance(values, list) or isinstance(values, tuple)):
                raise TypeError("Values must be provided as a list or tuple.")
            if len(values) != self.ndim:
                raise ValueError("The length of values must match the number of dimensions.")

            self.values = values

        except TypeError as e:
            raise TypeError("Invalid type provided for coordinates.") from e
        except ValueError as e:
            raise ValueError("Invalid value provided for coordinates.") from e
        except Exception as e:
            raise RuntimeError("An unexpected error occurred while setting the coordinates.") from e

    def __str__(self):
        """
        Returns a string representation of the Point instance.

        Returns:
            str: A string that represents the Point instance in the format 'Point(ndim:{ndim}, values:{values})'.
        """
        return f'Point(ndim:{self.ndim}, values:{self.values})'
