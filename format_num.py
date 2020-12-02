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


def format_real(x):
    """
    Returns string representation of real number x.
    """
    if abs(x) < 1e6:
        str = "{:0.4f}".format(x).rstrip('0').rstrip('.')
        if str == "-0":
            return "0"
        else:
            return str
    else:
        return "{:g}".format(x)


def format_complex(z):
    """
    Returns string representation of complex number z.
    """
    real_str = format_real(z.real)
    imag_str = format_real(abs(z.imag))

    sign = '-' if z.imag < 0 else '+'
    return "({} {} {}i)".format(real_str, sign, imag_str)


def format_num(x):
    """
    Returns string representation of x which may be complex or real.
    """
    if np.isreal(x):
        return format_real(x.real)
    else:
        return format_complex(x)
