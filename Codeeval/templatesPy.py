#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Copyright (C) 2017 Raj Kumar Lath
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import itertools
import sys

# if python 2+
if sys.version_info.major == 2:
    MAXINT =  sys.maxint
    MININT = -sys.maxint - 1

    filter = itertools.ifilter
    map    = itertools.imap
    range  = xrange
    zip    = itertools.izip
    
# if python 3+
else:
    MAXINT =  sys.maxsize
    MININT = -sys.maxsize - 1
    
    
    

# adopted for codeeval
if __name__ == '__main__':
    test_cases = open(sys.argv[1], 'r')
    for line in test_cases:
        ls = line.rstrip('\n')

    test_cases.close()


