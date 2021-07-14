"""
This type stub file was generated by pyright.
"""

from . import roles
from .traversals import HasCacheKey, HasCopyInternals
from .visitors import ClauseVisitor
from .. import util
from ..util import HasMemoized, hybridmethod

"""Foundational utilities common to many sql modules.

"""
coercions = ...
elements = ...
type_api = ...
PARSE_AUTOCOMMIT = ...
NO_ARG = ...
class Immutable:
    """mark a ClauseElement as 'immutable' when expressions are cloned."""
    def unique_params(self, *optionaldict, **kwargs):
        ...
    
    def params(self, *optionaldict, **kwargs):
        ...
    


class SingletonConstant(Immutable):
    """Represent SQL constants like NULL, TRUE, FALSE"""
    def __new__(cls, *arg, **kw): # -> Any:
        ...
    
    proxy_set = ...


class _DialectArgView(util.collections_abc.MutableMapping):
    """A dictionary view of dialect-level arguments in the form
    <dialectname>_<argument_name>.

    """
    def __init__(self, obj) -> None:
        ...
    
    def __getitem__(self, key): # -> None:
        ...
    
    def __setitem__(self, key, value): # -> None:
        ...
    
    def __delitem__(self, key): # -> None:
        ...
    
    def __len__(self): # -> int:
        ...
    
    def __iter__(self): # -> Generator[str, None, None]:
        ...
    


class _DialectArgDict(util.collections_abc.MutableMapping):
    """A dictionary view of dialect-level arguments for a specific
    dialect.

    Maintains a separate collection of user-specified arguments
    and dialect-specified default arguments.

    """
    def __init__(self) -> None:
        ...
    
    def __len__(self): # -> int:
        ...
    
    def __iter__(self): # -> Iterator[Unknown]:
        ...
    
    def __getitem__(self, key):
        ...
    
    def __setitem__(self, key, value): # -> None:
        ...
    
    def __delitem__(self, key): # -> None:
        ...
    


class DialectKWArgs:
    """Establish the ability for a class to have dialect-specific arguments
    with defaults and constructor validation.

    The :class:`.DialectKWArgs` interacts with the
    :attr:`.DefaultDialect.construct_arguments` present on a dialect.

    .. seealso::

        :attr:`.DefaultDialect.construct_arguments`

    """
    _dialect_kwargs_traverse_internals = ...
    @classmethod
    def argument_for(cls, dialect_name, argument_name, default): # -> None:
        """Add a new kind of dialect-specific keyword argument for this class.

        E.g.::

            Index.argument_for("mydialect", "length", None)

            some_index = Index('a', 'b', mydialect_length=5)

        The :meth:`.DialectKWArgs.argument_for` method is a per-argument
        way adding extra arguments to the
        :attr:`.DefaultDialect.construct_arguments` dictionary. This
        dictionary provides a list of argument names accepted by various
        schema-level constructs on behalf of a dialect.

        New dialects should typically specify this dictionary all at once as a
        data member of the dialect class.  The use case for ad-hoc addition of
        argument names is typically for end-user code that is also using
        a custom compilation scheme which consumes the additional arguments.

        :param dialect_name: name of a dialect.  The dialect must be
         locatable, else a :class:`.NoSuchModuleError` is raised.   The
         dialect must also include an existing
         :attr:`.DefaultDialect.construct_arguments` collection, indicating
         that it participates in the keyword-argument validation and default
         system, else :class:`.ArgumentError` is raised.  If the dialect does
         not include this collection, then any keyword argument can be
         specified on behalf of this dialect already.  All dialects packaged
         within SQLAlchemy include this collection, however for third party
         dialects, support may vary.

        :param argument_name: name of the parameter.

        :param default: default value of the parameter.

        .. versionadded:: 0.9.4

        """
        ...
    
    @util.memoized_property
    def dialect_kwargs(self): # -> _DialectArgView:
        """A collection of keyword arguments specified as dialect-specific
        options to this construct.

        The arguments are present here in their original ``<dialect>_<kwarg>``
        format.  Only arguments that were actually passed are included;
        unlike the :attr:`.DialectKWArgs.dialect_options` collection, which
        contains all options known by this dialect including defaults.

        The collection is also writable; keys are accepted of the
        form ``<dialect>_<kwarg>`` where the value will be assembled
        into the list of options.

        .. versionadded:: 0.9.2

        .. versionchanged:: 0.9.4 The :attr:`.DialectKWArgs.dialect_kwargs`
           collection is now writable.

        .. seealso::

            :attr:`.DialectKWArgs.dialect_options` - nested dictionary form

        """
        ...
    
    @property
    def kwargs(self): # -> memoized_property:
        """A synonym for :attr:`.DialectKWArgs.dialect_kwargs`."""
        ...
    
    _kw_registry = ...
    @util.memoized_property
    def dialect_options(self): # -> PopulateDict:
        """A collection of keyword arguments specified as dialect-specific
        options to this construct.

        This is a two-level nested registry, keyed to ``<dialect_name>``
        and ``<argument_name>``.  For example, the ``postgresql_where``
        argument would be locatable as::

            arg = my_object.dialect_options['postgresql']['where']

        .. versionadded:: 0.9.2

        .. seealso::

            :attr:`.DialectKWArgs.dialect_kwargs` - flat dictionary form

        """
        ...
    


class CompileState:
    """Produces additional object state necessary for a statement to be
    compiled.

    the :class:`.CompileState` class is at the base of classes that assemble
    state for a particular statement object that is then used by the
    compiler.   This process is essentially an extension of the process that
    the SQLCompiler.visit_XYZ() method takes, however there is an emphasis
    on converting raw user intent into more organized structures rather than
    producing string output.   The top-level :class:`.CompileState` for the
    statement being executed is also accessible when the execution context
    works with invoking the statement and collecting results.

    The production of :class:`.CompileState` is specific to the compiler,  such
    as within the :meth:`.SQLCompiler.visit_insert`,
    :meth:`.SQLCompiler.visit_select` etc. methods.  These methods are also
    responsible for associating the :class:`.CompileState` with the
    :class:`.SQLCompiler` itself, if the statement is the "toplevel" statement,
    i.e. the outermost SQL statement that's actually being executed.
    There can be other :class:`.CompileState` objects that are not the
    toplevel, such as when a SELECT subquery or CTE-nested
    INSERT/UPDATE/DELETE is generated.

    .. versionadded:: 1.4

    """
    __slots__ = ...
    plugins = ...
    @classmethod
    def create_for_statement(cls, statement, compiler, **kw): # -> CompileState:
        ...
    
    def __init__(self, statement, compiler, **kw) -> None:
        ...
    
    @classmethod
    def get_plugin_class(cls, statement): # -> None:
        ...
    
    @classmethod
    def plugin_for(cls, plugin_name, visit_name): # -> (cls_to_decorate: Unknown) -> Unknown:
        ...
    


class Generative(HasMemoized):
    """Provide a method-chaining pattern in conjunction with the
    @_generative decorator."""
    ...


class InPlaceGenerative(HasMemoized):
    """Provide a method-chaining pattern in conjunction with the
    @_generative decorator that mutates in place."""
    ...


class HasCompileState(Generative):
    """A class that has a :class:`.CompileState` associated with it."""
    _compile_state_plugin = ...
    _attributes = ...
    _compile_state_factory = ...


class _MetaOptions(type):
    """metaclass for the Options class."""
    def __init__(cls, classname, bases, dict_) -> None:
        ...
    
    def __add__(self, other): # -> Any:
        ...
    


class Options(util.with_metaclass(_MetaOptions)):
    """A cacheable option dictionary with defaults."""
    def __init__(self, **kw) -> None:
        ...
    
    def __add__(self, other): # -> Any:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    @classmethod
    def isinstance(cls, klass): # -> bool:
        ...
    
    @hybridmethod
    def add_to_element(self, name, value): # -> Any:
        ...
    
    _state_dict_const = ...
    @classmethod
    def safe_merge(cls, other):
        ...
    
    @classmethod
    def from_execution_options(cls, key, attrs, exec_options, statement_exec_options): # -> tuple[Unknown, immutabledict] | tuple[Unknown, Unknown]:
        """process Options argument in terms of execution options.


        e.g.::

            (
                load_options,
                execution_options,
            ) = QueryContext.default_load_options.from_execution_options(
                "_sa_orm_load_options",
                {
                    "populate_existing",
                    "autoflush",
                    "yield_per"
                },
                execution_options,
                statement._execution_options,
            )

        get back the Options and refresh "_sa_orm_load_options" in the
        exec options dict w/ the Options as well

        """
        ...
    


class CacheableOptions(Options, HasCacheKey):
    ...


class ExecutableOption(HasCopyInternals, HasCacheKey):
    _annotations = ...
    __visit_name__ = ...


class Executable(roles.StatementRole, Generative):
    """Mark a :class:`_expression.ClauseElement` as supporting execution.

    :class:`.Executable` is a superclass for all "statement" types
    of objects, including :func:`select`, :func:`delete`, :func:`update`,
    :func:`insert`, :func:`text`.

    """
    supports_execution = ...
    _execution_options = ...
    _bind = ...
    _with_options = ...
    _with_context_options = ...
    _executable_traverse_internals = ...
    is_select = ...
    is_update = ...
    is_insert = ...
    is_text = ...
    is_delete = ...
    is_dml = ...
    @_generative
    def options(self, *options): # -> None:
        """Apply options to this statement.

        In the general sense, options are any kind of Python object
        that can be interpreted by the SQL compiler for the statement.
        These options can be consumed by specific dialects or specific kinds
        of compilers.

        The most commonly known kind of option are the ORM level options
        that apply "eager load" and other loading behaviors to an ORM
        query.   However, options can theoretically be used for many other
        purposes.

        For background on specific kinds of options for specific kinds of
        statements, refer to the documentation for those option objects.

        .. versionchanged:: 1.4 - added :meth:`.Generative.options` to
           Core statement objects towards the goal of allowing unified
           Core / ORM querying capabilities.

        .. seealso::

            :ref:`deferred_options` - refers to options specific to the usage
            of ORM queries

            :ref:`relationship_loader_options` - refers to options specific
            to the usage of ORM queries

        """
        ...
    
    @_generative
    def execution_options(self, **kw): # -> None:
        """Set non-SQL options for the statement which take effect during
        execution.

        Execution options can be set on a per-statement or
        per :class:`_engine.Connection` basis.   Additionally, the
        :class:`_engine.Engine` and ORM :class:`~.orm.query.Query`
        objects provide
        access to execution options which they in turn configure upon
        connections.

        The :meth:`execution_options` method is generative.  A new
        instance of this statement is returned that contains the options::

            statement = select(table.c.x, table.c.y)
            statement = statement.execution_options(autocommit=True)

        Note that only a subset of possible execution options can be applied
        to a statement - these include "autocommit" and "stream_results",
        but not "isolation_level" or "compiled_cache".
        See :meth:`_engine.Connection.execution_options` for a full list of
        possible options.

        .. seealso::

            :meth:`_engine.Connection.execution_options`

            :meth:`_query.Query.execution_options`

            :meth:`.Executable.get_execution_options`

        """
        ...
    
    def get_execution_options(self): # -> immutabledict:
        """Get the non-SQL options which will take effect during execution.

        .. versionadded:: 1.3

        .. seealso::

            :meth:`.Executable.execution_options`
        """
        ...
    
    @util.deprecated_20(":meth:`.Executable.execute`", alternative="All statement execution in SQLAlchemy 2.0 is performed " "by the :meth:`_engine.Connection.execute` method of " ":class:`_engine.Connection`, " "or in the ORM by the :meth:`.Session.execute` method of " ":class:`.Session`.")
    def execute(self, *multiparams, **params):
        """Compile and execute this :class:`.Executable`."""
        ...
    
    @util.deprecated_20(":meth:`.Executable.scalar`", alternative="Scalar execution in SQLAlchemy 2.0 is performed " "by the :meth:`_engine.Connection.scalar` method of " ":class:`_engine.Connection`, " "or in the ORM by the :meth:`.Session.scalar` method of " ":class:`.Session`.")
    def scalar(self, *multiparams, **params):
        """Compile and execute this :class:`.Executable`, returning the
        result's scalar representation.

        """
        ...
    
    @property
    @util.deprecated_20(":attr:`.Executable.bind`", alternative="Bound metadata is being removed as of SQLAlchemy 2.0.", enable_warnings=False)
    def bind(self): # -> None:
        """Returns the :class:`_engine.Engine` or :class:`_engine.Connection`
        to
        which this :class:`.Executable` is bound, or None if none found.

        This is a traversal which checks locally, then
        checks among the "from" clauses of associated objects
        until a bound engine or connection is found.

        """
        ...
    


class prefix_anon_map(dict):
    """A map that creates new keys for missing key access.

    Considers keys of the form "<ident> <name>" to produce
    new symbols "<name>_<index>", where "index" is an incrementing integer
    corresponding to <name>.

    Inlines the approach taken by :class:`sqlalchemy.util.PopulateDict` which
    is otherwise usually used for this type of operation.

    """
    def __missing__(self, key):
        ...
    


class SchemaEventTarget:
    """Base class for elements that are the targets of :class:`.DDLEvents`
    events.

    This includes :class:`.SchemaItem` as well as :class:`.SchemaType`.

    """
    ...


class SchemaVisitor(ClauseVisitor):
    """Define the visiting for ``SchemaItem`` objects."""
    __traverse_options__ = ...


class ColumnCollection:
    """Collection of :class:`_expression.ColumnElement` instances,
    typically for
    :class:`_sql.FromClause` objects.

    The :class:`_sql.ColumnCollection` object is most commonly available
    as the :attr:`_schema.Table.c` or :attr:`_schema.Table.columns` collection
    on the :class:`_schema.Table` object, introduced at
    :ref:`metadata_tables_and_columns`.

    The :class:`_expression.ColumnCollection` has both mapping- and sequence-
    like behaviors. A :class:`_expression.ColumnCollection` usually stores
    :class:`_schema.Column` objects, which are then accessible both via mapping
    style access as well as attribute access style.

    To access :class:`_schema.Column` objects using ordinary attribute-style
    access, specify the name like any other object attribute, such as below
    a column named ``employee_name`` is accessed::

        >>> employee_table.c.employee_name

    To access columns that have names with special characters or spaces,
    index-style access is used, such as below which illustrates a column named
    ``employee ' payment`` is accessed::

        >>> employee_table.c["employee ' payment"]

    As the :class:`_sql.ColumnCollection` object provides a Python dictionary
    interface, common dictionary method names like
    :meth:`_sql.ColumnCollection.keys`, :meth:`_sql.ColumnCollection.values`,
    and :meth:`_sql.ColumnCollection.items` are available, which means that
    database columns that are keyed under these names also need to use indexed
    access::

        >>> employee_table.c["values"]


    The name for which a :class:`_schema.Column` would be present is normally
    that of the :paramref:`_schema.Column.key` parameter.  In some contexts,
    such as a :class:`_sql.Select` object that uses a label style set
    using the :meth:`_sql.Select.set_label_style` method, a column of a certain
    key may instead be represented under a particular label name such
    as ``tablename_columnname``::

        >>> from sqlalchemy import select, column, table
        >>> from sqlalchemy import LABEL_STYLE_TABLENAME_PLUS_COL
        >>> t = table("t", column("c"))
        >>> stmt = select(t).set_label_style(LABEL_STYLE_TABLENAME_PLUS_COL)
        >>> subq = stmt.subquery()
        >>> subq.c.t_c
        <sqlalchemy.sql.elements.ColumnClause at 0x7f59dcf04fa0; t_c>

    :class:`.ColumnCollection` also indexes the columns in order and allows
    them to be accessible by their integer position::

        >>> cc[0]
        Column('x', Integer(), table=None)
        >>> cc[1]
        Column('y', Integer(), table=None)

    .. versionadded:: 1.4 :class:`_expression.ColumnCollection`
       allows integer-based
       index access to the collection.

    Iterating the collection yields the column expressions in order::

        >>> list(cc)
        [Column('x', Integer(), table=None),
         Column('y', Integer(), table=None)]

    The base :class:`_expression.ColumnCollection` object can store
    duplicates, which can
    mean either two columns with the same key, in which case the column
    returned by key  access is **arbitrary**::

        >>> x1, x2 = Column('x', Integer), Column('x', Integer)
        >>> cc = ColumnCollection(columns=[(x1.name, x1), (x2.name, x2)])
        >>> list(cc)
        [Column('x', Integer(), table=None),
         Column('x', Integer(), table=None)]
        >>> cc['x'] is x1
        False
        >>> cc['x'] is x2
        True

    Or it can also mean the same column multiple times.   These cases are
    supported as :class:`_expression.ColumnCollection`
    is used to represent the columns in
    a SELECT statement which may include duplicates.

    A special subclass :class:`.DedupeColumnCollection` exists which instead
    maintains SQLAlchemy's older behavior of not allowing duplicates; this
    collection is used for schema level objects like :class:`_schema.Table`
    and
    :class:`.PrimaryKeyConstraint` where this deduping is helpful.  The
    :class:`.DedupeColumnCollection` class also has additional mutation methods
    as the schema constructs have more use cases that require removal and
    replacement of columns.

    .. versionchanged:: 1.4 :class:`_expression.ColumnCollection`
       now stores duplicate
       column keys as well as the same column in multiple positions.  The
       :class:`.DedupeColumnCollection` class is added to maintain the
       former behavior in those cases where deduplication as well as
       additional replace/remove operations are needed.


    """
    __slots__ = ...
    def __init__(self, columns=...) -> None:
        ...
    
    def keys(self): # -> list[Unknown]:
        """Return a sequence of string key names for all columns in this
        collection."""
        ...
    
    def values(self): # -> list[Unknown]:
        """Return a sequence of :class:`_sql.ColumnClause` or
        :class:`_schema.Column` objects for all columns in this
        collection."""
        ...
    
    def items(self): # -> list[Unknown]:
        """Return a sequence of (key, column) tuples for all columns in this
        collection each consisting of a string key name and a
        :class:`_sql.ColumnClause` or
        :class:`_schema.Column` object.
        """
        ...
    
    def __bool__(self): # -> bool:
        ...
    
    def __len__(self): # -> int:
        ...
    
    def __iter__(self): # -> Iterator[_T@iter]:
        ...
    
    def __getitem__(self, key): # -> None:
        ...
    
    def __getattr__(self, key): # -> None:
        ...
    
    def __contains__(self, key): # -> bool:
        ...
    
    def compare(self, other): # -> bool:
        """Compare this :class:`_expression.ColumnCollection` to another
        based on the names of the keys"""
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def get(self, key, default=...):
        """Get a :class:`_sql.ColumnClause` or :class:`_schema.Column` object
        based on a string key name from this
        :class:`_expression.ColumnCollection`."""
        ...
    
    def __str__(self) -> str:
        ...
    
    def __setitem__(self, key, value):
        ...
    
    def __delitem__(self, key):
        ...
    
    def __setattr__(self, key, obj):
        ...
    
    def clear(self):
        """Dictionary clear() is not implemented for
        :class:`_sql.ColumnCollection`."""
        ...
    
    def remove(self, column):
        """Dictionary remove() is not implemented for
        :class:`_sql.ColumnCollection`."""
        ...
    
    def update(self, iter_):
        """Dictionary update() is not implemented for
        :class:`_sql.ColumnCollection`."""
        ...
    
    __hash__ = ...
    def add(self, column, key=...): # -> None:
        """Add a column to this :class:`_sql.ColumnCollection`.

        .. note::

            This method is **not normally used by user-facing code**, as the
            :class:`_sql.ColumnCollection` is usually part of an existing
            object such as a :class:`_schema.Table`. To add a
            :class:`_schema.Column` to an existing :class:`_schema.Table`
            object, use the :meth:`_schema.Table.append_column` method.

        """
        ...
    
    def __getstate__(self): # -> dict[str, Unbound]:
        ...
    
    def __setstate__(self, state): # -> None:
        ...
    
    def contains_column(self, col): # -> bool:
        """Checks if a column object exists in this collection"""
        ...
    
    def as_immutable(self): # -> ImmutableColumnCollection:
        """Return an "immutable" form of this
        :class:`_sql.ColumnCollection`."""
        ...
    
    def corresponding_column(self, column, require_embedded=...): # -> None:
        """Given a :class:`_expression.ColumnElement`, return the exported
        :class:`_expression.ColumnElement` object from this
        :class:`_expression.ColumnCollection`
        which corresponds to that original :class:`_expression.ColumnElement`
        via a common
        ancestor column.

        :param column: the target :class:`_expression.ColumnElement`
                      to be matched.

        :param require_embedded: only return corresponding columns for
         the given :class:`_expression.ColumnElement`, if the given
         :class:`_expression.ColumnElement`
         is actually present within a sub-element
         of this :class:`_expression.Selectable`.
         Normally the column will match if
         it merely shares a common ancestor with one of the exported
         columns of this :class:`_expression.Selectable`.

        .. seealso::

            :meth:`_expression.Selectable.corresponding_column`
            - invokes this method
            against the collection returned by
            :attr:`_expression.Selectable.exported_columns`.

        .. versionchanged:: 1.4 the implementation for ``corresponding_column``
           was moved onto the :class:`_expression.ColumnCollection` itself.

        """
        ...
    


class DedupeColumnCollection(ColumnCollection):
    """A :class:`_expression.ColumnCollection`
    that maintains deduplicating behavior.

    This is useful by schema level objects such as :class:`_schema.Table` and
    :class:`.PrimaryKeyConstraint`.    The collection includes more
    sophisticated mutator methods as well to suit schema objects which
    require mutable column collections.

    .. versionadded:: 1.4

    """
    def add(self, column, key=...): # -> None:
        ...
    
    def extend(self, iter_): # -> None:
        ...
    
    def remove(self, column): # -> None:
        ...
    
    def replace(self, column): # -> None:
        """add the given column to this collection, removing unaliased
        versions of this column  as well as existing columns with the
        same key.

        e.g.::

            t = Table('sometable', metadata, Column('col1', Integer))
            t.columns.replace(Column('col1', Integer, key='columnone'))

        will remove the original 'col1' from the collection, and add
        the new column under the name 'columnname'.

        Used by schema.Column to override columns during table reflection.

        """
        ...
    


class ImmutableColumnCollection(util.ImmutableContainer, ColumnCollection):
    __slots__ = ...
    def __init__(self, collection) -> None:
        ...
    
    def __getstate__(self): # -> dict[str, Unbound]:
        ...
    
    def __setstate__(self, state): # -> None:
        ...
    
    add = ...


class ColumnSet(util.ordered_column_set):
    def contains_column(self, col): # -> bool:
        ...
    
    def extend(self, cols): # -> None:
        ...
    
    def __add__(self, other): # -> List[Unknown]:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    

