# Welcome to Pytisto
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
it is a very simple and very fast python test runner.
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
- fill it with ```assert_equals()``` or ```assert_not_equals```
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

|number of tests| ```Pytisto```|```unittest```  |```codewars_test```|
|---------------|--------------|----------------|-------------------|
| 3             | 0.00006008 s | 0.0000059605 s | 0.02 s            |
| 10,003        | 0.003 s      | 0.010 s        | 90.11 s           |
| 10,000,003    | 8.238 s      | 9.124 s        | 87987.96          |

even tho python's builtin ```unittest``` framework wins by a very small amount in the 3 tests, ```Pytisto``` wins in all the others!

**these benchmarks are inconsistent, so you may find different results (I don't think the difference may be bigger then a second)*