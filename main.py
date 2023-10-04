"""Module calculates graduses of ball that has gone some distance."""

import math


def degree(time: float, acceleration: float, radius: float, v_start: float = 0) -> float:
    """Calculate ball's degree between its start position.

    Args:
        time (float): the time that spent the ball.
        acceleration (float): ball's acceleration.
        radius (float): ball's radius, can't be a zero.
        v_start: ball's start position.

    Returns:
        graduses between ball's start position, it is rounded for 2.

    Raises:
        Exception - radius equal or less zero.
    """
    if radius == 0:
        raise Exception("Ball's radius can't be a zero")

    ball_graduses = 360

    ball_width = 2 * math.pi * radius
    distance = v_start * time + (acceleration * time**2) / 2
    between = distance % ball_width

    return round(between / ball_width * ball_graduses, 2)
