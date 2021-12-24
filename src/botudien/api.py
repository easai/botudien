"""Classes for botudien API

"""
import requests


API_URL = "https://botudien.pythonanywhere.com/api"


class Sana():
    """Class for a dictonary entry.

    This is a class for a record structure for the botudien dictionary.

    Attributes:
        exp (string): the word
        desc (string): the description of the word

    """

    def __init__(self, rec):
        """Constructor.

        Args:
            rec(dictionary): string in json format

        """
        self.exp = rec['vi']
        self.desc = rec['en']

    def dump(self):
        """Print formatted record.
        """
        print(f"[{self.exp}] means [{self.desc}]")

    def test():
        print("test")


class Botudien():
    """Class for botudien dictonary.

    This is a class for the botudien dictionary.

    Attributes:
        url (string): the server url

    """

    def __init__(self, url=None, is_local=False):
        """Constructor.

        Args:
            lst(string): server url
        """
        self.url = API_URL
        if is_local:
            self.url = "http://localhost:5000/api"

    def lookup(self, lang, word):
        """Retrieve records with expression WORD.
        """
        req = requests.get(f"{self.url}/lookup/{lang}/{word}")
        return req.json()

    def rand(self):
        """Obtain a random entry.
        """
        r = requests.get(self.url + "/rand")
        return r.json()

    def nrand(self, n):
        """Obtain n random entry.
        """
        r = requests.get(f"{self.url}/nrand/{n}")
        return r.json()

    def dump(self, lst):
        """Print formatted list of records.

        Args:
            lst(list): list of Sana objects
        """
        for item in lst:
            item.dump()
