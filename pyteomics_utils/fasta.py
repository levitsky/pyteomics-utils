from pyteomics import fasta

def decoy(args):
    print('decoy called with:', args)

def register_commands(subparsers):
    fasta_parser = subparsers.add_parser('fasta')
    fasta_commands = fasta_parser.add_subparsers()
    fasta_decoy = fasta_commands.add_parser('decoy')
    fasta_decoy.set_defaults(func=decoy)