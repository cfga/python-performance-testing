# Requirements

- Python >=3.7
- make

# Setting up the environment

This project uses [virtualenv](https://docs.python.org/3.7/tutorial/venv.html) to isolate the environment in which 
it is being run.

For instance, on MacOS, you would have to run:

```bash
$ python3 -m venv test-venv
$ source test-venv/bin/activate
```

Mind the necessity of using a different activation script, see `ls test-venv/bin`.

# Installing

This project uses setuptools. To install it in-place:

`make install`

This will run a pip3 command to install the library in-place, along with its dependencies.

# Run tests
The tests are written using property-based testing library (Hypothesis)[https://hypothesis.readthedocs.io/en/latest/]. To run the tests:

`make test`

# Run benchmarks

Benchmarking is done with (pytest-benchmark)[https://pytest-benchmark.readthedocs.io/en/latest/] library. To run the benchmarks:

`make bench`
