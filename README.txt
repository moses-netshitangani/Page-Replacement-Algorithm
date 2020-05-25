The output of each algorithm gives the final state of the 
main memory (which pages are left in memory) and the number 
of page faults incurred.

This program can be used in the following ways:

1. python paging.py frame_size

- This creates a random sequence of pages within the program, 
which is then applied to the three algorithms, using the 
specified frame_size.

EXAMPLE:	python paging.py 3


2. python paging.py frame_size sequence_length 

- This does the same thing as above, but instead of a random 
page sequence length, the value in the parameter sequence_length 
is used to determine the length of the random sequence.

EXAMPLE:	python paging.py 4 20


3. python paging.py frame_size page_sequence

- This refrains from creating a random sequence of pages, and instead 
uses a user-specified page sequence. The page_sequence parameter should 
be a square-bracket enclosed and comma-separated list.

EXAMPLE:	python paging.py 4 [1,2,3,7,3,5]


NB: When using ssh to test if the program ran, I found that it ran with python v3.
So you would replace 'python paging.py' with 'python3 paging.py'. Thank you.