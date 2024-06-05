"""
welcome to my unit test library!
--------------------------------

it is designed to be:
    - simple
    - feature rich
    - fast

"""
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


def assert_not_equals(real, expect, message="") -> bool | str:
    """
    returns True if the real and expections are not matched

    in case of mathing, returns False or the message (if provided)
    
    """
    return is_matching if (is_matching := expect != real) else message if message else is_matching


def test_group(name: str, unit_tests: list[bool | str]) -> dict[str, list[bool | str]]:
    """
    a way to group multiple tests in a group with a name, it is required.
    """
    return {name: unit_tests}

def expect_error(task: typing.Callable, values:list, exception: Exception, message: str = ""):
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


def tests(unit_tests: list[dict[str, list[bool | str]]]) -> None:
    """
    the main function to start the tests.
    """
    tasks = []
    failed_groups = set({})
    print(f"\n {'TESTS':^50} \n")
    for i in unit_tests:
        i = dict(i)
        print(list(i.keys())[0] + ":")
        for o in list(i.values())[0]:
            if isinstance(o, bool):
                o = bool(o)
                tasks.append(o)
                if not o:
                    failed_groups.add(list(i.keys())[0])
                if args == [] or (fails := args[0] != "onlyfails"):
                    if len(tasks) < 50:
                        print("  \\/ passed" if o else "  X failed")
                else:
                    if not o:
                        if len(tasks) < 50 or not fails:
                            print("  X failed")
            else:
                o = str(o)
                tasks.append(False)
                if len(tasks) < 50 or not fails:
                    print(f"  X failed: {o}")
        del o
    print(f"\n {'SUMMARY':^50} \n")
    print(f"tasks: {len(tasks):,}")

    print(f"passed tests: {tasks.count(True):,}")
    print(f"failed tests: {tasks.count(False):,}")
    print(f"failed groups: {' '.join(failed_groups)}")
    del failed_groups
    print(f"rate: {tasks.count(True) / len(tasks):2.2%}")
    del tasks
