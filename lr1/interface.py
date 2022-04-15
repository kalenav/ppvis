import argparse
import os
import sys

parser = argparse.ArgumentParser(description='input smth idk')
parser.add_argument("String", metavar="string", type=str, help="the string, duh")
args = parser.parse_args()
string = args.String
print("you've entered this: " + string)