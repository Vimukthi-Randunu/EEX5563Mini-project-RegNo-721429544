# Initialize memory blocks
memory_blocks = [100, 500, 200, 300, 600]

# Processes and their memory requirements
process_requests = [212, 417, 112]

# Simulate Best Fit allocation
for request in process_requests:
    # Find the best fit block
    best_block = None
    best_index = -1
    for i, block in enumerate(memory_blocks):
        if block >= request and (best_block is None or block < best_block):
            best_block = block
            best_index = i

    if best_block is not None:
        # Allocate memory
        print(f"Process requesting {request} KB allocated to block of size {memory_blocks[best_index]} KB.")
        memory_blocks[best_index] -= request
    else:
        print(f"Process requesting {request} KB cannot be allocated.")

    # Print current memory state
    print(f"Updated memory blocks: {memory_blocks}")
