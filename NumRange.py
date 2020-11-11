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


class NumRange:
    def __init__(self, min_val, max_val):
        if min_val > max_val:
            if np.isclose(min_val, max_val):
                self.__min_val = min_val
                self.__max_val = min_val
            else:
                assert False, 'min_val must be <= max_val' 
        else:
            self.__min_val = min_val
            self.__max_val = max_val

    @property
    def min_val(self):
        return self.__min_val

    @property
    def max_val(self):
        return self.__max_val
        
    @property
    def span(self):
        return self.max_val - self.min_val
