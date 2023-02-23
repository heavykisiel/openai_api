import os
import utilities.tools
import utilities.gen
import sys
import shutil
import argparse

path = 'results/'
API_keys_selected = utilities.tools.checkApiKey()
parser = argparse.ArgumentParser(description='This program meant to generate code using openai API')
parser.add_argument('function', type=str, choices=['gen', 'del', 'engines', 'apiKey'])
parser.add_argument('-m', '--flag', type=str, )
args = parser.parse_args()

if args.function == 'gen':
        if API_keys_selected:
                utilities.gen.genCode(args.flag)
        else:
                print('API keys are not selected, try run again with command apiKey to set them.')
if args.function == 'del':
        shutil.rmtree(path)
        os.mkdir(path)
if args.function == 'engines':
        utilities.gen.engines()
if args.function == 'apiKey':
        utilities.tools.addApiKey()




