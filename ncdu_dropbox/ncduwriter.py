import json
import time

from ncdu_dropbox.dirtree import FileRecord


class NcduWriter:
    def __init__(self, writer):
        self.writer = writer

    def export(self, dir_tree):
        """Exports the directory tree to ncdu compatible file format."""
        ncdu_dict = export_to_ncdu_dict(dir_tree)
        ncdu_json = [1, 0,
                     {'progname': 'ncdu-dropbox', 'progver': '0.1', 'timestamp': int(time.time())},
                     ncdu_dict]
        json.dump(ncdu_json, self.writer)


def export_to_ncdu_dict(record):
    if isinstance(record, FileRecord):
        return {'name': record.name, 'dsize': record.size}
    else:
        return [{'name': record.name}] + [export_to_ncdu_dict(child) for child in record.children.values()]

