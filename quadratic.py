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
import cmath


def create_quadratic_function(a, b, c):
    """Returns the quadratic function as a closure."""
    def quadratic(x):
        return a * x * x  +  b * x  + c
    return quadratic


def find_quadratic_roots(a, b, c):
    """Returns the 2 roots of the quadratic equation
    in a tuple. Each root is a complex
    number as the discriminant may be negative.
    """
    assert (not np.isclose(a, 0.0)),"a cannot be zero."
        
    sq_root_of_discrim = cmath.sqrt(b * b - 4.0 * a * c)
    denom = 2.0 * a
    
    root1 = (-b + sq_root_of_discrim) / denom 
    root2 = (-b - sq_root_of_discrim) / denom 
    
    return (root1, root2)


def find_quadratic_vertex(a, b, c):
    """Returns the values of x and y in a tuple where the
    value of y in the quadratic function y = ax^2+bx+c
    is at a minimum (or maximum if a < 0).
    """
    assert (not np.isclose(a, 0.0)),"a cannot be zero."
    
    vertex_x = -b / (2.0 * a)
    
    f = create_quadratic_function(a, b, c)
    vertex_y = f(vertex_x)
    
    return (vertex_x, vertex_y)
