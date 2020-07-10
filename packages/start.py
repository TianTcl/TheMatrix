# Matrix Loves You : packages/start.py

# Imports
from packages import convert, mInput, mPrint
from push import cramer

# Functions
def steps():
    mPrint.console(convert.data(mInput.run()))

def express():
    while True:
        cramer.cFind(cramer.cConvert(cramer.cInput()))