# database access module for chrome to extract
# browsing history from sqlite db

import sqlite3


class ChromeExtractor(object):
    """
    History extractor for chrome sqlite db.
    """
    def __init__(self):
        super(ChromeExtractor, self).__init__()
        self._db_path = ''

    def set_path(self, path):
        pass

    def extract(self):
        try:
            self.conn = sqlite3.connect(self._db_path)
        except:
            pass
