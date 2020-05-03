from hypothesis import given
import hypothesis.strategies as st
from utils import Finder


@given(st.lists(st.permutations(["a", "b", "c", "d", "e"]), min_size=3, max_size=1000))
def test_all_anagrams(chars):
    lst = list(map(lambda l: "".join(l), chars))
    finder = Finder(lst)
    result = set(finder.find(lst[0]))
    assert set(lst) == set(result)


@given(st.lists(st.just("abc"), min_size=3, max_size=1000))
def test_all_same(lst):
    finder = Finder(lst)
    result = set(finder.find(lst[0]))
    assert set(lst) == set(result)


@given(st.lists(st.just(""), min_size=3, max_size=1000))
def test_all_empty(lst):
    finder = Finder(lst)
    result = set(finder.find(lst[0]))
    assert set(lst) == set(result)
