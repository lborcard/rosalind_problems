#!/usr/bin/env python3
"""
Author : loicborcard <loicborcard@localhost>
Date   : 2022-12-23
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('-r',
                        '--rna',
                        help='A rna string',
                        metavar='str',
                        type=str,
                        default='')


    parser.add_argument('-m',
                        '--model',
                        help='model in a text file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default="/Users/loicborcard/Documents/Bioinformatics/Projects/rosalind_problems/mrna_to_prot/codon_table.txt")


    return parser.parse_args()


# --------------------------------------------------

# load the model from the file
def load_model(file):

    model = {}
    for line in file:
        
        entry = line.split()
        # print(entry[0],entry[1])
        model[entry[0]] = entry[1]
    return(model)
## translate the rna sequence

def tranlate(rna_seq,model):
        model = load_model(model)
        prot = ""
        for base in range(0,len(rna_seq),3):
            codon = rna_seq[base:base+3]
            # print("codon:",codon,model[codon])
            if len(codon) < 3:
                break
            if model[codon] == "Stop":
                break
            prot = prot + model[codon]
        print(prot)
        
def main():
    """Make a jazz noise here"""

    args = get_args()
    rna = args.rna
    model = args.model
    
    tranlate(rna_seq=rna, model=model)






# --------------------------------------------------
if __name__ == '__main__':
    main()
