import math

def calculate_distance(point1, point2):
    """
    Calculate the Euclidean distance between two points.

    Args:
        point1 (tuple): (x1, y1)
        point2 (tuple): (x2, y2)

    Returns:
        float: Distance between the two points
    """
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_angle(vector1, vector2):
    """
    Calculate the angle between two vectors.

    Args:
        vector1 (tuple): (x1, y1)
        vector2 (tuple): (x2, y2)

    Returns:
        float: Angle between the two vectors in radians
    """
    x1, y1 = vector1
    x2, y2 = vector2
    dot_product = x1 * x2 + y1 * y2
    magnitude1 = math.sqrt(x1 ** 2 + y1 ** 2)
    magnitude2 = math.sqrt(x2 ** 2 + y2 ** 2)
    return math.acos(dot_product / (magnitude1 * magnitude2))

def calculate_matrix_determinant(matrix):
    """
    Calculate the determinant of a 2x2 matrix.

    Args:
        matrix (list): [[a, b], [c, d]]

    Returns:
        float: Determinant of the matrix
    """
    a, b = matrix[0]
    c, d = matrix[1]
    return a * d - b * c

def calculate_vector_magnitude(vector):
    """
    Calculate the magnitude of a vector.

    Args:
        vector (tuple): (x, y)

    Returns:
        float: Magnitude of the vector
    """
    x, y = vector
    return math.sqrt(x ** 2 + y ** 2)
