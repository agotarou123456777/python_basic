import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--num', type=float, default=10)
parser.add_argument('--choice', type=str, default='choice', choices=['A', 'B', 'C'])
args = parser.parse_args()

print(args.num)
print(args.choice)