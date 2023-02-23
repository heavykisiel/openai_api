import os
import utilities.tools
import utilities.gen
import sys
import shutil
import argparse

path = 'results/'

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('function', type=str)
parser.add_argument('-f', '--flag', type=str)
args = parser.parse_args()

utilities.gen.get_cfg()

# if args.function == 'gen':
#         utilities.gen.genCode(args.flag)
# if args.function == 'del':
#         shutil.rmtree(path)
#         os.mkdir(path)
# if args.function == 'engines':
#         utilities.gen.engines()





