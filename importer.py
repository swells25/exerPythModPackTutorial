import sys
print(sys.path)

sys.path.append(r'C:\Users\Stacy\Documents\VS Code\exerPythModPackTutorial-1\mod.py')
print(sys.path)

import mod, fact
print(mod.__file__)
print(fact.__file__)

import re
print(re.__file__)

