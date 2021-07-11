"""
This type stub file was generated by pyright.
"""

from .compat import with_metaclass

class _ModuleClsMeta(type):
    def __setattr__(cls, key, value): # -> None:
        ...
    


class ModuleClsProxy(with_metaclass(_ModuleClsMeta)):
    """Create module level proxy functions for the
    methods on a given class.

    The functions will have a compatible signature
    as the methods.

    """
    _setups = ...
    @classmethod
    def create_module_class_proxy(cls, globals_, locals_): # -> None:
        ...
    


def asbool(value): # -> Literal[False]:
    ...

def rev_id(): # -> str:
    ...

def to_list(x, default=...): # -> list[Unknown]:
    ...

def to_tuple(x, default=...): # -> tuple[Unknown] | tuple[Unknown, ...]:
    ...

def unique_list(seq, hashfunc=...): # -> list[Unknown]:
    ...

def dedupe_tuple(tup): # -> tuple[Unknown, ...]:
    ...

class memoized_property:
    """A read-only @property that is only evaluated once."""
    def __init__(self, fget, doc=...) -> None:
        ...
    
    def __get__(self, obj, cls): # -> memoized_property:
        ...
    


class immutabledict(dict):
    __delitem__ = ...
    def __new__(cls, *args): # -> immutabledict:
        ...
    
    def __init__(self, *args) -> None:
        ...
    
    def __reduce__(self): # -> tuple[Type[immutabledict], tuple[dict[Unknown, Unknown]]]:
        ...
    
    def union(self, d): # -> immutabledict:
        ...
    
    def __repr__(self): # -> str:
        ...
    


class Dispatcher:
    def __init__(self, uselist=...) -> None:
        ...
    
    def dispatch_for(self, target, qualifier=...): # -> (fn: Unknown) -> Unknown:
        ...
    
    def dispatch(self, obj, qualifier=...): # -> (*arg: Unknown, **kw: Unknown) -> None:
        ...
    
    def branch(self): # -> Dispatcher:
        """Return a copy of this dispatcher that is independently
        writable."""
        ...
    


