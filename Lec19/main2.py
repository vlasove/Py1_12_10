import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-x", "--xarg", help="x value for calc", type=int) # --x - означает, что x - опциональный аргумент
parser.add_argument("-y", "--yarg", help="y value for calc", type=int)

args = parser.parse_args()


print(args)
if args.xarg is None and args.yarg is None:
    args.xarg ,args.yarg = 1, 1
elif args.xarg is None and args.yarg is not None:
    args.xarg = 1
elif args.yarg is None and args.xarg is not None:
    args.yarg = 1

print("Answer:",(args.xarg + args.yarg)**2)