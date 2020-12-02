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
from quadratic import find_quadratic_roots, find_quadratic_vertex 

SUPERSCRIPT_SQUARED = r'$^2$'
TEXT_SQUARED = r'^2'
        
    
def format_num(x):
    if abs(x) < 1e5:
        str = "{:0.3f}".format(x).rstrip('0').rstrip('.')
        if str == "-0":
            return "0"
        else:
            return str
    else:
        return "{:g}".format(x)


def format_complex(x):
    real_str = format_num(x.real)
    imag_str = format_num(abs(x.imag))

    sign = '-' if x.imag < 0 else '+'
    return "({} {} {}i)".format(real_str, sign, imag_str)


def get_formatted_intercept(a, b):
    return format_num(-b/a)

    
def get_formatted_quadratic_roots(a, b, c):
    (root1, root2) = find_quadratic_roots(a, b, c)

    if np.isreal(root1) and np.isreal(root2):
        return ( format_num(root1.real), format_num(root2.real) )
    else:
        return ( format_complex(root1), format_complex(root2) )        

  
def create_roots_descr(a, b, c):
    if np.isclose(a, 0.0):
        if np.isclose(b, 0.0):
            # It is just a constant equal to c.
            descr = ""
        else:
            # It is linear.
            intercept = get_formatted_intercept(b, c)
            descr = "x={} where y=0".format(intercept)
    else:
        root1_str, root2_str = get_formatted_quadratic_roots(a, b, c)
        if root1_str == root2_str:
            descr = "root is " + root1_str
        else:
            descr = "roots are {} and {}".format(root1_str, root2_str)
    return descr


def create_pre_x_str(coeff, always_show_sign):
    """Returns the string preceding the 'x' in ax^2 or bx, where coeff is
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

        
def create_quadratic_eqn_str(a, b, c, squared_str):
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
        
        
def create_quadratic_plot_title(a, b, c):
    eqn_str = create_quadratic_eqn_str(a, b, c, SUPERSCRIPT_SQUARED)
    descr = create_roots_descr(a, b, c)
    if descr == "":
        return eqn_str
    else:
        return "{}: {}".format(eqn_str, descr)
    
    
def print_quadratic_info(a, b, c):
    print("coeffs: a={:g},b={:g},c={:g}".format(a, b, c))  
    
    eqn_str = create_quadratic_eqn_str(a, b, c, TEXT_SQUARED)
    print("which substituted in ax{}+bx+c gives: {}".format(
            TEXT_SQUARED, eqn_str))
    
    if np.isclose(a, 0.0):
        if not np.isclose(b, 0.0):
            intercept = get_formatted_intercept(b, c)
            print("intercept (value of x where y=0): {}".format(intercept))
    else:
        root1_str, root2_str = get_formatted_quadratic_roots(a, b, c)
        if root1_str == root2_str:
            print("root (x value where y=0): {}".format(root1_str))
        else:            
            print("roots (x values where y=0): {},{}".format(
                    root1_str, root2_str))
    
        vertex_x, vertex_y = find_quadratic_vertex(a, b, c)
        min_max = "maximum" if a < 0 else "minimum"
        print("vertex (x,y where y is at a {}): x={},y={}".format(
                min_max, vertex_x, vertex_y))
    
