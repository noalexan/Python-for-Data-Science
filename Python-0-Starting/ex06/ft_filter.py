from typing import Iterable, TypeVar, Callable, Optional


T = TypeVar('T')


def ft_filter(func: Optional[Callable[[T], bool]], iterable: Iterable[T]) \
        -> Iterable[T]:
    """
filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
"""

    if func is None:
        return (item for item in iterable if item)
    return (item for item in iterable if func(item))
