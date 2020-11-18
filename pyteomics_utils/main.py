import argparse
import logging
from . import fasta
try:
    from . import pepxml
except ImportError:
    pepxml = None


def main():
    common_parser = argparse.ArgumentParser(add_help=False)
    common_parser.add_argument('-v', '--verbosity', choices=range(3), type=int, default=1,
        help='Output verbosity')
    io_parser = argparse.ArgumentParser(add_help=False)
    io_parser.add_argument('files', nargs='*', help='Input files to process. If none given, read standard input.')
    io_parser.add_argument('-o', '--output', nargs='?', help='Output file name. Default is stdout.')

    parent_dict = {'common': common_parser, 'io': io_parser}
    main_parser = argparse.ArgumentParser(parents=[common_parser])

    levels = [logging.WARNING, logging.INFO, logging.DEBUG]

    modules = main_parser.add_subparsers()
    fasta.register_commands(modules, parent_dict)
    pepxml.register_commands(modules, parent_dict)

    args = main_parser.parse_args()

    logging.basicConfig(format='%(levelname)8s: %(asctime)s %(message)s',
                        datefmt='[%H:%M:%S]', level=levels[args.verbosity])
    logger = logging.getLogger(__name__)
    logger.debug('Received args in main: %s', args)
    args.func(args)
