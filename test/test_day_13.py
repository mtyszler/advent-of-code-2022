import pytest

from functions_day_13 import *


def test_parse_signals():
    signal_pairs = parse_pairs('input_files/input_day_13_example.txt')
    print("")
    print("list of pairs")
    for pair in signal_pairs:
        print(pair)


def test_check_order():
    signal_pairs = parse_pairs('input_files/input_day_13_example.txt')
    is_in_order = check_order_pairs(signal_pairs)

    assert(sum(np.argwhere(is_in_order)+1) == 13)


def test_parse_signals_v2():
    packets = parse_pairs_v2('input_files/input_day_13_example.txt')

    print()
    print("list of packets")
    for packet in packets:
        print(packet)


def test_reorder():
    packets = parse_pairs_v2('input_files/input_day_13_example.txt')
    packets.append([[2]])
    packets.append([[6]])
    reordered = reorder_packets(packets)

    print("")
    print("list of reordered packets")
    for packet in reordered:
        print(packet)


def test_decoder_key():
    packets = parse_pairs_v2('input_files/input_day_13_example.txt')
    packets.append([[2]])
    packets.append([[6]])
    reordered = reorder_packets(packets)

    decoder_1 = reordered.index([[2]])+1
    decoder_2 = reordered.index([[6]])+1

    assert (decoder_1 * decoder_2 == 140)