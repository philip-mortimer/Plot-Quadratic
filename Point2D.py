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


from format_num import format_real

class Point2D:
    """x and y cartesian coordinates."""
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

        self.__point_str = None
   
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y

    def __str__(self):
        if self.__point_str is None:
            x_str = format_real(self.x)
            y_str = format_real(self.y)

            self.__point_str = "x={},y={}".format(x_str, y_str)
        return self.__point_str
