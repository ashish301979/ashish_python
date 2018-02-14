#!/usr/bin/python
import sys
from sys import stdout
stdout = ''.join(str(x) for x in (1,5,7))
print(stdout)
print(*range(1,11))
