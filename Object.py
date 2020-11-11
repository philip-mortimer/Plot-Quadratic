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


class Object:
    def __init__(self,
                err_detected = False,
                err_str = ''
    ):
        self.__err_detected = err_detected
        self.__err_str = err_str
        
    @property
    def err_detected(self):
        return self.__err_detected

    @err_detected.setter
    def err_detected(self, err_detected):
        self.__err_detected = err_detected


    @property
    def err_str(self):
        return self.__err_str

    @err_str.setter
    def err_str(self, err_str):
        self.__err_str = err_str
        
        
    def set_err(self, err_str):
        self.err_detected = True
        self.err_str = err_str
        
        
    