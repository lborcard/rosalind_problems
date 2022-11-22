#!/usr/bin/env python3
"""
Author : loicborcard <loicborcard@localhost>
Date   : 2022-11-20
Purpose: find the consensus from a multifasta
"""

import argparse
import fasta_lib


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
    """Output the consensus sequence from a multifasta (aligned)
    and the consensus matrix 
    The sequences must of same lengths or aligned
    """
    import fasta_lib
    args = get_args()

    file_arg = args.file
    # fasta_test = fasta_lib.fasta_to_list(file_arg)
    # print("fasta_test:",fasta_test)
    fasta = []
    seq = ""
    ## open and format a fasta file
    a = True
    #TODO function to process fasta files
    while a:
        fasta_line = file_arg.readline()
        # print(fasta_line)
            
        if fasta_line == "":
            # print("appending:",seq)
            fasta.append(seq)
            # print("end of the file")
            break
        if  fasta_line[0] in "ATCG":
            seq = seq + str(fasta_line.rstrip("\n"))
            # print("sequence:", seq)
        
        if fasta_line[0] == ">":
            # print("appending:",seq)
            fasta.append(seq)
            # print(seq)
            seq = ""
            # print("header")
            
    # remove the first empty row      
    fasta = fasta[1:]   
    
    consensus = ""
    # for the final output
    final_dict = {"A": "", "C": "", "G": "", "T": ""}
    
    for i in range(len(fasta[0])):
        dict = {"A": 0, "C": 0, "G": 0, "T": 0}
        for seq in fasta:
            # print(seq[i])
            dict[seq[i]] += 1
        for key, value in dict.items():
            final_dict[key] = str(final_dict[key]) + " " + str(value)
        # take the base with the biggest representation among sequences
        cons_base = max(dict, key=dict.get)
        consensus = consensus+cons_base
    print(consensus)
    for key, value in final_dict.items():
        print(f'{key}{":"} {value}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
