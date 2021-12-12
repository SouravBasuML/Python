# ---------------------------------------------------------------------------------------------------------------------
# Package is a container/directory for multiple modules
# ---------------------------------------------------------------------------------------------------------------------
# Package
#  |
#  |--> Module/sub-module
#        |
#        | --> Function
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# Modules:
# ---------------------------------------------------------------------------------------------------------------------
import random

import pandas as pd                 # import pandas module and give it an alias pd

# The above is same as:
import pandas
pd = pandas

# The following allows to use math functions directly (without using dotted prefox math.)
# But it is safer not to use as it will conflict with other modules having same function names
from math import *


# ---------------------------------------------------------------------------------------------------------------------
# Sub-Modules:
# ---------------------------------------------------------------------------------------------------------------------
import numpy.random
random.randint()


# ---------------------------------------------------------------------------------------------------------------------
# import package.module (and all functions in the module)
# ---------------------------------------------------------------------------------------------------------------------
import ecommerce.Tax
import ecommerce.Shipping
print('\n')
ecommerce.Shipping.calc_shipping()
ecommerce.Tax.calc_tax()


import ecommerce.Shipping as s
import ecommerce.Tax as t
print('\n')
s.calc_shipping()
t.calc_tax()


# ---------------------------------------------------------------------------------------------------------------------
# from package import a specific module (and all functions in the module)
# ---------------------------------------------------------------------------------------------------------------------
from ecommerce import Shipping
from ecommerce import Tax
print('\n')
Shipping.calc_shipping()
Tax.calc_tax()


# ---------------------------------------------------------------------------------------------------------------------
# from package.module import a specific function
# ---------------------------------------------------------------------------------------------------------------------
from ecommerce.Shipping import calc_shipping
from ecommerce.Tax import calc_tax
print('\n')
calc_shipping()                         # # no need to type module name
calc_tax()


# ---------------------------------------------------------------------------------------------------------------------
# If module is in a complete different directory
# To find a module, Python will use the current directory and then all directories listed in the system path
# ---------------------------------------------------------------------------------------------------------------------
# import sys
# sys.path.append("C:\...")
# import ecommerce.Shipping as s
# s.calc_shipping()
