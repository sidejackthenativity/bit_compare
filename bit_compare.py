#Compare two files bit by bit and tries to find a string of the right integer that is equivalent in both files

import argparse

parser = argparse.ArgumentParser(description='compare two files')

parser.add_argument('--integer', required=True, help='The number of bits to compare')
parser.add_argument('--file1path', required=True, help='Path to file1')
parser.add_argument('--file2path', required=True, help='Path to file2')


args = parser.parse_args()
compare_size = int(args.integer)

start_pos_data1 = 0
flag = 0


with open(args.file1path, 'rb') as file1:
    data1 = file1.read()
file1.close()

with open(args.file2path, 'rb') as file2:
    data2 = file2.read()
file2.close()

while start_pos_data1 < (len(data1)-compare_size+1):
    start_pos_data2 = 0
    while start_pos_data2 < (len(data2)-compare_size+1):
        if (data1[start_pos_data1:start_pos_data1+compare_size]==data2[start_pos_data2:start_pos_data2+compare_size]):
            print ("position in data file1: "+str(start_pos_data1))
            print ("position in data file2: "+str(start_pos_data2))
            flag = 1
            break
        else:
            start_pos_data2 += 1
    if (flag==1):
        break
    start_pos_data1 += 1
