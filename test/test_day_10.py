from functions_day_10 import *


def test_parse_instructions():
    signals = parse_instructions('input_files/input_day_10_baby_example.txt')
    print(signals)

    assert (signals == [1, 1, 1, 4, 4, -1])
    assert (signals[5-1] == 4)


def test_compute_score():
    signals = parse_instructions('input_files/input_day_10_example.txt')
    score = compute_signal_strength(signals, positions=[20, 60, 100, 140, 180, 220])

    assert (score == 13140)


def test_crt():
    signals = parse_instructions('input_files/input_day_10_example.txt')
    CRT = make_crt_image(signals)
    np.savetxt("test/CRT_example.txt", CRT,  fmt="%s")
    # read input file
    fin = open("test/CRT_example.txt", "rt")
    # read file contents to string
    data = fin.read()
    # replace all occurrences of the required string
    data = data.replace('b', '')
    data = data.replace('\'', '')
    data = data.replace(' ', '')
    # close the input file
    fin.close()
    # open the input file in write mode
    fin = open("test/CRT_example.txt", "wt")
    # overwrite the input file with the resulting data
    fin.write(data)
    # close the file
    fin.close()



