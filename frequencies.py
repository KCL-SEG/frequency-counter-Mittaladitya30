"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
  freq = {}

  for i in range(0, len(items)-1):
      if isinstance(items[i], int):

         items[i] = str(items[i])

  for x in items:
      freq[x] = items.count(x)
  return freq
