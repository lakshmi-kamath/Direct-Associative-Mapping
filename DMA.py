class CacheLine:
    def __init__(self, valid=False, tag=None, data=None):
        self.valid = valid
        self.tag = tag
        self.data = data  #write-through

class ParacacheSimulator:
    def __init__(self, cache_size_bytes, main_mem_size_bytes, offset_bits):
        self.cache_size_bytes = cache_size_bytes
        self.main_mem_size_bytes = main_mem_size_bytes
        self.offset_bits = offset_bits
        self.cache_lines = [CacheLine() for _ in range(cache_size_bytes // 4)]
        self.index_bits = self._calculate_index_bits()
        self.tag_bits = 11 - (self.offset_bits + self.index_bits)
        self.index_mask = (1 << self.index_bits) - 1
        self.total_accesses = 0
        self.total_misses = 0
        self.total_hits = 0

    def _calculate_index_bits(self):
        return (self.cache_size_bytes // 4).bit_length() - 1

    def simulate_access(self, address, write=False, data=None):
        self.total_accesses += 1

        address_binary = format(address, '011b')  
        offset = int(address_binary[-self.offset_bits:], 2)
        index = (address >> self.offset_bits) & self.index_mask
        tag = address >> (self.offset_bits + self.index_bits)

        cache_line = self.cache_lines[index]

        if cache_line.valid and cache_line.tag == tag:
            self.total_hits += 1
            status = "Hit"
        else:
            self.total_misses += 1
            cache_line.valid = True
            cache_line.tag = tag
            status = "Miss"

        if write:
            cache_line.data = data  # Update cache with write-through

        print(f"\nAddress: {address_binary}, Valid: {cache_line.valid}, Tag: {format(tag, 'b')}, Index: {format(index, 'b')}, Status: {status}")
        print("Cache Details:")
        for i, line in enumerate(self.cache_lines):
            if line.valid:
                print(f"Index {i}: Valid={line.valid}, Tag={format(line.tag, 'b')}, Data={line.data if line.data is not None else 'None'}")
            else:
                print(f"Index {i}: Empty")


    def print_stats(self):
        print("\nSimulation Summary:")
        print(f"Total Memory Accesses: {self.total_accesses}")
        print(f"Total Misses: {self.total_misses}")
        print(f"Total Hits: {self.total_hits}")
        print(f"\nCacahe Details:")
        print(f"Cache Size :{cache_size} bytes")
        print(f"Offset Bits:{offset_bits}")
        print(f"Tag Bits:{self.tag_bits}")

cache_size = 32  # bytes
main_mem_size = 2048  # bytes
offset_bits = 2

cache_simulator = ParacacheSimulator(cache_size, main_mem_size, offset_bits)
addresses_to_access = [1004, 1012, 5, 3, 88, 5, 22, 490, 888, 2000, 1999]
data_to_write = [10, 20, 30, 40, 50,60,70,80,90,100,110]

for address, data in zip(addresses_to_access, data_to_write):
    cache_simulator.simulate_access(address, write=True, data=data)

cache_simulator.print_stats()