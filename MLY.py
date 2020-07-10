# Matrix Loves You : MLY.py

# Imports
from packages import start
from push import execute
import sys

# Codes starts here
if len(sys.argv) == 1:
    update_status = execute.update_check() # check for internet first
    if update_status != False:
        execute.update_action(update_status)
    execute.welcome(0)
    start.steps()
else:
    if sys.argv[1] == "-c":
        if sys.argv[2] == "matrix":
            start.steps()
        elif sys.argv[2] == "cramer":
            execute.welcome(1)
            start.express()
            # execute.welcome(-1)