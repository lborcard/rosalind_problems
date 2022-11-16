#!/usr/bin/env python3
"""
Author : loicborcard <loicborcard@localhost>
Date   : 2022-11-05
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='obtain max GC content from a multifasta file',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # parser.add_argument('positional',
    #                     metavar='str',
    #                     help='A positional argument',
    #                     default='')

    # parser.add_argument('-a',
    #                     '--arg',
    #                     help='A named string argument',
    #                     metavar='str',
    #                     type=str,
    #                     default='')

    # parser.add_argument('-i',
    #                     '--int',
    #                     help='A named integer argument',
    #                     metavar='int',
    #                     type=int,
    #                     default=0)

    parser.add_argument('-f',
                        '--file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default=None)

    # parser.add_argument('-o',
    #                     '--on',
    #                     help='A boolean flag',
    #                     action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    # str_arg = args.arg
    # int_arg = args.int
    file_arg = args.file
    # flag_arg = args.on
    # pos_arg = args.positional
    dna = {}
    seq_name = []
    seqs = []
    # result = " ".join(line.strip() for line in file_arg.splitlines())
    # print(result)
    for line in file_arg:
        if ">" in line:
            name = line.strip()
            name = name.replace(">","")
            dna[name] = ""
        else:
            dna[name] = dna[name]+ line.strip()
    scores = []
    for name,seq in dna.items():
        length = len(seq)
        score = 0
        for i in seq:
            if i in "CG":
                score += 1
        scores.append((score/len(seq))*100)
        print(name,":",(score/len(seq))*100)

    print(f'max GC content :{max(scores):6}')
    # print(seq_name)          
    # print(seqs)          

    # print(f'str_arg = "{str_arg}"')
    # print(f'int_arg = "{int_arg}"')
    print('file_arg = "{}"'.format(file_arg.name if file_arg else ''))
    # print(f'flag_arg = "{flag_arg}"')
    # print(f'positional = "{pos_arg}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
