import logging
from pyteomics import fasta
import os
from . import utils
logger = logging.getLogger(__name__)


@utils.multiple_files(lambda name: logger.info('Processing %s', name))
def decoy(args):
    """Generate a decoy database"""
    logger.debug('decoy called with: %s', args)
    fasta.write_decoy_db(args.file, args.output,
        mode=args.mode, keep_nterm=args.keep_nterm, keep_cterm=args.keep_cterm,
        prefix=args.prefix, decoy_only=args.decoy_only)


@utils.multiple_files()
def describe(args):
    """Read database and produce a summary"""
    logger.debug('describe called with: %s', args)
    try:
        dlist = [d for d, seq in fasta.read(args.file)]
    except Exception as e:
        logger.info('Not a valid FASTA file.')
        logger.debug('Exception: %s', e)
    else:
        logger.info('Found %s FASTA entries.', len(dlist))
        n = len(dlist)
        if n:
            logger.debug('First entry: %s', dlist[0])
            if n > 2:
                dlist.sort()
                prefix_1 = os.path.commonprefix(dlist[:n // 2])
                prefix_2 = os.path.commonprefix(dlist[n // 2 + 1:])
                if prefix_1 != prefix_2:
                    logger.info('Common prefixes: %s, %s', prefix_1, prefix_2)
                else:
                    logger.info('Common prefix: %s', prefix_1)
            formats = []
            for flavor in fasta.std_parsers:
                try:
                    fasta.parse(dlist[0], flavor=flavor)
                except Exception as e:
                    logger.debug('Header: %s; parsing exception: %s', dlist[0], e)
                else:
                    formats.append(flavor)
            k = len(formats)
            if not k:
                logger.info('Unknown header format.')
            elif k == 1:
                logger.info('Suggested header format: %s', formats[0])
            else:
                logger.info('Possible header formats: %s', ', '.join(formats))


def register_commands(subparsers, parents):
    fasta_parser = subparsers.add_parser('fasta')
    fasta_commands = fasta_parser.add_subparsers()

    fasta_decoy = fasta_commands.add_parser('decoy', parents=[parents['common'], parents['io']],
        description='Read a FASTA file from standard input, write a FASTA with decoys to standard output.')
    fasta_decoy.set_defaults(func=decoy)
    fasta_decoy.add_argument('-m', '--mode', choices=fasta._decoy_functions.keys(), default='reverse')
    fasta_decoy.add_argument('--keep-nterm', action='store_true', help='Keep N-terminal residue in decoy sequences')
    fasta_decoy.add_argument('--keep-cterm', action='store_true', help='Keep C-terminal residue in decoy sequences')
    fasta_decoy.add_argument('-p', '--prefix', default='DECOY_', help='Decoy prefix')
    fasta_decoy.add_argument('--decoy-only', action='store_true', help='Do not include original sequences in output')

    fasta_describe = fasta_commands.add_parser('describe', parents=[parents['common'], parents['io']],
        description='Read a database and produce a short description.')
    fasta_describe.set_defaults(func=describe)
