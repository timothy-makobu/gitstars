"""
This type stub file was generated by pyright.
"""

from .base import Pool
from .. import util
from ..util import queue as sqla_queue

"""Pool implementation classes.

"""
class QueuePool(Pool):
    """A :class:`_pool.Pool`
    that imposes a limit on the number of open connections.

    :class:`.QueuePool` is the default pooling implementation used for
    all :class:`_engine.Engine` objects, unless the SQLite dialect is in use.

    """
    _is_asyncio = ...
    _queue_class = sqla_queue.Queue
    def __init__(self, creator, pool_size=..., max_overflow=..., timeout=..., use_lifo=..., **kw) -> None:
        r"""
        Construct a QueuePool.

        :param creator: a callable function that returns a DB-API
          connection object, same as that of :paramref:`_pool.Pool.creator`.

        :param pool_size: The size of the pool to be maintained,
          defaults to 5. This is the largest number of connections that
          will be kept persistently in the pool. Note that the pool
          begins with no connections; once this number of connections
          is requested, that number of connections will remain.
          ``pool_size`` can be set to 0 to indicate no size limit; to
          disable pooling, use a :class:`~sqlalchemy.pool.NullPool`
          instead.

        :param max_overflow: The maximum overflow size of the
          pool. When the number of checked-out connections reaches the
          size set in pool_size, additional connections will be
          returned up to this limit. When those additional connections
          are returned to the pool, they are disconnected and
          discarded. It follows then that the total number of
          simultaneous connections the pool will allow is pool_size +
          `max_overflow`, and the total number of "sleeping"
          connections the pool will allow is pool_size. `max_overflow`
          can be set to -1 to indicate no overflow limit; no limit
          will be placed on the total number of concurrent
          connections. Defaults to 10.

        :param timeout: The number of seconds to wait before giving up
          on returning a connection. Defaults to 30.0. This can be a float
          but is subject to the limitations of Python time functions which
          may not be reliable in the tens of milliseconds.

        :param use_lifo: use LIFO (last-in-first-out) when retrieving
          connections instead of FIFO (first-in-first-out). Using LIFO, a
          server-side timeout scheme can reduce the number of connections used
          during non-peak periods of use.   When planning for server-side
          timeouts, ensure that a recycle or pre-ping strategy is in use to
          gracefully handle stale connections.

          .. versionadded:: 1.3

          .. seealso::

            :ref:`pool_use_lifo`

            :ref:`pool_disconnects`

        :param \**kw: Other keyword arguments including
          :paramref:`_pool.Pool.recycle`, :paramref:`_pool.Pool.echo`,
          :paramref:`_pool.Pool.reset_on_return` and others are passed to the
          :class:`_pool.Pool` constructor.

        """
        ...
    
    def recreate(self): # -> QueuePool:
        ...
    
    def dispose(self): # -> None:
        ...
    
    def status(self): # -> str:
        ...
    
    def size(self):
        ...
    
    def timeout(self): # -> Unknown:
        ...
    
    def checkedin(self): # -> int:
        ...
    
    def overflow(self): # -> int:
        ...
    
    def checkedout(self):
        ...
    


class AsyncAdaptedQueuePool(QueuePool):
    _is_asyncio = ...
    _queue_class = sqla_queue.AsyncAdaptedQueue
    _dialect = ...


class FallbackAsyncAdaptedQueuePool(AsyncAdaptedQueuePool):
    _queue_class = sqla_queue.FallbackAsyncAdaptedQueue


class NullPool(Pool):
    """A Pool which does not pool connections.

    Instead it literally opens and closes the underlying DB-API connection
    per each connection open/close.

    Reconnect-related functions such as ``recycle`` and connection
    invalidation are not supported by this Pool implementation, since
    no connections are held persistently.

    """
    def status(self): # -> Literal['NullPool']:
        ...
    
    def recreate(self): # -> NullPool:
        ...
    
    def dispose(self): # -> None:
        ...
    


class SingletonThreadPool(Pool):
    """A Pool that maintains one connection per thread.

    Maintains one connection per each thread, never moving a connection to a
    thread other than the one which it was created in.

    .. warning::  the :class:`.SingletonThreadPool` will call ``.close()``
       on arbitrary connections that exist beyond the size setting of
       ``pool_size``, e.g. if more unique **thread identities**
       than what ``pool_size`` states are used.   This cleanup is
       non-deterministic and not sensitive to whether or not the connections
       linked to those thread identities are currently in use.

       :class:`.SingletonThreadPool` may be improved in a future release,
       however in its current status it is generally used only for test
       scenarios using a SQLite ``:memory:`` database and is not recommended
       for production use.


    Options are the same as those of :class:`_pool.Pool`, as well as:

    :param pool_size: The number of threads in which to maintain connections
        at once.  Defaults to five.

    :class:`.SingletonThreadPool` is used by the SQLite dialect
    automatically when a memory-based database is used.
    See :ref:`sqlite_toplevel`.

    """
    _is_asyncio = ...
    def __init__(self, creator, pool_size=..., **kw) -> None:
        ...
    
    def recreate(self): # -> SingletonThreadPool:
        ...
    
    def dispose(self): # -> None:
        """Dispose of this pool."""
        ...
    
    def status(self): # -> str:
        ...
    
    def connect(self): # -> Any | _ConnectionFairy:
        ...
    


class StaticPool(Pool):
    """A Pool of exactly one connection, used for all requests.

    Reconnect-related functions such as ``recycle`` and connection
    invalidation (which is also used to support auto-reconnect) are only
    partially supported right now and may not yield good results.


    """
    @util.memoized_property
    def connection(self): # -> _ConnectionRecord:
        ...
    
    def status(self): # -> Literal['StaticPool']:
        ...
    
    def dispose(self): # -> None:
        ...
    
    def recreate(self): # -> StaticPool:
        ...
    


class AssertionPool(Pool):
    """A :class:`_pool.Pool` that allows at most one checked out connection at
    any given time.

    This will raise an exception if more than one connection is checked out
    at a time.  Useful for debugging code that is using more connections
    than desired.

    """
    def __init__(self, *args, **kw) -> None:
        ...
    
    def status(self): # -> Literal['AssertionPool']:
        ...
    
    def dispose(self): # -> None:
        ...
    
    def recreate(self): # -> AssertionPool:
        ...
    


