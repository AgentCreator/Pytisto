"""
welcome to my unit test library!
--------------------------------

it is designed to be:
    - simple
    - feature rich
    - fast
"""

import sys

args = sys.argv[1:]

del sys

def assert_equals(real, expect, message = "") -> bool | str:
    return is_matching if (is_matching:=expect == real) else message if message != "" else is_matching
def assert_not_equals(real, expect, message ="") -> bool | str:
    return is_matching if (is_matching:=expect != real) else message if message != "" else is_matching
def test_group(name: str, tests: list[bool | str]) -> dict[str, list[bool | str]]:
    return {name:tests}
def tests(tests: dict[str, list[bool | str]]) -> None:
    tasks = []
    failed_groups = set({})
    print(f"\n {'TESTS':^50} \n")
    for i in tests:
        i = dict(i)
        print(list(i.keys())[0]+ ":")
        for o in list(i.values())[0]:
            if type(o) == bool:
                o = bool(o)
                tasks.append(o)
                if not o:
                    failed_groups.add(list(i.keys())[0])
                if args == [] or (fails := args[0] != "onlyfails"):
                    if len(tasks) < 50: print("  \\/ passed" if o else "  X failed")
                else:
                    if not o:
                        if len(tasks) < 50 or not fails: print("  X failed")
            else:
                o = str(o)
                tasks.append(False)
                if len(tasks) < 50 or not fails: print(f"  X failed: {o}")
        del o
    del i
    print(f"\n {'SUMMARY':^50} \n")
    print(f"tasks: {len(tasks):,}")

    print(f"passed tests: {tasks.count(True):,}")
    print(f"failed tests: {tasks.count(False):,}")
    print(f"failed groups: {' '.join(failed_groups)}")
    del failed_groups
    print(f"rate: {tasks.count(True)/len(tasks):2.2%}")
    del tasks
    

            
# if __name__ == "__main__":
#     tests([
#         test_group(
#             "example",
#             [
#                 assert_equals(1+1, 2, "hello"),
#             ]
#         ),
#         test_group(
#             "example2",
#             [
#                 assert_equals(1+2, 3)
#             ]
#         ),
#         test_group(
#             "random",
#             [
#                 assert_equals(1+3, 3, "wow you suck"),
#                 assert_equals(1+3, 3),
#             ]
#         )
#     ])
