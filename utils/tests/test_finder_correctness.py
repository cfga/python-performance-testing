from hypothesis import given
import hypothesis.strategies as st
from random import choice
from utils import Finder


@given(st.lists(st.text(min_size=3, max_size=1000), min_size=3, max_size=1000))
def test_exists(lst):
    el = "".join(sorted(choice(lst)))
    in_list = set(filter(lambda s: ("".join(sorted(s)) == el), lst))
    finder = Finder(lst)
    result = set(finder.find(el))
    assert in_list == result


@given(st.lists(st.text(min_size=3, max_size=1000), min_size=3, max_size=1000))
def test_not_exists(lst):
    el = "".join(sorted(lst[0]))
    clean_list = list(filter(lambda s: ("".join(sorted(s)) != el), lst))
    finder = Finder(clean_list)
    result = finder.find(el)
    assert [] == result
