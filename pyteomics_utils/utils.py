import logging
import sys
from pyteomics import auxiliary as aux
from copy import copy

logger = logging.getLogger(__name__)


def default_fname_formater(fname):
    logging.info('File: %s', fname)


def multiple_files(fname_formatter=default_fname_formater):
    def wrapper(func):
        def wrapped(args):
            with aux._file_obj(args.output, 'w') as out:
                arguments = copy(args)
                arguments.output = out
                if not arguments.files:
                    arguments.file = sys.stdin
                    func(arguments)
                else:
                    for f in args.files:
                        arguments.file = f
                        fname_formatter(f)
                        func(arguments)
        return wrapped
    return wrapper
