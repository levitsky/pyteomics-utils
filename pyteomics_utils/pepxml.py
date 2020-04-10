try:
    from pyteomics import pepxml
except ImportError as e:
    pepxml = None
    exception = e
else:
    exception = None
import logging

logger = logging.getLogger(__name__)


def _check_pepxml():
    if pepxml is None:
        logger.error('Missing dependencies for pepxml subcommand: %s', exception)


def filter(files):
    _check_pepxml()
    logger.info('This function is not implemented yet.')


def register_commands(subparsers, parents):
    pepxml_parser = subparsers.add_parser('pepxml', parents=[parents['common']])
    pepxml_commands = pepxml_parser.add_subparsers()

    pepxml_filter = pepxml_commands.add_parser('filter', parents=[parents['common']],
        description='Apply FDR threshold and report the number of PSMs in files.')
    pepxml_filter.set_defaults(func=filter)
    pepxml_filter.add_argument('--fdr', type=float, default=0.01)
    pepxml_filter.add_argument('-p', '--decoy-prefix', default='DECOY_')
