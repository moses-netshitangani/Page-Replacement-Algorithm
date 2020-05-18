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
            # replace the oldest page in memory
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
    memory_dict.append([page_numbers[0], 0])
    page_faults += 1
    page_numbers = page_numbers[1:]

    # insert rest of pages into memory
    for i in range(0, len(page_numbers)):
        page = page_numbers[i]
        #print('Now inserting: ', page)
        # insert into new frame only if frame size not full
        if len(memory_dict) < size and check(page, memory_dict) == -1:
            page_faults += 1
            memory_dict = grow_age(memory_dict)
            memory_dict.append([page, 0])
        elif check(page, memory_dict) != -1:
            # means it's a hit.
            memory_dict = grow_age(memory_dict)
        else:
            # replace page that won't be used the most in the future.
            page_faults += 1
            memory_dict = grow_age(memory_dict)
            memory_dict[future(i+1, page_numbers, memory_dict)] = [page, 0]
            #print('page went into third')
        print(memory_dict)
    print("number of faults: " + str(page_faults))


# returns index of page that is least used in the future
def future(start_index, page_numbers, memory_dict):
    # putting all in-memory pages into an array for comparison
    pages = []
    ages = []
    max_age = -1
    page_index = -1
    for pairs in memory_dict:
        pages.append(pairs[0])
        ages.append(pairs[1])
    pages_copy = pages.copy()
    #print('**************** future session ********************')
    #print('Start index of base array is ', start_index)
    # determining which in-memory page is least used in the future
    for i in range(start_index, len(page_numbers)):
        future_page = page_numbers[i]
        #print('Candidate page is ', future_page, 'with index ', i, ' in the base array ', page_numbers)
        if future_page in pages:
            pages.pop(pages.index(future_page))
            #print('Just removed ', future_page, ' as a candidate.')
        if len(pages) == 1:
            #print('Only page left in list is ', pages[0], 'with index of ', pages_copy.index(pages[0]), 'in copy ', pages_copy)
            return pages_copy.index(pages[0])
    #print('Remaining pages ', pages)
    for page in pages:
        if ages[pages_copy.index(page)] > max_age:
            max_age = ages[pages_copy.index(page)]
            page_index = pages_copy.index(page)
            #print('max_age currently is: ', max_age, ' and belongs to ', page, 'at index ', page_index)
    #print('Last resort, oldest page index is: ', page_index)
    return page_index

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
    #print(page_string)
    #return page_string
    #return [2, 3, 4, 2, 1, 3, 7, 5]
    #return [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    #return [4, 7, 6, 1, 7, 6, 1, 2, 7, 2]
    return [1, 2, 3, 4, 2, 1, 5, 6, 2, 1, 2, 3, 7, 6, 3, 2, 1, 2, 3, 6]


def main():
    FIFO(4, 5)
    LRU(4, 5)
    OPT(4, 5)


if __name__ == '__main__':
    main()
