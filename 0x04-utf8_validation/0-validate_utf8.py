#!/usr/bin/env python3

def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the leading bits
    mask1 = 1 << 7
    mask2 = 1 << 6

    # Iterate over each byte in the data
    for byte in data:
        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte & mask1) == 0:
                continue
            elif (byte & (mask1 >> 1)) == 0:
                num_bytes = 1
            elif (byte & (mask1 >> 2)) == 0:
                num_bytes = 2
            elif (byte & (mask1 >> 3)) == 0:
                num_bytes = 3
            else:
                return False

            # Invalid scenario for the first byte
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check if the current byte is a valid continuation byte
            if (byte & mask1) == 0 or (byte & mask2) != 0:
                return False

        num_bytes -= 1

    # All characters should be fully processed
    return num_bytes == 0
