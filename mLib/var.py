# Matrix Loves You : mLib/cramer.py

# Initialize
appVersion = "0.1.1.0 (BI)"
appVername = "Beta Iota"
appModified = "25/04/2020 - 17.25:42"
# GreekAlphabet = ("Alpha","Beta","Gamma","Delta","Epsilon","Zeta","Eta","Theta","Iota","Kappa","Lambda","Mu",
# "Nu","Xi","Omikron","Pi","Rho","Sigma","Tau","Upsilion","Phi","Hi","Psi","Omega")
Index = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
Integer = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
Lowercase = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
Uppercase = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
Delimiter = (" ",";",",","\t",":","\\","$","#","@")
Celimeter = ("; ",";",", ",",","\t",": ",":","' ","'","$ ","$","# ","#","@ ","@"," ")
Matsymbol = ("-",".","|","^","!")
Expsymbol = ("+","=")
Common = (Integer + Matsymbol)
Input = (Integer + Matsymbol + Delimiter)
restartPath = "TheMatrix.lnk"
restartArgs = ("-c matrix", "-c cramer")
detSize = (4,9,16,25,36,49,64,81,100)
commandCode = ("new","help","usage","restart","reset","stop","exit","quit") # No args
commandLine = ("det","transpose","inverse","prop") # 1 arg
commandCalc = ("compare","add","subtract","multiply","divide") # 2 args
commandArgs = ("member","minor","cofactor") # 3 args
commandDeprecated = ("dim","count","type") # Deprecated
commandList = u"""    Moderation
\t-new\t\t\t \u2192 Add new matrix
\t-help\t\t\t \u2192 Show this command list
\t-usage\t\t\t \u2192 Show command  Usage &  Examples
\t-restart, reset\t\t \u2192 Reset all values (restarts the program)
\t-quit, exit, stop\t \u2192 Exit program
    Matrix view
\t-Variable name\t\t \u2192 View all members
\t-Variable name with apostrophe \u2192 View transposed members
\t-member(, i, j)\t\t \u2192 View specifed member's value
\t-inverse()\t\t \u2192 View inversed members
    Properties
\t-prop()\t\t\t \u2192 View matrix properties (name, dimension, amount of member, type of matrix)
\t-compare(, )\t\t \u2192 See if both matrixes are equal or not
    Actions
\t-det()\t\t\t \u2192 Find determinant of matrix
\t-minor(, i, j)\t\t \u2192 Find minor of matrix
\t-cofactor(, i, j)\t \u2192 Find co-factor of matrix
    Operations
\t-add(, )\t\t \u2192 Add 2 matrixes
\t-subtract(, )\t\t \u2192 Subtract 2 matrixes
\t-multiply(, )\t\t \u2192 Multiply 2 matrixes (, ) or Multiply matrix by number (var, n)
\t-divide(, )\t\t \u2192 Divide matrix by number (var, n)
"""
commandUsage = """    Matrix view
\t-Variable name\t \t\t\t\t\t\t  Example: A, B, C
\t-Variable name with apostrophe \t\t\t\t\t  Example: A', B', C'
\t-member(, i, j)\t  Usage: member('matrix name', 'member's row', 'member's column')  Example: member(A, 2, 1)
\t-invert()\t  Usage: invert('matrix name')\t\t\t  Example: invert(A)
    Properties
\t-prop()\t\t  Usage: prop('matrix name')\t\t\t  Example: prop(A)
\t-compare()\t  Usage: compare('matrix name', 'matrix name')\t  Example: compare(A, B)
    Actions
\t-det()\t\t  Usage: det('matrix name')\t\t\t  Example: det(A)
\t-minor(, i, j)\t  Usage: minor('matrix name', 'row', 'column')\t  Example: minor(A, 2, 1)
\t-cofactor(, i, j) Usage: cofactor('matrix name', 'row', 'column') Example: cofactor(A, 2, 1)
    Operations
\t-add(, )\t  Usage: add('matrix name', 'matrix name')\t  Example: add(A, B)
\t-subtract(, )\t  Usage: subtract('matrix name', 'matrix name')\t  Example: subtract(A, B)
\t-multiply(, )\t  Usage: multiply('matrix name', 'matrix name')\t  Example: multiply(A, B)
\t\t\t  Usage: multiply('matrix name', 'real number')\t  Example: multiply(A, 1.5)
\t-divide(, )\t  Usage: divide('matrix name', 'real number')\t  Example: divide(A, 1.5)
"""