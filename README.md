Both the files contain the Python code for a Paracache Simulator following Direct Associative Mapping with a write through Policy.
The Cache and Memory details are:
Memory Size: 2K bytes =>Instruction length= 11 bits
Cache Size: 32 bytes =>Index bits = 3 bits
Block Size: 4 bytes => Offset Bits=2 bits
Tag Bits= 11-(3+2) = 6 bits

Approach 1:
The DMA.py file contains the code for the approach wherein we conventionally see the index bits and map the Main Memory to its respective Cache Line.

Approach 2:
The assignment.py file contains the code for the approach wherein the Memory adress mod no_of_cache_blocks gives the index of the cache line.

In both the policies at the end the total number of memory accesses, hits and misses are printed on the output screen. The adresses are hardcoded and the cache keeps updating with the help of Write Through Policy.
