from hashlib import sha256
from itertools import groupby
import logging
from typing import List, AnyStr


class Finder:
    """A simple class that supports fast lookups of anagrams among the provided strings"""

    @staticmethod
    def __calculate_str_hash(s):
        return sha256(bytes("".join(sorted(s)), encoding="utf-8")).hexdigest()

    def __init__(self, str_list: List[AnyStr]):
        """Constructs a new Finder object.

            The constructor indexes the input data, calculating the sha256 of the
            sorted list of characters of each list entry.

            Args:
                str_list (List[AnyStr]): list of the strings to index

            Returns:
                An object that enables searching for anagrams of a certain string.
            """
        grouped = groupby(str_list, self.__calculate_str_hash)
        self.index = {k: list(v) for k, v in grouped}

    def find(self, s: AnyStr) -> List[AnyStr]:
        """Looks up all anagrams of s, indexed by this Finder instance.

            Args:
                s (AnyStr): list of the string to index

            Returns:
                a list of all anagrams of s, indexed by this Finder object. In case if no
                matching anagrams were found, return empty list.
            """
        key = self.__calculate_str_hash(s)
        try:
            return self.index[key]
        except KeyError:
            logging.info(f"No anagrams found for `{s}`")
            return []
