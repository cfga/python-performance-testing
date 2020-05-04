import random
import string


def gen_random_string():
    return "".join(random.choices(string.ascii_letters + string.digits, k=30))


TEST_LIST_10 = [gen_random_string() for _ in range(10)]

TEST_LIST_100 = [gen_random_string() for _ in range(100)]

TEST_LIST_1000 = [gen_random_string() for _ in range(1000)]

TEST_LIST_10000 = [gen_random_string() for _ in range(10000)]
