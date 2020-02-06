import argparse
from . import fasta

def main():
    main_parser = argparse.ArgumentParser()

    modules = main_parser.add_subparsers()
    fasta.register_commands(modules)

    args = main_parser.parse_args()
    args.func(args)