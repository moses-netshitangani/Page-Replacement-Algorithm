# Program to simulate the FIFO, LRU and Optimal page replacement algorithms
# Names: Moses Netshitangani
# Student number: NTSNDI017
# Date: 16 May 2020

import random
import sys


# FIFO implementation
def FIFO(size, page_sequence_fifo):
    print(' FIFO '.center(80, "*"))

    page_faults = 0

    # 2D array to store page:age values. Acts as main memory
    memory_dict = []

    # insert rest of pages into memory
    for i in range(0, len(page_sequence_fifo)):
        page = page_sequence_fifo[i]
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
    show_memory(memory_dict)
    return page_faults


# LRU implementation
def LRU(size, page_sequence_lru):
    print(' LRU '.center(80, "*"))
    page_faults = 0

    # 2D array to store page:age values. Acts as memory
    memory_dict = []

    # insert rest of pages into memory
    for i in range(0, len(page_sequence_lru)):
        page = page_sequence_lru[i]

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
    show_memory(memory_dict)
    return page_faults


# Optimal implementation
def OPT(size, page_sequence_opt):
    print(' OPT '.center(80, "*"))

    page_faults = 0

    # 2D array to store page:age values. Acts as memory
    memory_dict = []

    # insert rest of pages into memory
    for i in range(0, len(page_sequence_opt)):
        page = page_sequence_opt[i]
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
            memory_dict[future(i + 1, page_sequence_opt, memory_dict)] = [page, 0]
    show_memory(memory_dict)
    return page_faults


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


# prints out pages in a formatted way
def show_memory(memory_array):
    print('Final state of memory: ', end=" ")
    for i in range(0, len(memory_array)):
        print(memory_array[i][0], end="     ")
    print()


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


# converts user-entered page_sequence into sequence of integers
def process_pages(page_sequence):
    sequence = page_sequence[1:len(page_sequence)-1].split(',')
    pages = []
    for page in sequence:
        pages.append(eval(page))
    return pages


def create_random_pages(pages):
    # Creating array of random integers between 0-9 to
    pages = int(pages)
    page_string = []
    i = 0
    while i < pages:
        page_string.append(int(random.random() * 10))
        i += 1
    return page_string


def main():
    frame_size = sys.argv[1]

    if len(sys.argv) == 3 and sys.argv[2][0] != '[':
        # Sequence length has been provided
        page_sequence = create_random_pages(sys.argv[2])
        print('\nPage sequence to be used: ', page_sequence, '\n')
        print('FIFO ', FIFO(eval(frame_size), page_sequence), 'page faults \n')
        print('LRU ', LRU(eval(frame_size), page_sequence), 'page faults \n')
        print('OPT ', OPT(eval(frame_size), page_sequence), 'page faults \n')
    elif len(sys.argv) == 3 and sys.argv[2][0] == '[':
        # Page sequence has been provided
        page_sequence = process_pages(sys.argv[2])
        print('\nPage sequence to be used: ', page_sequence, '\n')
        print('FIFO ', FIFO(eval(frame_size), page_sequence), 'page faults \n')
        print('LRU ', LRU(eval(frame_size), page_sequence), 'page faults \n')
        print('OPT ', OPT(eval(frame_size), page_sequence), 'page faults \n')
    else:
        # Sequence length has not been provided. Choose a random sequence between 10 and 50
        page_sequence = create_random_pages(random.randint(10, 50))
        print('\nPage sequence to be used: ', page_sequence, '\n')
        print('FIFO ', FIFO(eval(frame_size), page_sequence), 'page faults \n')
        print('LRU ', LRU(eval(frame_size), page_sequence), 'page faults \n')
        print('OPT ', OPT(eval(frame_size), page_sequence), 'page faults \n')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: py paging.py frame_size\nOR\npy paging.py frame_size sequence_length\nOR\npy paging.py '
              'frame_size page_sequence(as a square-bracket enclosed comma-separated string e.g [7,5,8,4,6])')
    else:
        main()
