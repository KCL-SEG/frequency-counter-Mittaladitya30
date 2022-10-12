"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
 freq = {}

 for i in items:
     if isinstance(i, int):
        items.remove(i)
        i = str(i)
        items.append(i)
 for x in items:
     freq[x] = items.count(x)
 print(freq)

frequencies([100, '100', 'hello', 100, '100'])
