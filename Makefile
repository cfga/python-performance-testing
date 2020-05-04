test:
	pytest  --hypothesis-show-statistics .

bench:
	pytest --benchmark-warmup-iterations=10000 --benchmark-min-rounds=5 --benchmark-warmup="on" --benchmark-calibration-precision=1000 --benchmark-columns="min, max, mean, stddev, median, outliers, rounds, iterations" **/benchmarking/**

install:
	pip3 install -e .
