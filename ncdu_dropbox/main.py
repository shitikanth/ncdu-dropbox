import argparse
import os

from ncdu_dropbox.dirtree import DirTreeBuilder
from ncdu_dropbox.dropboxfetcher import DropboxFetcher
from ncdu_dropbox.ncduwriter import NcduWriter


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', nargs='?', default='', help='Path of directory to scan. Leave empty for entire Dropbox.')
    parser.add_argument('-t', '--token', help='Dropbox API Token. You can also provide the token by setting '
                                        'the DROPBOX_TOKEN environment variable.')
    parser.add_argument('-o', '--output', dest='writer', metavar='FILE', help='Write output to FILE.',
                        type=argparse.FileType('w'), default='-')
    args = parser.parse_args()

    token = args.token or os.environ.get('DROPBOX_TOKEN')
    if not token:
        exit(parser.print_help())

    path = args.path
    if path and not path.startswith('/'):
        path = '/' + path

    fetcher = DropboxFetcher(token)
    entries = fetcher.list(path)

    builder = DirTreeBuilder(path)
    dir_tree = builder.build(entries)

    exporter = NcduWriter(args.writer)
    exporter.export(dir_tree)


if __name__ == '__main__':
    main()