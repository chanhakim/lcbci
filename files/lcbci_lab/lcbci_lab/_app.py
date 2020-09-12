"""
a cli app for lcbci_lab. helps with debugging and opening files quickly.
"""

import os
import argparse

def _parser():
    """Parses objects and returns a argparse parser object."""
    parser = argparse.ArgumentParser()
    exclusive = parser.add_mutually_exclusive_group(required=False)

    exclusive.add_argument('--application', '-a',
        action='store_true',
        help='Opens lcbci application.')
    exclusive.add_argument('--build', '-b',
        action='store_true',
        help='Reinstalls the package.')
    exclusive.add_argument('--source', '-s',
        type=str,
        default=None,
        help='Opens a source file.')

    return parser.parse_args()

def main():

    args = _parser()

    if args.application == False and args.build == False and args.source == None:
        os.system('/opt/anaconda3/bin/python /Users/chanhakim/Google\ Drive/RAISE/lcbci/files/lcbci_lab/lcbci_lab/lcbci_lab.py')
        # app = lcbci_lab()
        # app.start_gui()

    elif args.application == True:
        os.system('/opt/anaconda3/bin/python /Users/chanhakim/Google\ Drive/RAISE/lcbci/files/lcbci_lab/lcbci_lab/lcbci_lab.py')
        # app = lcbci_lab()
        # app.start_gui()

    elif args.build == True:
        os.system('cd /Users/chanhakim/Google\ Drive/RAISE/lcbci/files/lcbci_lab && poetry build && pip install --user dist/lcbci_lab-0.1.0.tar.gz')

    elif args.source != None:
        path = '/Users/chanhakim/Google\ Drive/RAISE/lcbci/files/lcbci_lab/lcbci_lab'
        if args.source == 'widgets': os.system('subl {}/_widgets.py'.format(path))
        if args.source == 'backend': os.system('subl {}/_backend.py'.format(path))
        if args.source == 'lab': os.system('subl {}/lcbci_lab.py'.format(path))
        if args.source == 'app': os.system('subl {}/_app.py'.format(path))
        os.system('subl ')
