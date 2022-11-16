#!/usr/bin/env python3
"""
Author : loicborcard <loicborcard@localhost>
Date   : 2022-11-05
Purpose: Rock the Casbah
"""

import argparse
import sys

# --------------------------------------------------
def get_args():
    """ 
    obtain the distance between two sequences

    """

    parser = argparse.ArgumentParser(
        description='Obtain the hamming distance between two DNA sequences',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=sys.stdin)



    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file_arg = args.file
# when you do args.file= something you can open it with a for loop
    seqs = list()
    for line in file_arg:
        seqs.append(line)
    if (len(seqs[0]) != len(seqs[1])):
        raise "Not same length"
    seq1 = seqs[0]
    seq2 = seqs[1]
    
    score = 0
    for i in range(len(seqs[0])):
        if seq1[i] != seq2[i]:
            score += 1
    print(f'score:{score:4}')
    return(score)
    print('file_arg = "{}"'.format(file_arg.name if file_arg else ''))



# --------------------------------------------------
if __name__ == '__main__':
    main()
