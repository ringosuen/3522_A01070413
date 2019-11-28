"""
Main driver class to run the program from the terminal.
"""
import argparse

parser = argparse.ArgumentParser()
# parser.add_argument("pokemon", help="enter the pokemon you want to see")
parser.add_argument("move", help="enter the move(s) you want to see")
parser.add_argument("--m", "--move", help="enter the move(s) you want to see")

parser.add_argument("-s", "--string", help="The string of moves")
args = parser.parse_args()
print(args.move)