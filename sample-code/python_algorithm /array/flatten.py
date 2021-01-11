"""
Implement Flatten Arrays.
Given an array that may contain nested arrays,
produce a single resultant array.
"""
from collections.abc import Iterable

# return list
def flatten(input_arr, output_arr=None):
  if output_arr is None:
    output_arr = []
    for ele in input_arr:
      if isinstance(ele, Iterable):
        flatten(ele, output_arr)  #tall=recurision
      else: 
