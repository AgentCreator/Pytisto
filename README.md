# Welcome to Pytisto <img src="logo.png" width="50"/></img>

```python
from pytisto import *
tests([
        test_group(
            "example",
            [
                assert_equals(1+1, 2, "hello"),
            ]
        ),
        test_group(
            "example2",
            [
                assert_equals(1+2, 3)
            ]
        ),
        test_group(
            "random",
            [
                assert_equals(1+3, 3, "wow you suck"),
                assert_equals(1+3, 3),
            ]
        )
    ])
```
What is Pytisto?
===
it is a very simple, very minimalist and very fast python test runner.
I will try to update it daily.

> FUN FACT 💡: tisto means "dough" in Ukrainian
## it is a very simple test runner
- import pytisto.
```python
from pytisto import *
```
- initialize the tests.
```python
from pytisto import *

tests([
#     tests will go here
])
```
- create a test group
```python
from pytisto import *

tests([
    test_group("name of the test group", [
        
    ])
])
```
- fill it with ```assert_equals()``` or ```assert_not_equals()``` or whatever else
```python
from pytisto import *

tests([
    test_group("name of the test group", [
        assert_not_equals(2+32, 4, "a message in case of a failure"),
        assert_equals(2+2, 4, "you broke reality")
    ])
])
```
- just run the program.
```

                       TESTS                        

name of the test group:
  \/ passed
  \/ passed

                      SUMMARY                       

tasks: 2
passed tests: 2
failed tests: 0
failed groups: 
rate: 100.00%
```
# **that's it!**
if you'll have a lot of tests, and you only want to see which failed, you can pass in an argument "onlyfails"
```commandline
python3 tests.py onlyfails
```

## it is a fast test runner

here are benchmarks:

| number of tests | ```Pytisto``` | ```unittest``` | ```codewars_test``` |
|-----------------|---------------|----------------|---------------------|
| 3               | 0.00006008 s  | 0.0000059605 s | 0.02 s              |
| 10,003          | 0.003 s       | 0.010 s        | 90.11 s             |
| 10,000,003      | 8.238 s       | 9.124 s        | 87987.96 s          |

even tho python's builtin ```unittest``` framework wins by a very small amount in the 3 tests, ```Pytisto``` wins in all the others!

**these benchmarks are inconsistent, so you may find different results (I don't think the difference may be bigger then a second)*


**with the third benchmark you may get vastly different results. I have no idea why, but sometimes it is 8.238 s and 9.124 s, and sometimes it is 13.237 s and 15.197 s.*

# experimental features
pytisto has a few of new and exciting experimental features. currently there is only 1, it is **expr_tests**.
it makes your code 2 times faster (8.844 s for 10,000,000 tests) using dictionary comprehension.

to check it out just use the ```expr_tests()``` function, here is an example:
```python

from pytisto import *
from main import tru_RPS as RPS
from random import choice

expr_tests(RPS, [
        {
            (vals := (choice(["rock", "paper", "scissors"]), choice(["rock", "paper", "scissors"]))): tru_rps(*vals) for
            _ in range(10_000_000)
        }
    ])
```

# How to get started?
- clone this repo to the project you want to use it in.
- make a new file for tests (like ```tests.py```)
- that's it! you can start by copying the tutorial and enjoying 