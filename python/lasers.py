"""
In this puzzle, you are given a rectangular grid of numbers, and a set of three-way lasers
to place. Each laser is centered on one square of the grid and covers three of the four horizontally or
vertically adjacent squares. Your goal is to cover the highest sum of numbers possible.

Note that if two lasers shoot at the same square, you can count that value twice,
but you cannot have two lasers centered on the same square.

You also may not place a laser such that it would shoot outside the grid (this would be very dangerous to spectators!).

author: Nilan Lovelace
"""
from dataclasses import dataclass
from insertion import insertion
import itertools
import sys

@dataclass
class Lasers:
    field: list
    lasers: dict
    maximums: dict

def getMap() -> None:
    """
    reads the puzzle contents from a file and prints the puzzle
    :return None:
    """
    #reads the second argument as our filename
    filename = sys.argv[1]

    #reads puzzle from file
    file = open(filename)
    lines = file.readlines()
    file.close()

    print("\nLoaded: " + filename)

    # removes \n character and prints puzzle
    lines = [line.replace('\n', '') for line in lines]

    for line in lines: print(line)

    #removes spaces between characters
    lines = [line.replace(' ', '') for line in lines]

    #loops through each line of the puzzle and appends it to field
    field = [line for line in lines]

    Lasers.field = field

    for line in field:
        for spot in line:
            if not spot.isdigit():
                print("This puzzle isn't usable. Must only contain digits.")
                sys.exit()

def possiblePositions() -> int:
    """
    finds the numbers of places on a field a laser can possible be centered
    :return int: the number of spaces where a laser can be placed
    """
    #cases where the field is too small to place a laser
    if len(Lasers.field) < 2 or len(Lasers.field[0]) < 2:
        return 0
    #finds how many legal positions there are for a laser to be placed when field is big enough
    #the top, bottom, left, and right borders have unplaceable positions
    if (len(Lasers.field) >= 2 and len(Lasers.field[0]) > 2) or (len(Lasers.field) > 2 and len(Lasers.field[0]) >= 2):
        topBott = (len(Lasers.field) - 2) * 2
        leftRight = (len(Lasers.field[0]) - 2) * 2
        middle = (len(Lasers.field) - 2) * (len(Lasers.field[0]) - 2)

        if topBott == 0 or leftRight == 0:
            return 0

        return topBott + leftRight + middle

def addEmUp() -> None:
    """
    finds all possible, legal placements of lasers per spot on the field and records the orientation of the laser and the sum of values
    :return None:
    """

    #call field
    field = Lasers.field

    #records the coordinates for the center of laser, the direction it's facing
    # and the value of the laser placement with the highest sum
    maximums = {}

    #loops through each spot in each line of the field
    for i in range(0, len(field)):
        for j in range(0, len(field[i])):
            MAX = 0
            temp = 0

            #if there is a legal spot in relation to the current spot, collect that value
            #if there is not legal spot in that direction, value is -1
            north = -1
            south = -1
            east = -1
            west = -1

            if i-1 >=0: north = int(field[i-1][j])
            if i+1 < len(field): south = int(field[i+1][j])
            if j+1 < len(field[i]): east = int(field[i][j+1])
            if j-1 >= 0: west = int(field[i][j-1])

            #if at least three directions have legal spots, add those values together
            #if that value is larger than current MAX, save new MAX and record orientation (pos)
            if north != -1 and west != -1 and east != -1:
                temp = north + west + east
                if temp > MAX:
                    MAX = max(MAX, temp)
                    pos = "N"
            if west != -1 and north != -1 and south != -1:
                temp = west + north + south
                if temp > MAX:
                    MAX = max(MAX, temp)
                    pos = "W"
            if east != -1 and north != -1 and south != -1:
                temp = east + north + south
                if temp > MAX:
                    MAX = max(MAX, temp)
                    pos = "E"
            if south != -1 and east != -1 and west != -1:
                temp = south + east + west
                if temp > MAX:
                    MAX = max(MAX, temp)
                    pos = "S"
            #update maximums with the coordinates, orientation, and MAX value with the highest sum for this position
            #key: tuple (i:int, j:int), value: tuple (pos: str, MAX: int)
            if MAX > 0:
                maximums.update({(i,j): (pos, MAX)})
    #store maximums in Lasers.maximums to be used outside of function
    Lasers.maximums = maximums

def placeLasers(num: int) -> None:
    """
    places desired number laser covering the highest possible values
    :param num: number of lasers being placed
    :return None:
    """
    #collect our stored maximum values and their coordinates and orientation
    maximums = Lasers.maximums
    #sorts the lasers by maximum values, descending order
    sortedDict = insertion(maximums)
    #the num-th number of lasers to nbe placed
    lasers = dict(itertools.islice(sortedDict.items(), num))
    #stores lasers to be placed in Laser class to be referenced outside of function
    Lasers.lasers = lasers

    print("Optimal placement: ")

    #loops through the lasers to be placed
    #prints the lasers location, orientation, and the value of the placement
    total = 0
    for key, value in lasers.items():
        MAX = lasers[key][1]
        location = key
        pos = value[0]
        total += MAX
        print("loc: " + str(location) + ", facing: " + pos + ", sum: " + str(MAX))
    #prints total value of all lasers placed
    print("Total: " + str(total))

def legalInput(num: str) -> int:
    """
    checks if user has entered a legal input
    :param num: the user's input
    :return int: returns as an int if legal
    """
    #try to turn the input into an int
    #if not possible, end program
    try:
        num = int(num)
    except:
        print("Not a valid output. Integers only.")
        sys.exit()

    #if users attempts to place more lasers than can fit on field
    #print an error and end the program
    if num > possiblePositions():
        print("Too many lasers to place!")
        sys.exit()
    elif num >= 0:
        return num
    #if use attempts to place a negative number of lasers
    #end the program
    elif num < 0:
        sys.exit()

def userInput() -> None:
    """
    handles user input then places lasers
    :return None:
    """

    #take user's input for number of lasers to be placed
    lasers = input("Enter number of lasers: ")
    #checks if input is legal
    lasers = legalInput(lasers)

    #finds max values in each position
    addEmUp()
    #places the number of lasers requested
    placeLasers(lasers)

def main() -> None:
    """
    allows the program to be executed
    :return None:
    """
    # if user doesn't input enough arguments in terminal
    # print warning and end the program
    if len(sys.argv) != 2:
        print("Usage: python3 lasers.py filename")
        sys.exit()

    play = True

    while play:
        #produced field
        getMap()
        #place lasers
        userInput()

        prompt = input("\nWould you like to try again? (y/n): ").lower()

        if prompt != 'y':
            play = False

if __name__ == '__main__':
    main()
