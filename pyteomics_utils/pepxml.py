from . import utils
try:
    from pyteomics import pepxml, auxiliary as aux
except ImportError as e:
    pepxml = None
    exception = e
else:
    exception = None
import logging

logger = logging.getLogger(__name__)
FORMAT = '%-{}s\t%+10s\t%+10s'


def _check_pepxml():
    if pepxml is None:
        logger.error('Missing dependencies for pepxml subcommand: %s', exception)


@utils.multiple_files(lambda x: None)
def show_info(args):
    with pepxml.PepXML(args.file) as f:
        psms = list(f)
        fpsms = aux.filter(psms, is_decoy=lambda x: pepxml.is_decoy(x, args.decoy_prefix), fdr=args.fdr, key=pepxml._key, )
        logger.info(args.format, args.file, len(psms), fpsms.size)


def info(args):
    _check_pepxml()
    log_format = FORMAT.format(max(len(x) for x in args.files))
    logger.info(log_format, 'File', 'Total PSMs', '{:.0%} FDR'.format(args.fdr))
    args.format = log_format
    show_info(args)


def register_commands(subparsers, parents):
    pepxml_parser = subparsers.add_parser('pepxml', parents=[parents['common']])
    pepxml_commands = pepxml_parser.add_subparsers()

    pepxml_info = pepxml_commands.add_parser('info', parents=[parents['common'], parents['io']],
        description='Apply FDR threshold and report the number of PSMs in files.')
    pepxml_info.set_defaults(func=info)
    pepxml_info.add_argument('-f', '--fdr', type=float, default=0.01, help='FDR level (between 0.0 and 1.0)')
    pepxml_info.add_argument('-p', '--decoy-prefix', default='DECOY_')
