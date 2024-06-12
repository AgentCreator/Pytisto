"""
welcome to my unit test library!
--------------------------------

it is designed to be:
    - simple
    - minimalistic
    - fast

"""
from sys import argv
from typing import Callable

args = argv[1:]

del argv


def assert_equals(real, expect, message="") -> bool | str:
    """
Returns True if the real and expectations are matched

    in case of not mathing, returns False or the message (if provided)

    """
    return is_matching if (is_matching := expect == real) else message if message else is_matching


def assert_true(statement, message="") -> bool | str:
    """
Returns True if the statement is True.

Returns False or the message you provided if the statement is False.
    """
    return statement if statement else message if message else statement


def assert_false(statement, message="") -> bool | str:
    """
Returns True if the statement is True.

Returns False or the message you provided if the statement is False.
    """
    return not statement if not statement else message if message else not statement


def assert_not_equals(real, expect, message="") -> bool | str:
    """
Returns True if the real and expectations are not matched

    in case of mathing, returns False or the message (if provided)

    """
    return is_matching if (is_matching := expect != real) else message if message else is_matching


def expect_error(task: Callable,
                 exception: __import__("typing", globals(), locals(), ["Type"], 0).Type[ZeroDivisionError],
                 message: str = "") -> str | bool:
    """
    what do you think you little bozo this function does?
    (definitely doesn't expect an error)
    btw, I don't yet know how to work with the with keyword so this code kinda sucks

    if you want to pass in values to a function, just use a lambda

    lambda: sum(10, 20)
    """
    is_passed = False
    try:
        task()
    except exception:
        is_passed = True
    return is_passed if is_passed else is_passed or message


def test_group(name: str, unit_tests: list[bool | str]) -> dict[str, list[bool | str]]:
    """
    a way to group multiple tests in a group with a name, it is required.
    """
    return {name: unit_tests}


def silent_tests(name: str, unit_tests: list[dict[str, list[bool | str]]], destroy=True) -> None:
    """
    this does the same as the tests function,
    but doesn't print out anything (unless on failure), and on failure of the tests says:
    - where the error happened
    - in which group
    - turns of your code if destroy is set to True

    these silent tests are built, so you can simply put one inside your main file,
    and it won't break anything
    """
    for i in unit_tests:
        for o in i.values():
            for y in o:
                if isinstance(y, str) or not y:
                    print(f"your silent tests have failed:\nname: {name}\ngroup: {list(i.keys())[0]}\n")
                    if destroy:
                        quit()


def tests(unit_tests: list[dict[str, list[bool | str]]]) -> None:
    """
    the main function to start the tests.
    """

    def test_test_group(oy: dict, taskies: list, failed_groupies: set, returningies: list):
        for o in list(oy.values())[0]:
            if isinstance(o, bool):
                o = bool(o)
                taskies.append(o)
                if not o:
                    failed_groupies.add(list(oy.keys())[0])
                if args == [] or (fails := args[0] != "onlyfails"):
                    if len(taskies) < 50:
                        returningies.append("  \\/ Passed" if o else "  X Failed")
                else:
                    if not o and len(taskies) < 50 or not fails:
                        returningies.append("  X Failed")
            else:
                o = str(o)
                taskies.append(False)
                if len(taskies) < 50 or not fails:
                    returningies.append(f"  X Failed: {o}")

    tasks: list[bool] = []
    failed_groups: set[str] = set()
    returnings = [f"\n {'TESTS':^50} \n"]
    for i in unit_tests:
        i = dict(i)
        returnings.append(list(i.keys())[0] + ":")
        test_test_group(i, tasks, failed_groups, returnings)

    print("\n".join(returnings))
    print(f"\n {'SUMMARY':^50} \n")
    print(f"tests: {len(tasks):,}")

    print(f"passed tests: {tasks.count(True):,}")
    print(f"failed tests: {tasks.count(False):,}")
    print(f"failed groups: {' '.join(failed_groups)}")
    del failed_groups
    print(f"rate: {tasks.count(True) / len(tasks):2.2%}")
    del tasks


del Callable
