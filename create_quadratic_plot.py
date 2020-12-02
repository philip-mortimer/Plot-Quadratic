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


import matplotlib.pyplot as plt

from QuadraticInfo import QuadraticInfo


def get_intercept_descr(x_intercept_set):
    descr = ""
    if x_intercept_set.is_quadratic():
        if x_intercept_set.num_intercepts == 2:
            roots_str = x_intercept_set.get_intercepts_str(sep=" and ")
            descr = "roots are {}".format(roots_str)
        else:
            descr = "root is {}".format(x_intercept_set)
    elif x_intercept_set.num_intercepts == 1:
        descr = "x={} where y=0".format(x_intercept_set)
    else:
        descr = ""
    return descr


def create_quadratic_plot_title(info: QuadraticInfo):
    function_str = info.function_strings.gui
    intercept_descr = get_intercept_descr(info.x_intercept_set)
    if intercept_descr == "":
        return function_str
    else:
        return "{}: {}".format(function_str, intercept_descr)


def create_quadratic_plot(x, info: QuadraticInfo) -> plt.Figure:
    """
    x:    the plot's x values

    info: contains information to appear in the plot title, and a method
          (create_quadratic_function) that returns a quadratic function 
          corresponding to the coefficients in info.coeffs
    """
    f = info.create_quadratic_function()
    y = [f(x_val) for x_val in x]

    figure, ax = plt.subplots()
    figure.canvas.set_window_title("Quadratic Function")

    plot_title = create_quadratic_plot_title(info)
    ax.set_title(plot_title)

    ax.grid(True)

    ax.set_xlabel("x")
    ax.set_ylabel("y")

    # Draw horizontal line where y = 0.
    ax.axhline(y=0.0, linewidth=1, color='black')
    
    ax.plot(x, y, linewidth=1)

    return figure


 

