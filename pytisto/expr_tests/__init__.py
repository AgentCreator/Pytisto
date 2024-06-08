from types import NoneType
from typing import Callable, Any

def expr_tests(func: Callable, unit_tests: list[dict[tuple[Any, ...], Any]]):
    """
    an experimental test feature
    makes your tests faster, but you have to do dict comprehension, which was literally made by devil himself.
    param func: the function that we will be testing
    param unit_tests: the tests
    example:
    {
    ("arguments",):(expected_value, "message on failure"),
    # without a message on failure
    ("arguments",):expected_value
    }
    return: None
    """
    tasks = []
    returnings = [f"\n {'TESTS':^50} \n"]
    for p in unit_tests:
        for i in p.keys():
            message = ""
            if isinstance(p[i], tuple):
                message = p[i][1]
                test = p[i][0]
            else:
                test = p[i]

            try:
                tasks.append((is_matching := func(*i) == test))
                returnings.append("\\/ Passed" if is_matching else "X Failed" + (f": {message}" if message else ""))
            except TypeError:
                tasks.append((is_matching := func(i) == test))
                returnings.append("\\/ Passed" if is_matching else "X Failed" + (f": {message}" if message else ""))

    print("\n".join(returnings))

    print(f"\n {'SUMMARY':^50} \n")
    print(f"tested function: {func.__name__}()")
    print(f"unique tests: {len(tasks)}")
    print(f"passed: {tasks.count(True)}")
    print(f"failed: {tasks.count(False)}")
    print(f"rate: {tasks.count(True) / len(tasks):2.2%}")


def silent_expr_tests(func: Callable, unit_tests: list[dict[tuple[Any, ...], Any]], destroy=True):
    for p in unit_tests:
        for i in p.keys():
            if isinstance(p[i], tuple):
                message = p[i][1]
                test = p[i][0]
            else:
                test = p[i]

            try:
                if func(*i) != test:
                    print(f"""\nyour silent tests have failed:\nfunc: {func.__name__}\nvalues: {i}\n""")
                    if destroy:
                        __import__("sys", globals(), locals(), ["exit"], 0).exit()
            except TypeError:
                if func(i) != test:
                    print(f"""
                    your silent tests have failed:
                    func: {func.__name__}\nvalues: {i}\n""")
                    if destroy:
                        __import__("sys", globals(), locals(), ["exit"], 0).exit()


def autotest(ref: Callable | None = None,
             rand_int_range: list | None = None,
             destroy: bool = True,
             str_values: list[str] | None = None,
             test_amount: int = 20

             ):
    #       ^^^ a sad and lonely smiley
    """
    a decorator for functions, that automatically generates tests for the function.

    these tests are silent, so you won't know about the running unless you put a print statement inside the tested
    function or get a message that shuts down your code (disable this by setting destroy to False)

    in case of an error like "you can't divide by zero" or any other error about the range of numbers,
    just add rand_int_range, a list, that will contain all the possible numbers.

    your code only works with specific string values? set the str_values list to all the possible values!

    set the amount of tests taken with the test_amount value!
    """

    def decor(func: Callable):
        """
        the decorator.
        """
        def autotest_func(*argus, **kwargs):
            # a(*argus, **kwargs)
            # imports
            random_lib = __import__("random", globals(), locals(), ["randint, choice", "getrandbits"])
            string_lib = __import__("string", globals(), locals(), ["ascii_letters"])

            types = [type(i) for i in argus]

            def get_rand_test(types_list: list[type]):
                res = []
                for i in types_list:
                    if i == int:
                        res.append(random_lib.randint(-10_000, 10_000) if isinstance(rand_int_range, NoneType)
                                   else random_lib.choice(rand_int_range))
                    elif i == str:
                        res.append(random_lib.choice(str_values) if str_values else "".join(
                            random_lib.choice([*string_lib.ascii_letters]) for _ in range(test_amount)))
                    elif i == bool:
                        res.append(random_lib.getrandbits(1))
                return res

            if ref:
                silent_expr_tests(func, [
                    {
                        (val := tuple(get_rand_test(types))): ref(*val) for i in range(test_amount)
                    }
                ], destroy=destroy)
            else:
                for i in range(test_amount):
                    func(*get_rand_test(types))
            del string_lib
            del random_lib
            return func(*argus, **kwargs)

        return autotest_func

    return decor
