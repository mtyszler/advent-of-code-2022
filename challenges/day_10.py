from functions_day_10 import *

# challenge 1:
signals = parse_instructions('../input_files/input_day_10.txt')
CRT = make_crt_image(signals)
np.savetxt("CRT.txt", CRT,  fmt="%s")
# read input file
fin = open("CRT.txt", "rt")
# read file contents to string
data = fin.read()
# replace all occurrences of the required string
data = data.replace('b', '')
data = data.replace('\'', '')
data = data.replace(' ', '')
# close the input file
fin.close()
# open the input file in write mode
fin = open("CRT.txt", "wt")
# overwrite the input file with the resulting data
fin.write(data)
# close the file
fin.close()
print("Open CRT.txt")
