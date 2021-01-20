import difflib
from pprint import pprint
import sys

text1 = '''1. Beautiful is better than ugly.
2. Explicit is better than implicit.
3. Simple is better than complex.
4. Complex is better than complicated.
'''.splitlines(keepends=True)

text2 = '''1. Beautiful is better than ugly.
3.   Simple is better than complex.
4. Complicated is better than complex.
5. Flat is better than nested.
'''.splitlines(keepends=True)

d = difflib.Differ()
result = list(d.compare(text1, text2))
pprint(result)
sys.stdout.writelines(result)




