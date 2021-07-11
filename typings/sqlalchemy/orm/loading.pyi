"""
This type stub file was generated by pyright.
"""

from .. import util

"""private module containing functions used to convert database
rows into object instances and associated state.

the functions here are called primarily by Query, Mapper,
as well as some of the attribute loading strategies.

"""
_new_runid = ...
def instances(cursor, context): # -> ChunkedIteratorResult:
    """Return a :class:`.Result` given an ORM query context.

    :param cursor: a :class:`.CursorResult`, generated by a statement
     which came from :class:`.ORMCompileState`

    :param context: a :class:`.QueryContext` object

    :return: a :class:`.Result` object representing ORM results

    .. versionchanged:: 1.4 The instances() function now uses
       :class:`.Result` objects and has an all new interface.

    """
    ...

@util.preload_module("sqlalchemy.orm.context")
def merge_frozen_result(session, statement, frozen_result, load=...):
    """Merge a :class:`_engine.FrozenResult` back into a :class:`_orm.Session`,
    returning a new :class:`_engine.Result` object with :term:`persistent`
    objects.

    See the section :ref:`do_orm_execute_re_executing` for an example.

    .. seealso::

        :ref:`do_orm_execute_re_executing`

        :meth:`_engine.Result.freeze`

        :class:`_engine.FrozenResult`

    """
    ...

@util.deprecated("2.0", "The :func:`_orm.merge_result` method is superseded by the " ":func:`_orm.merge_frozen_result` function.")
@util.preload_module("sqlalchemy.orm.context")
def merge_result(query, iterator, load=...): # -> Iterator[Unknown]:
    """Merge a result into this :class:`.Query` object's Session."""
    ...

def get_from_identity(session, mapper, key, passive): # -> _symbol | None:
    """Look up the given key in the given session's identity map,
    check the object for expired state if found.

    """
    ...

def load_on_ident(session, statement, key, load_options=..., refresh_state=..., with_for_update=..., only_load_props=..., no_autoflush=..., bind_arguments=..., execution_options=...): # -> None:
    """Load the given identity key from the database."""
    ...

def load_on_pk_identity(session, statement, primary_key_identity, load_options=..., refresh_state=..., with_for_update=..., only_load_props=..., identity_token=..., no_autoflush=..., bind_arguments=..., execution_options=...): # -> None:
    """Load the given primary key identity from the database."""
    ...

class PostLoad:
    """Track loaders and states for "post load" operations."""
    __slots__ = ...
    def __init__(self) -> None:
        ...
    
    def add_state(self, state, overwrite): # -> None:
        ...
    
    def invoke(self, context, path): # -> None:
        ...
    
    @classmethod
    def for_context(cls, context, path, only_load_props):
        ...
    
    @classmethod
    def path_exists(self, context, path, key): # -> bool:
        ...
    
    @classmethod
    def callable_for_path(cls, context, path, limit_to_mapper, token, loader_callable, *arg, **kw): # -> None:
        ...
    


def load_scalar_attributes(mapper, state, attribute_names, passive): # -> None:
    """initiate a column-based attribute refresh operation."""
    ...

