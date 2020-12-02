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


SUPERSCRIPT_SQUARED = r'$^2$'
TEXT_SQUARED = r'^2'

import numpy as np


def create_pre_x_str(coeff, always_show_sign):
    """
    Returns the string preceding the 'x' in ax^2 or bx, where coeff is
    the value a or b. If always_show_sign is True then the string
    returned by the function will always begin with "-" or "+" 
    depending on the sign of coeff, otherwise it will only begin
    with the sign if coeff is negative. If the string that results from
    formatting coeff is "1", "+1" or "-1" then the function will
    return "", "+" and "-" respectively. This will result in,
    for example, x^2-x rather than 1x^2-1x.
    """
    if always_show_sign:
        pre_x_str = "{:+g}".format(coeff)
    else:
        pre_x_str = "{:g}".format(coeff)

    if pre_x_str == "1":
        pre_x_str = ""
    elif pre_x_str == "+1":
        pre_x_str = "+"
    elif pre_x_str == "-1":
        pre_x_str = "-"
    
    return pre_x_str

        
def create_quadratic_function_str(a, b, c, squared_str):
    expr = ""
    
    if not np.isclose(a, 0.0):
        # a is non-zero so create ax^2 term.
        pre_x_str = create_pre_x_str(a, always_show_sign = False)
        expr += "{}x{}".format(pre_x_str, squared_str)
        
    if not np.isclose(b, 0.0):
        # b is non-zero so create bx term.
        
        # If expr contains ax^2 term then bx term must 
        # be preceded by '+' or '-'.
        always_show_sign = len(expr) > 0  
        
        pre_x_str = create_pre_x_str(b, always_show_sign)
        expr += "{}x".format(pre_x_str)

    if len(expr) > 0:
        # expr contains terms for ax^2, bx or both, so only add c 
        # term if it is non-zero.
        if not np.isclose(c, 0.0):
            expr += "{:+g}".format(c)
    else: 
        # expr contains no ax^2 or bx terms, so expr consists of const
        # value c only.           
        expr = "{:g}".format(c)
    
    return "y=" + expr


class QuadraticFunctionStrings():
    """
    Contains 2 string representations of the quadratic function:
    
    1) plain text representation where 'squared' symbol is written as '^2'
       e.g. '4x^2+2x+3'

    2) representation suitable for GUI environments (e.g in plot title)
       where 'squared' symbol appears as superscript 2
    """
    def __init__(self, a, b, c):
        self.__gui = create_quadratic_function_str(
            a, b, c, SUPERSCRIPT_SQUARED
        )

        self.__txt = create_quadratic_function_str(
            a, b, c, TEXT_SQUARED
        )
    
    @property
    def txt(self):
        return self.__txt

    @property
    def gui(self):
        return self.__gui

