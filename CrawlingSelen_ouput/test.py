import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--members", type=int,
                    help="how many group member")
parser.add_argument("-u", "--url",
                    help="group facebook page url")
args = parser.parse_args()
print(f'input is {args.members} url : {args.url}')
