import argparse

# Args
parser = argparse.ArgumentParser(description='An argparse demo.')
parser.add_argument('-e', '--env', choices=['prod', 'staging', 'test'], help='An environment', required=True)
parser.add_argument('-n', '--name', help='A users name', required=True)
args = parser.parse_args()


print(f"This program will setup {args.name} in the {args.env} environemnt.")
