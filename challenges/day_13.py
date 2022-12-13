from functions_day_13 import *

# challenge 1:
signal_pairs = parse_pairs('../input_files/input_day_13.txt')
is_in_order = check_order_pairs(signal_pairs)

print("Sum of right order indices:")
print(sum(np.argwhere(is_in_order) + 1))

# challenge 2:
packets = parse_pairs_v2('../input_files/input_day_13.txt')
packets.append([[2]])
packets.append([[6]])
reordered = reorder_packets(packets)

decoder_1 = reordered.index([[2]]) + 1
decoder_2 = reordered.index([[6]]) + 1

print("Decoder key")
print(decoder_1 * decoder_2)