README for Distance Calculation Program

Overview

This program provides a framework to calculate various types of distances between points in an n-dimensional space. The distances supported are Euclidean, Manhattan, and Chebyshev. The main components of the program are:

Point: Represents a point in an n-dimensional space.
Distance: An abstract base class for distance calculations.
EuclideanDistance: Computes the Euclidean distance between two points.
ManhattanDistance: Computes the Manhattan distance between two points.
ChebyshevDistance: Computes the Chebyshev distance between two points.

Components:

Point Class
The Point class represents a point in an n-dimensional space and provides methods to get and set its properties.

EuclideanDistance Class
The EuclideanDistance class computes the Euclidean distance between two points.

ManhattanDistance Class
The ManhattanDistance class computes the Manhattan distance between two points.

ChebyshevDistance Class
The ChebyshevDistance class computes the Chebyshev distance between two points.

Error Handling
Each class and method includes error handling to manage potential issues, such as:

Type and value errors during initialization.
Attribute errors if required methods are missing.
Unexpected runtime errors.
