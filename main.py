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

#import numpy as np
#import matplotlib.pyplot as plt

from create_quadratic_plot import create_quadratic_plot
from plot_utils import create_x_array, save_plot, show_all
from QuadraticInfo import QuadraticInfo
import params as prm

def main():
    info = QuadraticInfo(prm.A, prm.B, prm.C)
    if prm.VERBOSE:
        info.print()

    x = create_x_array(prm.MIN_X, prm.MAX_X, prm.NUM_VALS)
    plot = create_quadratic_plot(x, info)
    if prm.SHOW_PLOT:
        show_all()

    if prm.PLOT_PATH != '':
        ok, err_str = save_plot(plot, prm.PLOT_PATH)
        if not ok:
            print(err_str)
            return 1    
    return 0

if __name__ == '__main__':
    exit_code = main()
    exit(exit_code)
