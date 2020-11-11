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
import matplotlib.pyplot as plt


def line_plot(f, x_range,
                num_vals = 200,
                plot_title = ''):
    """f must be a function which takes a 
    single numeric argument and returns a numeric value.
    """
    x_list = np.linspace(x_range.min_val, x_range.max_val, num=num_vals)
    y_list = [f(x) for x in x_list]
 
    # Draw horizontal line where y = 0.
    plt.axhline(y=0.0, linewidth=1, color='black')
    
    plt.plot(x_list, y_list, linewidth=1)
    plt.grid(True)
    if plot_title != '':
        plt.title(plot_title)
    plt.xlabel('x')
    plt.ylabel('y')

    plt.show()
