### Tests and linter status:
[![Actions Status](https://github.com/Deln0r/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/Delnor/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/f7cbfec6c082003cfec9/maintainability)](https://codeclimate.com/github/Deln0r/python-project-50/maintainability)

### Description

# Parallel Cloud Downloader
This program, written in Python, allows downloading files from cloud storage in three different ways - using multithreading, multiprocessing, and a hybrid approach (asyncio module). I conducted tests on a MacBook i5/16GB while downloading ten files ranging from 500KB to 3MB in size. The results for multithreading were as follows: 1 thread - 20 seconds, 5 threads - 6 seconds, 10 threads - 4 seconds. For multiprocessing, the results were: 5 processes - 5 seconds, 10 processes - 3 seconds. Using the asyncio module, I achieved the best results: 5 tasks - 4 seconds, 10 tasks - 2 seconds.
