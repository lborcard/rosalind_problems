#!/usr/bin/env python3
"""
Author : loicborcard <loicborcard@localhost>
Date   : 2022-11-19
Purpose: find pattern in a DNA sequence
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('-f',
                        '--file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)


    return parser.parse_args()


# --------------------------------------------------
def main():
    """find the number of occurences in a dna string"""

    args = get_args()
    file_arg = args.file
    
    dna_str = file_arg.readline().rstrip('\n')
    pat = file_arg.readline().rstrip('\n') # rstrip('\n') remove the newline at each line
    print(dna_str,pat)
    
    # lengths of the motif and the dna string
    k = len(pat)
    s = len(dna_str)
    # store the position of the pattern
    pos = []
    
    for i in range(0,s):
        cur_str = dna_str[i:k+i]
        if cur_str == pat:
            # take the position where the motif is found
            pos.append(str(i+1))
            
    print(" ".join(pos))




# --------------------------------------------------
if __name__ == '__main__':
    main()
