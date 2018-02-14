import re
test="""
hello    hello
goodbye
bye bye bye
hello goodbye
"""
#pat=re.compile(r"\n(?P<x>\w*)\s*{\x}*\s*\n", re.MULTILINE)
#result=pat.sub("\0", test)
#pat=re.compile(r"$.*\s*\0*^")
#result=pat.sub("", test)
#pat=re.compile(r"\N(\$*)\s+(\0)+")
#result=pat.sub("\0", test)
pat=re.compile("^(?P<x>\S*)(\s+(?P=x))+\s*$", re.MULTILINE)
result=pat.sub("\g<x>", test)
print result
