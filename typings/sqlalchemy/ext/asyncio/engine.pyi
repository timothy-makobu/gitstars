"""
This type stub file was generated by pyright.
"""

from .base import ProxyComparable, StartableContext
from ... import util
from ...future import Connection, Engine

def create_async_engine(*arg, **kw): # -> AsyncEngine:
    """Create a new async engine instance.

    Arguments passed to :func:`_asyncio.create_async_engine` are mostly
    identical to those passed to the :func:`_sa.create_engine` function.
    The specified dialect must be an asyncio-compatible dialect
    such as :ref:`dialect-postgresql-asyncpg`.

    .. versionadded:: 1.4

    """
    ...

class AsyncConnectable:
    __slots__ = ...


@util.create_proxy_methods(Connection, ":class:`_future.Connection`", ":class:`_asyncio.AsyncConnection`", classmethods=[], methods=[], attributes=["closed", "invalidated", "dialect", "default_isolation_level"])
class AsyncConnection(ProxyComparable, StartableContext, AsyncConnectable):
    """An asyncio proxy for a :class:`_engine.Connection`.

    :class:`_asyncio.AsyncConnection` is acquired using the
    :meth:`_asyncio.AsyncEngine.connect`
    method of :class:`_asyncio.AsyncEngine`::

        from sqlalchemy.ext.asyncio import create_async_engine
        engine = create_async_engine("postgresql+asyncpg://user:pass@host/dbname")

        async with engine.connect() as conn:
            result = await conn.execute(select(table))

    .. versionadded:: 1.4

    """
    __slots__ = ...
    def __init__(self, async_engine, sync_connection=...) -> None:
        ...
    
    async def start(self, is_ctxmanager=...): # -> AsyncConnection:
        """Start this :class:`_asyncio.AsyncConnection` object's context
        outside of using a Python ``with:`` block.

        """
        ...
    
    @property
    def connection(self): # -> NoReturn:
        """Not implemented for async; call
        :meth:`_asyncio.AsyncConnection.get_raw_connection`.

        """
        ...
    
    async def get_raw_connection(self):
        """Return the pooled DBAPI-level connection in use by this
        :class:`_asyncio.AsyncConnection`.

        This is typically the SQLAlchemy connection-pool proxied connection
        which then has an attribute .connection that refers to the actual
        DBAPI-level connection.
        """
        ...
    
    @property
    def info(self):
        """Return the :attr:`_engine.Connection.info` dictionary of the
        underlying :class:`_engine.Connection`.

        This dictionary is freely writable for user-defined state to be
        associated with the database connection.

        This attribute is only available if the :class:`.AsyncConnection` is
        currently connected.   If the :attr:`.AsyncConnection.closed` attribute
        is ``True``, then accessing this attribute will raise
        :class:`.ResourceClosedError`.

        .. versionadded:: 1.4.0b2

        """
        ...
    
    def begin(self): # -> AsyncTransaction:
        """Begin a transaction prior to autobegin occurring."""
        ...
    
    def begin_nested(self): # -> AsyncTransaction:
        """Begin a nested transaction and return a transaction handle."""
        ...
    
    async def invalidate(self, exception=...):
        """Invalidate the underlying DBAPI connection associated with
        this :class:`_engine.Connection`.

        See the method :meth:`_engine.Connection.invalidate` for full
        detail on this method.

        """
        ...
    
    async def get_isolation_level(self):
        ...
    
    async def set_isolation_level(self):
        ...
    
    def in_transaction(self):
        """Return True if a transaction is in progress.

        .. versionadded:: 1.4.0b2

        """
        ...
    
    def in_nested_transaction(self):
        """Return True if a transaction is in progress.

        .. versionadded:: 1.4.0b2

        """
        ...
    
    def get_transaction(self): # -> None:
        """Return an :class:`.AsyncTransaction` representing the current
        transaction, if any.

        This makes use of the underlying synchronous connection's
        :meth:`_engine.Connection.get_transaction` method to get the current
        :class:`_engine.Transaction`, which is then proxied in a new
        :class:`.AsyncTransaction` object.

        .. versionadded:: 1.4.0b2

        """
        ...
    
    def get_nested_transaction(self): # -> None:
        """Return an :class:`.AsyncTransaction` representing the current
        nested (savepoint) transaction, if any.

        This makes use of the underlying synchronous connection's
        :meth:`_engine.Connection.get_nested_transaction` method to get the
        current :class:`_engine.Transaction`, which is then proxied in a new
        :class:`.AsyncTransaction` object.

        .. versionadded:: 1.4.0b2

        """
        ...
    
    async def execution_options(self, **opt): # -> AsyncConnection:
        r"""Set non-SQL options for the connection which take effect
        during execution.

        This returns this :class:`_asyncio.AsyncConnection` object with
        the new options added.

        See :meth:`_future.Connection.execution_options` for full details
        on this method.

        """
        ...
    
    async def commit(self): # -> None:
        """Commit the transaction that is currently in progress.

        This method commits the current transaction if one has been started.
        If no transaction was started, the method has no effect, assuming
        the connection is in a non-invalidated state.

        A transaction is begun on a :class:`_future.Connection` automatically
        whenever a statement is first executed, or when the
        :meth:`_future.Connection.begin` method is called.

        """
        ...
    
    async def rollback(self): # -> None:
        """Roll back the transaction that is currently in progress.

        This method rolls back the current transaction if one has been started.
        If no transaction was started, the method has no effect.  If a
        transaction was started and the connection is in an invalidated state,
        the transaction is cleared using this method.

        A transaction is begun on a :class:`_future.Connection` automatically
        whenever a statement is first executed, or when the
        :meth:`_future.Connection.begin` method is called.


        """
        ...
    
    async def close(self): # -> None:
        """Close this :class:`_asyncio.AsyncConnection`.

        This has the effect of also rolling back the transaction if one
        is in place.

        """
        ...
    
    async def exec_driver_sql(self, statement, parameters=..., execution_options=...):
        r"""Executes a driver-level SQL string and return buffered
        :class:`_engine.Result`.

        """
        ...
    
    async def stream(self, statement, parameters=..., execution_options=...): # -> AsyncResult:
        """Execute a statement and return a streaming
        :class:`_asyncio.AsyncResult` object."""
        ...
    
    async def execute(self, statement, parameters=..., execution_options=...):
        r"""Executes a SQL statement construct and return a buffered
        :class:`_engine.Result`.

        :param object: The statement to be executed.  This is always
         an object that is in both the :class:`_expression.ClauseElement` and
         :class:`_expression.Executable` hierarchies, including:

         * :class:`_expression.Select`
         * :class:`_expression.Insert`, :class:`_expression.Update`,
           :class:`_expression.Delete`
         * :class:`_expression.TextClause` and
           :class:`_expression.TextualSelect`
         * :class:`_schema.DDL` and objects which inherit from
           :class:`_schema.DDLElement`

        :param parameters: parameters which will be bound into the statement.
         This may be either a dictionary of parameter names to values,
         or a mutable sequence (e.g. a list) of dictionaries.  When a
         list of dictionaries is passed, the underlying statement execution
         will make use of the DBAPI ``cursor.executemany()`` method.
         When a single dictionary is passed, the DBAPI ``cursor.execute()``
         method will be used.

        :param execution_options: optional dictionary of execution options,
         which will be associated with the statement execution.  This
         dictionary can provide a subset of the options that are accepted
         by :meth:`_future.Connection.execution_options`.

        :return: a :class:`_engine.Result` object.

        """
        ...
    
    async def scalar(self, statement, parameters=..., execution_options=...):
        r"""Executes a SQL statement construct and returns a scalar object.

        This method is shorthand for invoking the
        :meth:`_engine.Result.scalar` method after invoking the
        :meth:`_future.Connection.execute` method.  Parameters are equivalent.

        :return: a scalar Python value representing the first column of the
         first row returned.

        """
        ...
    
    async def run_sync(self, fn, *arg, **kw):
        """Invoke the given sync callable passing self as the first argument.

        This method maintains the asyncio event loop all the way through
        to the database connection by running the given callable in a
        specially instrumented greenlet.

        E.g.::

            with async_engine.begin() as conn:
                await conn.run_sync(metadata.create_all)

        .. note::

            The provided callable is invoked inline within the asyncio event
            loop, and will block on traditional IO calls.  IO within this
            callable should only call into SQLAlchemy's asyncio database
            APIs which will be properly adapted to the greenlet context.

        .. seealso::

            :ref:`session_run_sync`
        """
        ...
    
    def __await__(self): # -> Generator[Any, None, AsyncConnection]:
        ...
    
    async def __aexit__(self, type_, value, traceback): # -> None:
        ...
    


@util.create_proxy_methods(Engine, ":class:`_future.Engine`", ":class:`_asyncio.AsyncEngine`", classmethods=[], methods=["clear_compiled_cache", "update_execution_options", "get_execution_options"], attributes=["url", "pool", "dialect", "engine", "name", "driver", "echo"])
class AsyncEngine(ProxyComparable, AsyncConnectable):
    """An asyncio proxy for a :class:`_engine.Engine`.

    :class:`_asyncio.AsyncEngine` is acquired using the
    :func:`_asyncio.create_async_engine` function::

        from sqlalchemy.ext.asyncio import create_async_engine
        engine = create_async_engine("postgresql+asyncpg://user:pass@host/dbname")

    .. versionadded:: 1.4

    """
    __slots__ = ...
    _connection_cls = AsyncConnection
    _option_cls: type
    class _trans_ctx(StartableContext):
        def __init__(self, conn) -> None:
            ...
        
        async def start(self, is_ctxmanager=...):
            ...
        
        async def __aexit__(self, type_, value, traceback): # -> None:
            ...
        
    
    
    def __init__(self, sync_engine) -> None:
        ...
    
    def begin(self): # -> _trans_ctx:
        """Return a context manager which when entered will deliver an
        :class:`_asyncio.AsyncConnection` with an
        :class:`_asyncio.AsyncTransaction` established.

        E.g.::

            async with async_engine.begin() as conn:
                await conn.execute(
                    text("insert into table (x, y, z) values (1, 2, 3)")
                )
                await conn.execute(text("my_special_procedure(5)"))


        """
        ...
    
    def connect(self): # -> _connection_cls:
        """Return an :class:`_asyncio.AsyncConnection` object.

        The :class:`_asyncio.AsyncConnection` will procure a database
        connection from the underlying connection pool when it is entered
        as an async context manager::

            async with async_engine.connect() as conn:
                result = await conn.execute(select(user_table))

        The :class:`_asyncio.AsyncConnection` may also be started outside of a
        context manager by invoking its :meth:`_asyncio.AsyncConnection.start`
        method.

        """
        ...
    
    async def raw_connection(self):
        """Return a "raw" DBAPI connection from the connection pool.

        .. seealso::

            :ref:`dbapi_connections`

        """
        ...
    
    def execution_options(self, **opt): # -> AsyncEngine:
        """Return a new :class:`_asyncio.AsyncEngine` that will provide
        :class:`_asyncio.AsyncConnection` objects with the given execution
        options.

        Proxied from :meth:`_future.Engine.execution_options`.  See that
        method for details.

        """
        ...
    
    async def dispose(self):
        """Dispose of the connection pool used by this
        :class:`_asyncio.AsyncEngine`.

        This will close all connection pool connections that are
        **currently checked in**.  See the documentation for the underlying
        :meth:`_future.Engine.dispose` method for further notes.

        .. seealso::

            :meth:`_future.Engine.dispose`

        """
        ...
    


class AsyncTransaction(ProxyComparable, StartableContext):
    """An asyncio proxy for a :class:`_engine.Transaction`."""
    __slots__ = ...
    def __init__(self, connection, nested=...) -> None:
        ...
    
    @property
    def is_valid(self):
        ...
    
    @property
    def is_active(self):
        ...
    
    async def close(self): # -> None:
        """Close this :class:`.Transaction`.

        If this transaction is the base transaction in a begin/commit
        nesting, the transaction will rollback().  Otherwise, the
        method returns.

        This is used to cancel a Transaction without affecting the scope of
        an enclosing transaction.

        """
        ...
    
    async def rollback(self): # -> None:
        """Roll back this :class:`.Transaction`."""
        ...
    
    async def commit(self): # -> None:
        """Commit this :class:`.Transaction`."""
        ...
    
    async def start(self, is_ctxmanager=...): # -> AsyncTransaction:
        """Start this :class:`_asyncio.AsyncTransaction` object's context
        outside of using a Python ``with:`` block.

        """
        ...
    
    async def __aexit__(self, type_, value, traceback): # -> None:
        ...
    

