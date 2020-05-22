# Program to simulate the FIFO, LRU and Optimal page replacement algorithms
# Names: Moses Netshitangani
# Student number: NTSNDI017
# Date: 16 May 2020

import random


# FIFO implementation
def FIFO(size, pages):
    page_faults = 0

    # create array of random page numbers between 0:9
    page_numbers = allocator(pages)

    # 2D array to store page:age values. Acts as memory
    memory_dict = []

    # insert initial page into memory with age of 0.
    if len(page_numbers) > 0:
        memory_dict.append([page_numbers[0], 0])
        page_faults += 1
        page_numbers = page_numbers[1:]

    # insert rest of pages into memory
    for i in range(0, len(page_numbers)):
        page = page_numbers[i]
        # insert into new frame only if frame size not full
        if len(memory_dict) < size and check(page, memory_dict) == -1:
            page_faults += 1
            memory_dict = grow_age(memory_dict)
            memory_dict.append([page, 0])
        elif check(page, memory_dict) != -1:
            # means it's a hit. No need to reset page age's value
            memory_dict = grow_age(memory_dict)
        else:
            # replace the oldest page in memory
            page_faults += 1
            memory_dict = grow_age(memory_dict)
            memory_dict[oldest(memory_dict)] = [page, 0]
        print(memory_dict)
    print("number of faults: " + str(page_faults))


# LRU implementation
def LRU(size, pages):
    page_faults = 0

    # create array of random page numbers between 0:9
    page_numbers = allocator(pages)

    # 2D array to store page:age values. Acts as memory
    memory_dict = []

    # insert initial page into memory with age of 0.
    if len(page_numbers) > 0:
        memory_dict.append([page_numbers[0], 0])
        page_faults += 1
        page_numbers = page_numbers[1:]

    # insert rest of pages into memory
    for i in range(0, len(page_numbers)):
        page = page_numbers[i]

        # insert into new frame only if frame size not full
        if len(memory_dict) < size and check(page, memory_dict) == -1:
            page_faults += 1
            memory_dict = grow_age(memory_dict)
            memory_dict.append([page, 0])
        elif check(page, memory_dict) != -1:
            # means it's a hit. Replace page's age value with 0, as if it were new
            memory_dict = grow_age(memory_dict)
            memory_dict[check(page, memory_dict)] = [page, 0]
        else:
            # replace the least recently used page in memory
            page_faults += 1
            memory_dict = grow_age(memory_dict)
            memory_dict[oldest(memory_dict)] = [page, 0]
        print(memory_dict)
    print("number of faults: " + str(page_faults))


# Optimal implementation
def OPT(size, pages):
    page_faults = 0

    # create array of random page numbers between 0:9
    page_numbers = allocator(pages)

    # 2D array to store page:age values. Acts as memory
    memory_dict = []

    # insert initial page into memory with age of 0.
    if len(page_numbers) > 0:
        memory_dict.append([page_numbers[0], 0])
        page_faults += 1
        page_numbers = page_numbers[1:]

    # insert rest of pages into memory
    for i in range(0, len(page_numbers)):
        page = page_numbers[i]
        # insert into new frame only if frame size not full
        if len(memory_dict) < size and check(page, memory_dict) == -1:
            page_faults += 1
            memory_dict = grow_age(memory_dict)
            memory_dict.append([page, 0])
        elif check(page, memory_dict) != -1:
            # means it's a hit.
            memory_dict = grow_age(memory_dict)
        else:
            # replace page that won't be used the most in the future, or the closest page using indices.
            page_faults += 1
            memory_dict = grow_age(memory_dict)
            memory_dict[future(i + 1, page_numbers, memory_dict)] = [page, 0]
        print(memory_dict)
    print("number of faults: " + str(page_faults))


# returns index of page that is least used in the future
def future(start_index, page_numbers, memory_dict):
    # putting all in-memory pages into an array for comparison
    pages = []
    ages = []
    for pairs in memory_dict:
        pages.append(pairs[0])
        ages.append(pairs[1])
    pages_copy = pages.copy()
    # determining which in-memory page is least used in the future
    for i in range(start_index, len(page_numbers)):
        future_page = page_numbers[i]
        if future_page in pages:
            pages.pop(pages.index(future_page))
        if len(pages) == 1:
            # this is the page that gets used the latest in the future
            return pages_copy.index(pages[0])
    return pages_copy.index(pages[0])


# returns index of oldest page in memory
def oldest(memory_dict):
    max_age = -1
    index = -1
    for i in range(0, len(memory_dict)):
        if memory_dict[i][1] > max_age:
            max_age = memory_dict[i][1]
            index = i
    return index


# checks to see if page is in memory
def check(page, memory_dict):
    for i in range(0, len(memory_dict)):
        if page == memory_dict[i][0]:
            return i
    return -1


# increments the 'age' values of each page in memory
def grow_age(memory_dict):
    for page in memory_dict:
        page[1] = page[1] + 1
    return memory_dict


def allocator(pages):
    # Creating array of random integers between 0-9
    pages = int(pages)
    page_string = []
    i = 0
    while i < pages:
        page_string.append(int(random.random() * 10))
        i += 1
    return page_string


def main():
    FIFO(3, 32)
    LRU(3, 32)
    OPT(3, 32)


if __name__ == '__main__':
    main()
