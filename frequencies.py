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

  for x in items:
      if x not in freq.keys():
          freq[x] = 1
      else:
          freq[x] += 1

  return freq;
