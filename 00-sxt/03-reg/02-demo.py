'''

\d = [0-9]
\D = [^0-9]
\w = [a-zA-Z0-9_]
\W = [^a-zA-Z0-9_]
'''
import re

# [^] ^在[] 里面是取反

result = re.match("1[^34]", '19')
print(result)

result = re.match("1[^34]", '13')
print(result)

result = re.match("1[a-z5-9]", '13')
print(result)
