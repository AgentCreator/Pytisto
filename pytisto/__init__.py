"""
welcome to my unit test library!
--------------------------------

it is designed to be:
    - simple
    - minimalistic
    - fast

"""
from contextlib import contextmanager
import sys
import typing

args = sys.argv[1:]

del sys


def assert_equals(real, expect, message="") -> bool | str:
    """
    returns True if the real and expections are matched

    in case of not mathing, returns False or the message (if provided)
    
    """
    return is_matching if (is_matching := expect == real) else message if message else is_matching

def assert_true(statement, message="") -> bool | str:
    """
    returns True if the statement is True.

    returns False or the message you provided if the statement is False.
    """
    return statement if statement else message if message else statement


def assert_false(statement, message="") -> bool | str:
    """
    returns True if the statement is True.

    returns False or the message you provided if the statement is False.
    """
    return not statement if not statement else message if message else not statement


def assert_not_equals(real, expect, message="") -> bool | str:
    """
    returns True if the real and expections are not matched

    in case of mathing, returns False or the message (if provided)
    
    """
    return is_matching if (is_matching := expect != real) else message if message else is_matching





def expect_error(task: typing.Callable, values:list, exception: BaseException, message: str = ""):
    """
    what do you think you little bozo this function does?
    (defenetly doesn't expect an error)
    btw, I don't yet know how to work with the with keyword so this code kinda sucks
    """
    try:
        task(values)
    except exception:
        return True
    return message if message else False


def test_group(name: str, unit_tests: list[bool | str]) -> dict[str, list[bool | str]]:
    """
    a way to group multiple tests in a group with a name, it is required.
    """
    return {name: unit_tests}



def silent_tests(name: str, unit_tests: list[dict[str, list[bool | str]]], destroy=True) -> None:
    """
    this does the same as the ```tests``` function,
    but doesn't print out anything (unless on failure), and on failure of any of the tests says:
    - where the error happened
    - in which group
    - turns of of your code if ```destroy``` is set to ```True```

    these silent tests are built so you can simply put one inside of your main file
    and it won't break anything
    """
    for i in unit_tests:
        for o in i.values():
            # print(o)
            for y in o:
                if isinstance(y, str) or not y:
                    print(f"""
your silent tests have failed:
name: {name}\ngroup: {list(i.keys())[0]}\n""")
                    if destroy:
                        __import__("sys", globals(), locals(), ["exit"], 0).exit()


def test_test_group(i: dict, tasks: list, failed_groups: set, returnings: list):
    """
    as the name implies, tests a test group.
    """
    for o in list(i.values())[0]:
        if isinstance(o, bool):
            o = bool(o)
            tasks.append(o)
            if not o:
                failed_groups.add(list(i.keys())[0])
            if args == [] or (fails := args[0] != "onlyfails"):
                if len(tasks) < 50:
                    returnings.append("  \\/ passed" if o else "  X failed")
            else:
                if not o and len(tasks) < 50 or not fails:
                    returnings.append("  X failed")
        else:
            o = str(o)
            tasks.append(False)
            if len(tasks) < 50 or not fails:
                returnings.append(f"  X failed: {o}")
    return failed_groups, returnings

def tests(unit_tests: list[dict[str, list[bool | str]]]) -> None:
    """
    the main function to start the tests.
    """
    tasks: list[bool] = []
    failed_groups: set[str] = set()
    returnings = []
    returnings.append(f"\n {'TESTS':^50} \n")
    for i in unit_tests:
        i = dict(i)
        returnings.append(list(i.keys())[0] + ":")
        add_failed_groups, add_returnings = test_test_group(i, tasks, failed_groups, returnings)
        # tasks.append(add_tasks)
        failed_groups = failed_groups ^ add_failed_groups
        returnings+= add_returnings
    print("\n".join(returnings))
    print(f"\n {'SUMMARY':^50} \n")
    print(f"tests: {len(tasks):,}")

    print(f"passed tests: {tasks.count(True):,}")
    print(f"failed tests: {tasks.count(False):,}")
    print(f"failed groups: {' '.join(failed_groups)}")
    del failed_groups
    print(f"rate: {tasks.count(True) / len(tasks):2.2%}")
    del tasks
