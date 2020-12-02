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


import sys

from quadratic import create_quadratic_function, find_x_intercepts
from quadratic import find_quadratic_vertex
from QuadraticFunctionStrings import QuadraticFunctionStrings
from XInterceptSet import XInterceptSet,QuadraticRootSet
from Point2D import Point2D

NO_VERTEX_STR = "has no quadratic vertex because not quadratic"


def print_quadratic_root_set(root_set: QuadraticRootSet, dest=sys.stdout):
    if root_set.num_intercepts == 2:
        print("roots (x values where y=0): {}".format(root_set), file=dest)
    else:
        print("root (x value where y=0): {}".format(root_set), file=dest)


class QuadraticCoeffs:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    @property
    def c(self):
        return self.__c

    @property
    def abc(self):
        return (self.a, self.b, self.c)
    
    def __str__(self):
        a,b,c = self.abc
        return "a={:g},b={:g},c={:g}".format(a, b, c)


class QuadraticInfo:
    """
    Contains information relating to the quadratic function ax^2+bx+c such as 
    the coefficients a,b and c, and the x intercepts.
    """
    def __init__(self, a, b, c):
        self.__coeffs = QuadraticCoeffs(a, b, c)
        self.__function_strings = QuadraticFunctionStrings(a, b, c)
        self.__x_intercept_set = find_x_intercepts(a, b, c)

        if self.__x_intercept_set.is_quadratic():
            self.__vertex = find_quadratic_vertex(a, b, c)
        else:
            self.__vertex = None

    @property
    def coeffs(self) -> QuadraticCoeffs:
        return self.__coeffs
    
    @property
    def function_strings(self) -> QuadraticFunctionStrings:
        """String representations of the quadratic functions."""
        return self.__function_strings
    
    @property
    def x_intercept_set(self) -> XInterceptSet:
        return self.__x_intercept_set
    
    @property
    def vertex(self) -> Point2D:
        """x,y point where y is at a minimum or maximum"""
        assert (self.__vertex is not None),NO_VERTEX_STR
        return self.__vertex
    
    def create_quadratic_function(self):
        a,b,c = self.coeffs.abc
        return create_quadratic_function(a,b,c)
            
    def print(self, dest=sys.stdout):
        print("coeffs: {}".format(self.coeffs), file=dest)  
        
        function_str = self.function_strings.txt
        print(
            "which substituted in ax^2+bx+c gives: {}".format(function_str), 
            file=dest
        )

        if self.x_intercept_set.is_quadratic():
            print_quadratic_root_set(self.x_intercept_set)

            min_max = "maximum" if self.coeffs.a < 0 else "minimum"
            vertex_line = "vertex (x,y where y is at a {}): {}".format(
                min_max, self.vertex
            )
            print(vertex_line, file=dest)
        elif self.x_intercept_set.num_intercepts == 1:
            intercept_line = "x intercept (value of x where y=0):{}".format(
                self.x_intercept_set
            )
            print(intercept_line, file=dest)
    




