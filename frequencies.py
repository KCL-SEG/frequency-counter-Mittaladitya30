"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
  freq = {}
  count = 0

  for i in items:
      if isinstance(i, int):
          items.remove(i)
          i = str(i)
          items.append(i)
  print(items)

  for x in items:
      if x not in freq.keys():
          freq[x] = 1
      else:
          freq[x] += 1

  print(freq)

frequencies([100, 'Hello', '100', '100', 100])
