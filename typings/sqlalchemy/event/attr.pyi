"""
This type stub file was generated by pyright.
"""

from .. import util

"""Attribute implementation for _Dispatch classes.

The various listener targets for a particular event class are represented
as attributes, which refer to collections of listeners to be fired off.
These collections can exist at the class level as well as at the instance
level.  An event is fired off using code like this::

    some_object.dispatch.first_connect(arg1, arg2)

Above, ``some_object.dispatch`` would be an instance of ``_Dispatch`` and
``first_connect`` is typically an instance of ``_ListenerCollection``
if event listeners are present, or ``_EmptyListener`` if none are present.

The attribute mechanics here spend effort trying to ensure listener functions
are available with a minimum of function call overhead, that unnecessary
objects aren't created (i.e. many empty per-instance listener collections),
as well as that everything is garbage collectable when owning references are
lost.  Other features such as "propagation" of listener functions across
many ``_Dispatch`` instances, "joining" of multiple ``_Dispatch`` instances,
as well as support for subclass propagation (e.g. events assigned to
``Pool`` vs. ``QueuePool``) are all implemented here.

"""
class RefCollection(util.MemoizedSlots):
    __slots__ = ...


class _empty_collection:
    def append(self, element): # -> None:
        ...
    
    def extend(self, other): # -> None:
        ...
    
    def remove(self, element): # -> None:
        ...
    
    def __iter__(self): # -> Iterator[Any]:
        ...
    
    def clear(self): # -> None:
        ...
    


class _ClsLevelDispatch(RefCollection):
    """Class-level events on :class:`._Dispatch` classes."""
    __slots__ = ...
    def __init__(self, parent_dispatch_cls, fn) -> None:
        ...
    
    def insert(self, event_key, propagate): # -> None:
        ...
    
    def append(self, event_key, propagate): # -> None:
        ...
    
    def update_subclass(self, target): # -> None:
        ...
    
    def remove(self, event_key): # -> None:
        ...
    
    def clear(self): # -> None:
        """Clear all class level listeners"""
        ...
    
    def for_modify(self, obj): # -> _ClsLevelDispatch:
        """Return an event collection which can be modified.

        For _ClsLevelDispatch at the class level of
        a dispatcher, this returns self.

        """
        ...
    


class _InstanceLevelDispatch(RefCollection):
    __slots__ = ...


class _EmptyListener(_InstanceLevelDispatch):
    """Serves as a proxy interface to the events
    served by a _ClsLevelDispatch, when there are no
    instance-level events present.

    Is replaced by _ListenerCollection when instance-level
    events are added.

    """
    propagate = ...
    listeners = ...
    __slots__ = ...
    def __init__(self, parent, target_cls) -> None:
        ...
    
    def for_modify(self, obj): # -> _ListenerCollection:
        """Return an event collection which can be modified.

        For _EmptyListener at the instance level of
        a dispatcher, this generates a new
        _ListenerCollection, applies it to the instance,
        and returns it.

        """
        ...
    
    exec_once = ...
    def __call__(self, *args, **kw): # -> None:
        """Execute this event."""
        ...
    
    def __len__(self): # -> int:
        ...
    
    def __iter__(self): # -> Iterator[Unknown]:
        ...
    
    def __bool__(self): # -> bool:
        ...
    
    __nonzero__ = ...


class _CompoundListener(_InstanceLevelDispatch):
    __slots__ = ...
    def exec_once(self, *args, **kw): # -> None:
        """Execute this event, but only if it has not been
        executed already for this collection."""
        ...
    
    def exec_once_unless_exception(self, *args, **kw): # -> None:
        """Execute this event, but only if it has not been
        executed already for this collection, or was called
        by a previous exec_once_unless_exception call and
        raised an exception.

        If exec_once was already called, then this method will never run
        the callable regardless of whether it raised or not.

        .. versionadded:: 1.3.8

        """
        ...
    
    def __call__(self, *args, **kw): # -> None:
        """Execute this event."""
        ...
    
    def __len__(self): # -> int:
        ...
    
    def __iter__(self): # -> chain[Unknown]:
        ...
    
    def __bool__(self): # -> bool:
        ...
    
    __nonzero__ = ...


class _ListenerCollection(_CompoundListener):
    """Instance-level attributes on instances of :class:`._Dispatch`.

    Represents a collection of listeners.

    As of 0.7.9, _ListenerCollection is only first
    created via the _EmptyListener.for_modify() method.

    """
    __slots__ = ...
    def __init__(self, parent, target_cls) -> None:
        ...
    
    def for_modify(self, obj): # -> _ListenerCollection:
        """Return an event collection which can be modified.

        For _ListenerCollection at the instance level of
        a dispatcher, this returns self.

        """
        ...
    
    def insert(self, event_key, propagate): # -> None:
        ...
    
    def append(self, event_key, propagate): # -> None:
        ...
    
    def remove(self, event_key): # -> None:
        ...
    
    def clear(self): # -> None:
        ...
    


class _JoinedListener(_CompoundListener):
    __slots__ = ...
    def __init__(self, parent, name, local) -> None:
        ...
    
    @property
    def listeners(self): # -> Any:
        ...
    
    def for_modify(self, obj): # -> _JoinedListener:
        ...
    
    def insert(self, event_key, propagate): # -> None:
        ...
    
    def append(self, event_key, propagate): # -> None:
        ...
    
    def remove(self, event_key): # -> None:
        ...
    
    def clear(self):
        ...
    


