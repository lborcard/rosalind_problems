#!/usr/bin/env python3
"""
Author : loicborcard <loicborcard@localhost>
Date   : 2022-11-20
Purpose: find the consensus from a multifasta
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Return the consensus from aligned sequences ',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='A multi fasta files with aligned sequences',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    file_arg = args.file
    fasta = []
    seq = str()
    ## open and format a fasta file
    n = 0
    print(file_arg.readlines())
    fasta_list = file_arg.readlines()
    
    for line in fasta_list:
        if "ATCG" in line:
            print(line.rstrip("\n"))
            seq = seq + str(line.rstrip("\n"))
            print(seq)
        if ">" or "\n" in line:
            print(line)
            fasta.append(seq.rstrip("\n"))
            seq = ""
    # for line in file_arg:
    #     # if n == 0:
    #     #     continue
    #     if ">" not in line:
    #         print(line.rstrip("\n"))
    #         seq = seq + str(line.rstrip("\n"))
    #         print(seq)
    #     else:
    #         print(line)
    #     n += 1
    print(fasta)
    fasta = fasta[1:]   
    print(fasta)
    
    consensus = ""
    final_dict = {"A": "", "C": "", "G": "", "T": ""}
    for i in range(len(fasta[0])):
        dict = {"A": 0, "C": 0, "G": 0, "T": 0}
        for seq in fasta:
            print(seq[i])
            dict[seq[i]] += 1
        for key, value in dict.items():
            final_dict[key] = str(final_dict[key]) + " " + str(value)
        print(dict)
        cons_base = max(dict, key=dict.get)
        consensus = consensus+cons_base
    print(consensus)
    for key, value in final_dict.items():
        print(f'{key}{":"} {value}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
