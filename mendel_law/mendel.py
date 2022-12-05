#!/usr/bin/env python3
"""
Author : loicborcard <loicborcard@localhost>
Date   : 2022-12-05
Purpose: Mendel law
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # parser.add_argument('positional',
    #                     metavar='int',
    #                     nargs= 3,
    #                     help='A positional argument')
    
    parser.add_argument("-n",
                        "--n_arg",
                        metavar="n",
                        type=int,
                        help="Number of Homozygous recessive individuals",
                        default=2)
    parser.add_argument("-k",
                        "--k_arg",
                        metavar="K",
                        type=int,
                        help="Number of Homozygous dominant individuals",
                        default=2)
    
    parser.add_argument("-m",
                        "--m_arg",
                        metavar="M",
                        type=int,
                        help="Number of heterzygous individuals",
                        default=2)


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    # pos_arg = args.positional
    # arguments
    
    k = args.k_arg 
    m = args.m_arg 
    n = args.n_arg
    
    # numbers of res and dom in total in the population
    
    res = k*0 + m*1 + n*2
    dom = k*2 + m*1 + n*0
    # total of genes in the pool
    total = dom + res
    
    # probability of each 
    print("P(dominant):",dom/total, "\nP(Recessive):",res/total)
    
    res1 = (res/total) * (res-1)/(total-1)
    dom1 = (dom/total) * (dom-1)/(total-1)
    dom2 = (res/total) * (dom)/(total-1)
    dom3 = (dom/total) * (res)/(total-1)
    
    result = round(dom1+dom2+dom3,5)
    
    
    
    # print(total)
    print(f'Probability to obtain a dominant individual = {result}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
