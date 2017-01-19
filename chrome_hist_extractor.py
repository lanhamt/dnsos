# database access module for chrome to extract
# browsing history from sqlite db

import sqlite3


CHROME_QUERY = "SELECT url FROM urls"


class ChromeExtractor(object):
    """
    History extractor for chrome sqlite db.
    """
    def __init__(self):
        super(ChromeExtractor, self).__init__()
        self._db_path = ''

    def set_path(self, path):
        self._db_path = path

    def extract(self, output_file):
        try:
            self._conn = sqlite3.connect(self._db_path)
            self._cur = self._conn.cursor()
            urls_query = self._cur.execute(CHROME_QUERY)
            for url in urls_query:
                output_file.write(url)
        except:
            pass  # "Unable to connect. Make sure that your browser is closed."
