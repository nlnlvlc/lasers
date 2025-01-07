"""
author: Nilan Lovelace
"""
def insertion(data:dict) -> dict:
    """
    performs insertion sort on a dictionary, data, in descneding order
    :param data: dictionary holding a tuple with coordinates: a tuple with direction and integer as key: value
    :return sortedDict: a new dictionary of the sorted data
    """

    #separates dictionary into two lists
    #one list holding keys, one holding values
    data_keys = list(data.keys())
    data_vals = list(data.values())
    #length of values
    n = len(data_vals)

    #loops through each value and compares the integer value
    #stored at index 1 of each element
    #if element is larger than the element before it, swap places
    #also swaps the places of the corresponding key values
    for i in range(0,n):
        pos = i
        while pos > 0 and data_vals[pos][1] > data_vals[pos - 1][1]:
            data_vals[pos], data_vals[pos - 1] = data_vals[pos - 1], data_vals[pos]
            data_keys[pos], data_keys[pos - 1] = data_keys[pos - 1], data_keys[pos]
            pos -= 1

    #combine sorted values and keys into a new dictionary
    sortedDict = {data_keys[j]: data_vals[j] for j in range(len(data_keys))}

    return sortedDict