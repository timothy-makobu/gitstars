"""
This type stub file was generated by pyright.
"""

from . import base

class MockConnection(base.Connectable):
    def __init__(self, dialect, execute) -> None:
        ...
    
    engine = ...
    dialect = ...
    name = ...
    def schema_for_object(self, obj):
        ...
    
    def connect(self, **kwargs): # -> MockConnection:
        ...
    
    def execution_options(self, **kw): # -> MockConnection:
        ...
    
    def compiler(self, statement, parameters, **kwargs):
        ...
    
    def create(self, entity, **kwargs): # -> None:
        ...
    
    def drop(self, entity, **kwargs): # -> None:
        ...
    
    def execute(self, object_, *multiparams, **params):
        ...
    


def create_mock_engine(url, executor, **kw): # -> MockConnection:
    """Create a "mock" engine used for echoing DDL.

    This is a utility function used for debugging or storing the output of DDL
    sequences as generated by :meth:`_schema.MetaData.create_all`
    and related methods.

    The function accepts a URL which is used only to determine the kind of
    dialect to be used, as well as an "executor" callable function which
    will receive a SQL expression object and parameters, which can then be
    echoed or otherwise printed.   The executor's return value is not handled,
    nor does the engine allow regular string statements to be invoked, and
    is therefore only useful for DDL that is sent to the database without
    receiving any results.

    E.g.::

        from sqlalchemy import create_mock_engine

        def dump(sql, *multiparams, **params):
            print(sql.compile(dialect=engine.dialect))

        engine = create_mock_engine('postgresql://', dump)
        metadata.create_all(engine, checkfirst=False)

    :param url: A string URL which typically needs to contain only the
     database backend name.

    :param executor: a callable which receives the arguments ``sql``,
     ``*multiparams`` and ``**params``.  The ``sql`` parameter is typically
     an instance of :class:`.DDLElement`, which can then be compiled into a
     string using :meth:`.DDLElement.compile`.

    .. versionadded:: 1.4 - the :func:`.create_mock_engine` function replaces
       the previous "mock" engine strategy used with
       :func:`_sa.create_engine`.

    .. seealso::

        :ref:`faq_ddl_as_string`

    """
    ...

