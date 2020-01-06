import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--member", type=int, help="member")
args = parser.parse_args()

print(args.member)
