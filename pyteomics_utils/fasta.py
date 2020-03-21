import logging
from pyteomics import fasta
logger = logging.getLogger(__name__)


def decoy(args):
    logger.debug('decoy called with: %s', args)
    fasta.write_decoy_db(mode=args.mode, keep_nterm=args.keep_nterm, keep_cterm=args.keep_cterm,
        prefix=args.prefix, decoy_only=args.decoy_only)


def register_commands(subparsers, parents=[]):
    fasta_parser = subparsers.add_parser('fasta', parents=parents)
    fasta_commands = fasta_parser.add_subparsers()
    fasta_decoy = fasta_commands.add_parser('decoy', parents=parents,
        description='Read a FASTA file from standard input, write a FASTA with decoys to standard output.')
    fasta_decoy.set_defaults(func=decoy)
    fasta_decoy.add_argument('-m', '--mode', choices=fasta._decoy_functions.keys(), default='reverse')
    fasta_decoy.add_argument('--keep-nterm', action='store_true', help='Keep N-terminal residue in decoy sequences')
    fasta_decoy.add_argument('--keep-cterm', action='store_true', help='Keep C-terminal residue in decoy sequences')
    fasta_decoy.add_argument('-p', '--prefix', default='DECOY_', help='Decoy prefix')
    fasta_decoy.add_argument('--decoy-only', action='store_true', help='Do not include original sequences in output')
