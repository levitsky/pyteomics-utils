import argparse
import logging
from . import fasta


def main():
    common_parser = argparse.ArgumentParser(add_help=False)
    common_parser.add_argument('-v', '--verbosity', choices=range(3), type=int, default=1,
        help='Output verbosity')
    main_parser = argparse.ArgumentParser(parents=[common_parser])
    levels = [logging.WARNING, logging.INFO, logging.DEBUG]

    modules = main_parser.add_subparsers()
    fasta.register_commands(modules, [common_parser])

    args = main_parser.parse_args()

    logging.basicConfig(format='{levelname:>8}: {asctime} {message}',
                        datefmt='[%H:%M:%S]', level=levels[args.verbosity], style='{')
    logger = logging.getLogger(__name__)
    logger.debug('Received args in main: %s', args)
    args.func(args)