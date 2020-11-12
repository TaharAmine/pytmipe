# -*- coding: UTF-8 -*-
# By Quentin HARDY (quentin.hardy@protonmail.com) - bobsecq

import sys
sys.path.append('../')
from impersonate import Impersonate
from utils import *

configureLogging()
imp = Impersonate()
print("Print current effective token for current thread:")
imp.printCurrentThreadEffectiveToken(printFull=True, printLinked=True)