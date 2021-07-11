"""
This type stub file was generated by pyright.
"""

"""Routines to handle the string class registry used by declarative.

This system allows specification of classes and expressions used in
:func:`_orm.relationship` using strings.

"""
_registries = ...
def add_class(classname, cls, decl_class_registry): # -> None:
    """Add a class to the _decl_class_registry associated with the
    given declarative class.

    """
    ...

def remove_class(classname, cls, decl_class_registry): # -> None:
    ...

class _MultipleClassMarker:
    """refers to multiple classes of the same name
    within _decl_class_registry.

    """
    __slots__ = ...
    def __init__(self, classes, on_remove=...) -> None:
        ...
    
    def remove_item(self, cls): # -> None:
        ...
    
    def __iter__(self): # -> Generator[Unknown | None, None, None]:
        ...
    
    def attempt_get(self, path, key):
        ...
    
    def add_item(self, item): # -> None:
        ...
    


class _ModuleMarker:
    """Refers to a module name within
    _decl_class_registry.

    """
    __slots__ = ...
    def __init__(self, name, parent) -> None:
        ...
    
    def __contains__(self, name): # -> bool:
        ...
    
    def __getitem__(self, name):
        ...
    
    def resolve_attr(self, key): # -> Any:
        ...
    
    def get_module(self, name): # -> _ModuleMarker:
        ...
    
    def add_class(self, name, cls): # -> None:
        ...
    
    def remove_class(self, name, cls): # -> None:
        ...
    


class _ModNS:
    __slots__ = ...
    def __init__(self, parent) -> None:
        ...
    
    def __getattr__(self, key): # -> _ModNS:
        ...
    


class _GetColumns:
    __slots__ = ...
    def __init__(self, cls) -> None:
        ...
    
    def __getattr__(self, key): # -> Any:
        ...
    


class _GetTable:
    __slots__ = ...
    def __init__(self, key, metadata) -> None:
        ...
    
    def __getattr__(self, key):
        ...
    


class _class_resolver:
    __slots__ = ...
    def __init__(self, cls, prop, fallback, arg, favor_tables=...) -> None:
        ...
    
    def __call__(self): # -> Any | None:
        ...
    


_fallback_dict = ...
