import string
import textwrap
import re
s = "python is better programming language"
# print(string.capwords(s))

# s2 = """The textwrap module can be used to format text for output in
# situations where pretty-printing is desired. It offers
# programmatic functionality similar to the paragraph wrapping
# or filling features found in many text editors."""
# print(textwrap.fill(s2, width=30))
# print(textwrap.indent(s2, '*'))

pattern = "is"
match = re.search(pattern, s)
s = match.start()
e = match.end()
print(f"{match.re.pattern} \\ {s} \\ {e}")
