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


from format_num import format_num, format_real


class XInterceptSet:
    """
    Root of class hierarchy which contains classes for storing quadratic 
    roots, linear x intercept etc. for equation ax^2 + bx + c = 0.
    """
    def __init__(self, intercepts, is_quadratic):
        self.__intercepts = intercepts
        self.__is_quadratic = is_quadratic

        self.__intercept_strings = None

    @property
    def intercepts(self):
        """Returns intercepts in a tuple."""
        return self.__intercepts

    @property
    def num_intercepts(self):
        return len(self.intercepts)

    @property
    def intercept_strings(self):
        """Returns string representations of the intercepts in a tuple."""
        if self.__intercept_strings is None:
            str_list = [
                format_num(intercept) for intercept in self.intercepts
            ]
            self.__intercept_strings = tuple(str_list)
        return self.__intercept_strings

    def get_intercepts_str(self, sep=","):
        """Returns a string representation of the intercepts."""
        return sep.join(self.intercept_strings)

    def __str__(self):
        return self.get_intercepts_str()

    def is_quadratic(self):
        """Returns True if the intercepts are quadratic roots."""
        return self.__is_quadratic


class QuadraticRootSet(XInterceptSet):
    """
    Root of class hierarchy which contains classes for storing roots of 
    quadratic equation ax^2 + bx + c = 0.
    """
    def __init__(self, roots):
        super().__init__(roots, is_quadratic=True)


class QuadraticRoot(QuadraticRootSet):
    """
    Root of quadratic equation ax^2 + bx + c = 0 where there is only 1 root
    (where the value of the discriminant b^2 - 4ac is zero).
    """
    def __init__(self, root):
        super().__init__((root,))

    @property
    def root(self):
        return self.intercepts[0]


class QuadraticRoots(QuadraticRootSet):
    """
    Roots of quadratic equation ax^2 + bx + c = 0 where there are 2 roots
    (where the value of the discriminant b^2 - 4ac is not zero).
    """
    def __init__(self, root1, root2):
        super().__init__((root1,root2))

    @property
    def root1(self):
        return self.intercepts[0]
    
    @property
    def root2(self):
        return self.intercepts[1]

    @property
    def roots(self):
        return (self.root1, self.root2)       

    def get_intercepts_str(self, sep=","):
        root1_str, root2_str = self.intercept_strings
        if root1_str==root2_str:
            return "both {} approximately".format(root1_str)
        else:
            return "{}{}{}".format(root1_str, sep, root2_str)


class LinearXInterceptSet(XInterceptSet):
    """
    Root of linear x intercept class hierarchy, including a class for the
    situation where there is no x intercept becuase the function is constant.
    """
    def __init__(self, intercepts):
        super().__init__(intercepts, is_quadratic=False)


class LinearXIntercept(LinearXInterceptSet):
    """x intercept of a non-constant linear function."""
    def __init__(self, intercept):
        super().__init__((intercept,))
    
    @property
    def intercept(self):
        return self.intercepts[0]


class NoXInterceptBecauseConst(LinearXInterceptSet):
    """
    Class for the situation where there is no x intercept because the function
    is constant.
    """
    def __init__(self):
        super().__init__(())




