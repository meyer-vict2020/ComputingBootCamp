import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--foo", action="append", help="foo help")
args = parser.parse_args()

print(args)