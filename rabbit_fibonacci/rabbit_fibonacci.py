#!/usr/bin/env python3
"""
Author : loicborcard <loicborcard@localhost>
Date   : 2022-11-16
Purpose: calcultate the number of rabbits after N generations
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('-k',
                        '--int',
                        help='A named integer argument',
                        metavar='int',
                        type=int,
                        default=0)
    
    parser.add_argument('-k',
                        '--int',
                        help='A named integer argument',
                        metavar='int',
                        type=int,
                        default=0)

    parser.add_argument('-f',
                        '--file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-o',
                        '--on',
                        help='A boolean flag',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    str_arg = args.arg
    int_arg = args.int
    file_arg = args.file
    flag_arg = args.on
    pos_arg = args.positional

    print(f'str_arg = "{str_arg}"')
    print(f'int_arg = "{int_arg}"')
    print('file_arg = "{}"'.format(file_arg.name if file_arg else ''))
    print(f'flag_arg = "{flag_arg}"')
    print(f'positional = "{pos_arg}"')
    
    def rabbits(N,k):
        memo = {}
    args = (N,k)
    if args in memo:
        return(memo[args])
    for i in range(1,N+1):
        # print(i)
        
        if i == 1:
            past = {i:  1}
        elif i == 2:
            past[i] = 1
        else:
            past[i] = past[i-1] + past[i-2]*k
            
    print(past[N])  

# --------------------------------------------------
if __name__ == '__main__':
    main()
