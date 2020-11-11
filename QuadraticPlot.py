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


from quadratic import create_quadratic_function
from quadratic_info import create_quadratic_plot_title
from line_plot import line_plot
from Object import Object
from NumRange  import NumRange

MIN_X_SPAN = 1e-3
MIN_NUM_VALS = 2


class QuadraticPlot(Object):
    def __init__(self,
                x_range = NumRange(-1.0, +1.0),
                num_vals = 100,
                
    ):
        self.__x_range = x_range
        self.__num_vals = num_vals
        
    @property
    def x_range(self):
        return self.__x_range

    @x_range.setter
    def x_range(self, x_range):
        self.__x_range = x_range


    @property
    def num_vals(self):
        return self.__num_vals

    @num_vals.setter
    def num_vals(self, num_vals):
        self.__num_vals = num_vals
        

    def check_settings(self):
        if self.x_range.span < MIN_X_SPAN:
            err_str = "x span ({:g}) is < min allowed value of {:g}".format(
                   self.x_range.span, MIN_X_SPAN)
            self.set_err(err_str)
            return False
        
        if self.num_vals < MIN_NUM_VALS:
            err_str = "x span ({:g}) is < min allowed value of {:g}".format(
                    self.num_vals, MIN_NUM_VALS)
            self.set_err(err_str)
            return False
        
        return True
    
    
    def plot(self, a, b, c):
        plot_title = create_quadratic_plot_title(a, b, c)

        f = create_quadratic_function(a, b, c)
        line_plot(f, self.x_range,
                    num_vals = self.num_vals,
                    plot_title=plot_title)


