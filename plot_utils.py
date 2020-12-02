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
import numpy as np

def create_x_array(min_x, max_x, num_vals=100):
    return np.linspace(min_x, max_x, num=num_vals)

def save_plot(plot: plt.Figure, path):
    err_str = ''
    try:
        plot.savefig(path)
        ok = True
    except Exception as e:
        ok = False
        err_str = "Error saving plot: {}".format(e)
    return (ok, err_str)

def show_all():
    plt.show()