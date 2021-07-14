"""
This type stub file was generated by pyright.
"""

import contextlib
from ..util import decorator

def skip_if(predicate, reason=...): # -> compound:
    ...

def fails_if(predicate, reason=...): # -> compound:
    ...

class compound:
    def __init__(self) -> None:
        ...
    
    def __add__(self, other): # -> compound:
        ...
    
    def as_skips(self): # -> compound:
        ...
    
    def add(self, *others): # -> compound:
        ...
    
    def not_(self): # -> compound:
        ...
    
    @property
    def enabled(self): # -> bool:
        ...
    
    def enabled_for_config(self, config): # -> bool:
        ...
    
    def matching_config_reasons(self, config): # -> list[Unknown]:
        ...
    
    def include_test(self, include_tags, exclude_tags): # -> bool:
        ...
    
    def __call__(self, fn): # -> None:
        ...
    
    @contextlib.contextmanager
    def fail_if(self): # -> Generator[None, None, None]:
        ...
    


def requires_tag(tagname): # -> compound:
    ...

def tags(tagnames): # -> compound:
    ...

def only_if(predicate, reason=...): # -> compound:
    ...

def succeeds_if(predicate, reason=...): # -> compound:
    ...

class Predicate:
    @classmethod
    def as_predicate(cls, predicate, description=...): # -> Predicate | OrPredicate | SpecPredicate | LambdaPredicate:
        ...
    


class BooleanPredicate(Predicate):
    def __init__(self, value, description=...) -> None:
        ...
    
    def __call__(self, config):
        ...
    


class SpecPredicate(Predicate):
    def __init__(self, db, op=..., spec=..., description=...) -> None:
        ...
    
    _ops = ...
    def __call__(self, config): # -> Any | bool:
        ...
    


class LambdaPredicate(Predicate):
    def __init__(self, lambda_, description=..., args=..., kw=...) -> None:
        ...
    
    def __call__(self, config):
        ...
    


class NotPredicate(Predicate):
    def __init__(self, predicate, description=...) -> None:
        ...
    
    def __call__(self, config): # -> bool:
        ...
    


class OrPredicate(Predicate):
    def __init__(self, predicates, description=...) -> None:
        ...
    
    def __call__(self, config): # -> bool:
        ...
    


_as_predicate = ...
def db_spec(*dbs): # -> OrPredicate:
    ...

def open(): # -> compound:
    ...

def closed(): # -> compound:
    ...

def fails(reason=...): # -> compound:
    ...

@decorator
def future(fn, *arg): # -> compound:
    ...

def fails_on(db, reason=...): # -> compound:
    ...

def fails_on_everything_except(*dbs): # -> compound:
    ...

def skip(db, reason=...): # -> compound:
    ...

def only_on(dbs, reason=...): # -> compound:
    ...

def exclude(db, op, spec, reason=...): # -> compound:
    ...

def against(config, *queries): # -> bool:
    ...
