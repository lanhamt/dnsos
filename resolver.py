# resolver module for dns queries

import dns.resolver


class Resolver(object):
    """
    resolver for dns queries
    """
    def __init__(self):
        super(Resolver, self).__init__()
        self._name_set = set()
        self._resolved_set = dict()

    def add_domain(self, url):
        """
        Adds a parsed url to the name set
        to be resolved.
        """
        self._name_set.add(url)

    def resolve_domains(self):
        """
        For each name in name set, resolves name and adds
        the answers for that name to the resolved set where
        key is the domain name, and value is a list of the
        answer IP addresses.
        """
        for name in self._name_set:
            try:
                answer = dns.resolver.query(name)
                self._resolved_set[name] = [str(rec) for rec in answer]
            except:
                pass
