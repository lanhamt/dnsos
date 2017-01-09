# parser to make urls ready to dns resolve

from urlparse import urlparse


class DomainParser(object):
    """
    parses urls to make ready for dns resolve
    """
    def __init__(self):
        super(DomainParser, self).__init__()

    def parse_url(self, url):
        """
        Parses given url and checks if a valid network
        location exists; if so returns the netloc.
        """
        result = urlparse(url)
        if result.netloc:
            return result.netloc
        else:
            return None
