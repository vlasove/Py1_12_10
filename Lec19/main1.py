import argparse

parser = argparse.ArgumentParser()
parser.add_argument("x", help="x value for calc", type=int)
parser.add_argument("y", help="y value for calc", type=int)

args = parser.parse_args()

print(args)
print("Answer:", (args.x + args.y)**2)