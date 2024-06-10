"""
Notes:
    adds cases.
    for example below:
    in case of "case2", set hello to "hello".
Examples:

    >>> hello = Case("world", case2="hello")
    >>> print(hello)
    world
    >>> change_case("case2")
    >>> print(hello)
    hello


"""

behavior_case = "case2"


class Case(object):
    def __init__(self, default_behavior: str, **case_kwargs: str) -> None:
        """

        Args:
            default_behavior: what the default value should be
            **case_kwargs: what the value should be in other cases
        """
        self.default_behavior = default_behavior
        self.case_kwargs = case_kwargs

    def __str__(self):
        global behavior_case
        if behavior_case == "default":
            return self.default_behavior
        return self.case_kwargs[behavior_case]


def change_case(to: str) -> None:
    global behavior_case
    behavior_case = to