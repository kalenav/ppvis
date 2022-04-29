import argparse
from UIclass import UI
from file_reader import FileReader
from file_writer import FileWriter
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'examples\\pa1.txt')
fr = FileReader(filename)
playarea = fr.readPlayareaFromFile()

ui = UI()

parser = argparse.ArgumentParser(description='Railroad simulation')
subparsers = parser.add_subparsers()
parser_printState = subparsers.add_parser('print', help='Print current playarea state')
parser_printState.set_defaults(func=ui.printPlayareaState)

args = parser.parse_args()
args.func(playarea)

fw = FileWriter(filename, playarea)
fw.writePlayareaToFile()