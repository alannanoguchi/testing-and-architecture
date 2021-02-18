# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math

def distance_formula(xc1, yc1, xc2, yc2):
    """Calculate the distance between two circles."""
    calc_x_dist = (xc1-xc2)**2
    calc_y_dist = (yc1 - yc2)**2

    distance = math.sqrt(calc_x_dist + calc_y_dist)
    print('distance', distance)


def vector_length(xa, ya, xb, yb):
    """Calculate the length of vector AB vector which is a vector between points A and B."""
    x_length = (xa-xb)*(xa-xb)
    y_length = (ya-yb)*(ya-yb)

    length = math.sqrt(x_length + y_length)
    print('length', length)

distance_formula(4, 4.25, 53, -5.35)
vector_length(-36, 97, .34, .91)
