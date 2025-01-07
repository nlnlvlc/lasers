# Lasers

In this puzzle, you are given a rectangular grid of numbers, and a set of three-way lasers
to place. Each laser is centered on one square of the grid and covers three of the four horizontally or
vertically adjacent squares. Your goal is to cover the highest sum of numbers possible.

Note that if two lasers shoot at the same square, you can count that value twice,
but you cannot have two lasers centered on the same square.

You also may not place a laser such that it would shoot outside the grid (this would be very dangerous to spectators!).

## Run program

The program should execute on the command line as:

```commandline
$ python3 lasers.py filename
```
Where filename is the name of the text table containing the grid as one row per line, with
single integers 0-9, separated by spaces.



