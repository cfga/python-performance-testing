import pytest

from utils import Finder
import utils.benchmarking.data as td

test_data_sets = [td.TEST_LIST_10, td.TEST_LIST_100, td.TEST_LIST_1000, td.TEST_LIST_10000]


@pytest.mark.benchmark(group="Access last element")
@pytest.mark.parametrize("test_data", test_data_sets)
def test_access_last(benchmark, test_data):
    finder = Finder(test_data)
    test_data_last = test_data[-1]
    benchmark(finder.find, test_data_last)


@pytest.mark.benchmark(group="Access first element")
@pytest.mark.parametrize("test_data", test_data_sets)
def test_access_first(benchmark, test_data):
    finder = Finder(test_data)
    test_data_head = test_data[0]
    benchmark(finder.find, test_data_head)


@pytest.mark.benchmark(group="Access element in the middle")
@pytest.mark.parametrize("test_data", test_data_sets)
def test_access_middle(benchmark, test_data):
    finder = Finder(test_data)
    test_data_mid = test_data[len(test_data) // 2]
    benchmark(finder.find, test_data_mid)


@pytest.mark.benchmark(group="Access nonexistent element")
@pytest.mark.parametrize("test_data", test_data_sets)
def test_access_nonexistent(benchmark, test_data):
    el = "".join(sorted(test_data[0]))
    clean_list = list(filter(lambda s: ("".join(sorted(s)) != el), test_data))
    finder = Finder(clean_list)
    benchmark(finder.find, el)
