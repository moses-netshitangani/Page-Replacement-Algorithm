The output of each algorithm gives the final state of the 
main memory (which pages are left in memory) and the number 
of page faults incurred.

So this program can be used in 3 of the following ways:

1. py paging.py frame_size

- This creates a random sequence of pages within the program, 
which is then applied to the three algorithms, using the 
specified frame_size


2. py paging.py frame_size sequence_length 

- This does the same thing as above, but instead of a random 
page sequence length, the value in the parameter sequence_length 
is used to determine the length of the random sequence.


3. py paging.py frame_size page_sequence

- This refrains from creating a random sequence of pages, and instead 
uses a user-specified page sequence.