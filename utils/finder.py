from typing import List, AnyStr
from hashlib import sha256
import logging


class Finder:
    @staticmethod
    def __calculate_str_hash(s):
        return sha256(bytes("".join(sorted(s)), encoding="utf-8")).hexdigest()

    def __init__(self, str_list: List[AnyStr]):
        """Constructs a new Finder instance.

            The constructor indexes the input data, calculating the sha256 of the
            sorted list of characters of each list entry.

            Args:
                str_list (List[AnyStr]): list of the string to index

            Returns:
                An object allowing searching for anagrams of a certain string.
            """
        index = {}
        for s in str_list:
            key = self.__calculate_str_hash(s)

            # O(1)
            current_obj = index.get(key)
            if current_obj:
                current_obj.append(s)
            else:
                index[key] = [s]
        self.index = index

    def find(self, s: AnyStr) -> List[AnyStr]:
        """Looks up all anagrams of s, indexed by this Finder instance.

            Args:
                s (AnyStr): list of the string to index

            Returns:
                a list of all anagrams of s, indexed by this Finder object. In case if no
                matching anagrams were found, return empty list.
            """
        hash = self.__calculate_str_hash(s)
        try:
            return self.index[hash]
        except KeyError:
            logging.info(f"No anagrams found for `{s}`")
            return []
