import dropbox


class DropboxFetcher:
    def __init__(self, token):
        self.dbx = dropbox.Dropbox(token)

    def list(self, path):
        """Get a listing of all files and folders in Dropbox."""
        listing = self.dbx.files_list_folder(path=path, recursive=True)
        for entry in listing.entries:
            yield entry
        while listing.has_more:
            cursor = listing.cursor
            listing = self.dbx.files_list_folder_continue(cursor=cursor)
            for entry in listing.entries:
                yield entry