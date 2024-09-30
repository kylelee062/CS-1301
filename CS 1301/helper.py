"""
Program Description:
This is a repository of helpful functions.

Author: Faris Hawamdeh
"""

# Week 8 Lab
# chunk() splits a string into a list of sub strings of chunk_size
def chunk(string, chunk_size):
    chunk_list = []

    num_chunks = len(string) // chunk_size

    for i in range(0, len(string), chunk_size):
        chunk_list.append(string[i:i+chunk_size])

    return chunk_list

# Week 9 Lab
# print_grid() prints a 2-dimensional nested list of values as a grid
def print_grid(grid):
  for row in grid:
    for column in row:
      print(column, end=" ")
    print()
