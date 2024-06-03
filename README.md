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
it is a very simple and a very fast python test runner.
### get started
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