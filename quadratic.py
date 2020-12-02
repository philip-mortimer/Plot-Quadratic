"""
    Copyright 2019 Philip Mortimer
    
    This file is part of Philip Mortimer Example Programs.

    Philip Mortimer Example Programs is free software: you can redistribute it 
    and/or modify it under the terms of the GNU General Public License as 
    published by the Free Software Foundation, either version 3 of the License,
    or (at your option) any later version.

    Philip Mortimer Example Programs is distributed in the hope that it will be
    useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Philip Mortimer Example Programs.  If not, see 
    <https://www.gnu.org/licenses/>.
"""


import numpy as np
import math
import cmath

from XInterceptSet import XInterceptSet
from XInterceptSet import QuadraticRootSet,QuadraticRoot,QuadraticRoots
from XInterceptSet import LinearXIntercept,NoXInterceptBecauseConst
from Point2D import Point2D


def create_quadratic_function(a, b, c):
    """Returns the quadratic function as a closure."""
    def quadratic(x):
        return a*(x**2.0) + b*x + c
    return quadratic


def find_quadratic_roots(a, b, c) -> QuadraticRootSet:
    """
    Returns the roots of the quadratic equation ax^2+bx+c=0. The roots are
    complex if the discriminant b^2-4ac is negative.
    """
    assert (not np.isclose(a, 0.0)),"a cannot be zero."
        
    denom = 2.0 * a
    discrim = b**2.0 - 4.0*a*c
    if np.isclose(discrim, 0.0):
        # There is only 1 root.
        root = -b / denom
        return QuadraticRoot(root)

    if discrim < 0.0:
        sq_root_of_discrim = cmath.sqrt(discrim)
    else:
        sq_root_of_discrim = math.sqrt(discrim)
    
    root1 = (-b + sq_root_of_discrim) / denom 
    root2 = (-b - sq_root_of_discrim) / denom 
    
    return QuadraticRoots(root1, root2)


def find_x_intercepts(a, b, c) -> XInterceptSet:
    """
    Returns the roots of the quadratic equation ax^2+bx+c=0 if a <> 0,
    otherwise it returns the x intercept of bx+c=0, or instance of
    NoXInterceptBecauseConst if b is zero.
    """
    if np.isclose(a, 0.0):
        if np.isclose(b, 0.0):
            # a and b are both zero so the quadratic function has a constant
            # value and there is no x intercept.
            return NoXInterceptBecauseConst()
        else:
            return LinearXIntercept(-c/b)
    else:
        return find_quadratic_roots(a, b, c)


def find_quadratic_vertex(a, b, c) -> Point2D:
    """
    Returns x,y where the value of y in the quadratic function y = ax^2+bx+c
    is at a minimum (or maximum if a < 0).
    """
    assert (not np.isclose(a, 0.0)),"a cannot be zero."
    
    vertex_x = -b / (2.0*a)
    
    f = create_quadratic_function(a, b, c)
    vertex_y = f(vertex_x)
    
    return Point2D(vertex_x, vertex_y)
