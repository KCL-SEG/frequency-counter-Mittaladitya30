"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
  frequencies = {}
  count = 0

  for i in range(len(items)):
      j = items[0]

      items.remove(j)
      if isinstance(j, int):


          j= str(j)
      items.append(j)


  for x in items:
      if x not in freq.keys():
          freq[x] = 1
      else:
          freq[x] += 1
  return frequencies
