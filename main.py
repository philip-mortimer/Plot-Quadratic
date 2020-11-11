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

from QuadraticPlot import QuadraticPlot
from NumRange  import NumRange
from quadratic_info import print_quadratic_info
import params as prm

def main():
    if prm.verbose:
        print_quadratic_info(prm.a, prm.b, prm.c)
        
    # Create plot object.
    plot_obj = QuadraticPlot()
    
    # Assign settings to plot object.
    plot_obj.x_range   = NumRange(prm.min_x, prm.max_x)
    plot_obj.num_vals  = prm.num_vals
    
    # Check that the settings are valid.
    if not plot_obj.check_settings():
        print('Error - {}'.format(plot_obj.err_str))
        return 1
    
    # Run the plot.
    plot_obj.plot(prm.a, prm.b, prm.c)
    
    return 0

if __name__ == '__main__':
    exit_code = main()
    exit(exit_code)
