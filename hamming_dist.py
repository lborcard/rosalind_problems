#!/usr/bin/env python3
"""
Author : loicborcard <loicborcard@localhost>
Date   : 2022-11-05
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():


    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='str',
                        help='A positional argument')


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


    print('file_arg = "{}"'.format(file_arg.name if file_arg else ''))



# --------------------------------------------------
if __name__ == '__main__':
    main()
