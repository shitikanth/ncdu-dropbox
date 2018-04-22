import dropbox
import os


class DirRecord:
    def __init__(self, name):
        self.name = name
        self.children = {}

    def __repr__(self):
        return 'Directory({})'.format(self.name)


class FileRecord:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self):
        return 'File({}, {})'.format(self.name, self.size)


def make_record(entry):
    if isinstance(entry, dropbox.files.FolderMetadata):
        return DirRecord(entry.name)
    return FileRecord(entry.name, entry.size)


class DirTreeBuilder:
    def __init__(self, path):
        if not path:
            path = "/"
        self.root_path = path
        self.dir_tree = DirRecord(path)

    def build(self, entries):
        for entry in entries:
            record = make_record(entry)
            self.insert_record(entry.path_display, record)
        return self.dir_tree

    def insert_record(self, path, record):
        walk = self.walk_from_root(path)
        cur_dict = self.dir_tree.children
        for directory in walk[:-1]:
            key = directory.lower()
            if key not in cur_dict:
                cur_dict[key] = DirRecord(directory)
            cur_dict = cur_dict[key].children
        key = walk[-1].lower()
        if key not in cur_dict:
            cur_dict[key] = record
        else:
            cur_dict[key].name = record.name

    def walk_from_root(self, path):
        walk = []
        while path != self.root_path:
            path, cur = os.path.split(path)
            walk.append(cur)
        walk.reverse()
        return walk