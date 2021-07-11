"""
This type stub file was generated by pyright.
"""

from . import roles
from .base import CompileState, DialectKWArgs, Executable, HasCompileState, _exclusive_against, _generative
from .elements import ClauseElement
from .selectable import HasCTE, HasPrefixes, ReturnsRows

"""
Provide :class:`_expression.Insert`, :class:`_expression.Update` and
:class:`_expression.Delete`.

"""
class DMLState(CompileState):
    _no_parameters = ...
    _dict_parameters = ...
    _multi_parameters = ...
    _ordered_values = ...
    _parameter_ordering = ...
    _has_multi_parameters = ...
    isupdate = ...
    isdelete = ...
    isinsert = ...
    def __init__(self, statement, compiler, **kw) -> None:
        ...
    
    @property
    def dml_table(self):
        ...
    


@CompileState.plugin_for("default", "insert")
class InsertDMLState(DMLState):
    isinsert = ...
    include_table_with_column_exprs = ...
    def __init__(self, statement, compiler, **kw) -> None:
        ...
    


@CompileState.plugin_for("default", "update")
class UpdateDMLState(DMLState):
    isupdate = ...
    include_table_with_column_exprs = ...
    def __init__(self, statement, compiler, **kw) -> None:
        ...
    


@CompileState.plugin_for("default", "delete")
class DeleteDMLState(DMLState):
    isdelete = ...
    def __init__(self, statement, compiler, **kw) -> None:
        ...
    


class UpdateBase(roles.DMLRole, HasCTE, HasCompileState, DialectKWArgs, HasPrefixes, ReturnsRows, Executable, ClauseElement):
    """Form the base for ``INSERT``, ``UPDATE``, and ``DELETE`` statements."""
    __visit_name__ = ...
    _execution_options = ...
    _hints = ...
    named_with_column = ...
    _return_defaults = ...
    _returning = ...
    is_dml = ...
    def params(self, *arg, **kw):
        """Set the parameters for the statement.

        This method raises ``NotImplementedError`` on the base class,
        and is overridden by :class:`.ValuesBase` to provide the
        SET/VALUES clause of UPDATE and INSERT.

        """
        ...
    
    @_generative
    def with_dialect_options(self, **opt): # -> None:
        """Add dialect options to this INSERT/UPDATE/DELETE object.

        e.g.::

            upd = table.update().dialect_options(mysql_limit=10)

        .. versionadded: 1.4 - this method supersedes the dialect options
           associated with the constructor.


        """
        ...
    
    def bind(self):
        """Return a 'bind' linked to this :class:`.UpdateBase`
        or a :class:`_schema.Table` associated with it.

        """
        ...
    
    bind = ...
    @_generative
    def returning(self, *cols): # -> None:
        r"""Add a :term:`RETURNING` or equivalent clause to this statement.

        e.g.:

        .. sourcecode:: pycon+sql

            >>> stmt = (
            ...     table.update()
            ...     .where(table.c.data == "value")
            ...     .values(status="X")
            ...     .returning(table.c.server_flag, table.c.updated_timestamp)
            ... )
            >>> print(stmt)
            UPDATE some_table SET status=:status
            WHERE some_table.data = :data_1
            RETURNING some_table.server_flag, some_table.updated_timestamp

        The method may be invoked multiple times to add new entries to the
        list of expressions to be returned.

        .. versionadded:: 1.4.0b2 The method may be invoked multiple times to
         add new entries to the list of expressions to be returned.

        The given collection of column expressions should be derived from the
        table that is the target of the INSERT, UPDATE, or DELETE.  While
        :class:`_schema.Column` objects are typical, the elements can also be
        expressions:

        .. sourcecode:: pycon+sql

            >>> stmt = table.insert().returning(
            ...     (table.c.first_name + " " + table.c.last_name).label("fullname")
            ... )
            >>> print(stmt)
            INSERT INTO some_table (first_name, last_name)
            VALUES (:first_name, :last_name)
            RETURNING some_table.first_name || :first_name_1 || some_table.last_name AS fullname

        Upon compilation, a RETURNING clause, or database equivalent,
        will be rendered within the statement.   For INSERT and UPDATE,
        the values are the newly inserted/updated values.  For DELETE,
        the values are those of the rows which were deleted.

        Upon execution, the values of the columns to be returned are made
        available via the result set and can be iterated using
        :meth:`_engine.CursorResult.fetchone` and similar.
        For DBAPIs which do not
        natively support returning values (i.e. cx_oracle), SQLAlchemy will
        approximate this behavior at the result level so that a reasonable
        amount of behavioral neutrality is provided.

        Note that not all databases/DBAPIs
        support RETURNING.   For those backends with no support,
        an exception is raised upon compilation and/or execution.
        For those who do support it, the functionality across backends
        varies greatly, including restrictions on executemany()
        and other statements which return multiple rows. Please
        read the documentation notes for the database in use in
        order to determine the availability of RETURNING.

        .. seealso::

          :meth:`.ValuesBase.return_defaults` - an alternative method tailored
          towards efficient fetching of server-side defaults and triggers
          for single-row INSERTs or UPDATEs.

          :ref:`tutorial_insert_returning` - in the :ref:`unified_tutorial`

        """
        ...
    
    @property
    def exported_columns(self): # -> ImmutableColumnCollection:
        """Return the RETURNING columns as a column collection for this
        statement.

        .. versionadded:: 1.4

        """
        ...
    
    @_generative
    def with_hint(self, text, selectable=..., dialect_name=...): # -> None:
        """Add a table hint for a single table to this
        INSERT/UPDATE/DELETE statement.

        .. note::

         :meth:`.UpdateBase.with_hint` currently applies only to
         Microsoft SQL Server.  For MySQL INSERT/UPDATE/DELETE hints, use
         :meth:`.UpdateBase.prefix_with`.

        The text of the hint is rendered in the appropriate
        location for the database backend in use, relative
        to the :class:`_schema.Table` that is the subject of this
        statement, or optionally to that of the given
        :class:`_schema.Table` passed as the ``selectable`` argument.

        The ``dialect_name`` option will limit the rendering of a particular
        hint to a particular backend. Such as, to add a hint
        that only takes effect for SQL Server::

            mytable.insert().with_hint("WITH (PAGLOCK)", dialect_name="mssql")

        :param text: Text of the hint.
        :param selectable: optional :class:`_schema.Table` that specifies
         an element of the FROM clause within an UPDATE or DELETE
         to be the subject of the hint - applies only to certain backends.
        :param dialect_name: defaults to ``*``, if specified as the name
         of a particular dialect, will apply these hints only when
         that dialect is in use.
        """
        ...
    


class ValuesBase(UpdateBase):
    """Supplies support for :meth:`.ValuesBase.values` to
    INSERT and UPDATE constructs."""
    __visit_name__ = ...
    _supports_multi_parameters = ...
    _preserve_parameter_order = ...
    select = ...
    _post_values_clause = ...
    _values = ...
    _multi_values = ...
    _ordered_values = ...
    _select_names = ...
    _returning = ...
    def __init__(self, table, values, prefixes) -> None:
        ...
    
    @_generative
    @_exclusive_against("_select_names", "_ordered_values", msgs={ "_select_names": "This construct already inserts from a SELECT","_ordered_values": "This statement already has ordered " "values present" })
    def values(self, *args, **kwargs): # -> None:
        r"""Specify a fixed VALUES clause for an INSERT statement, or the SET
        clause for an UPDATE.

        Note that the :class:`_expression.Insert` and
        :class:`_expression.Update`
        constructs support
        per-execution time formatting of the VALUES and/or SET clauses,
        based on the arguments passed to :meth:`_engine.Connection.execute`.
        However, the :meth:`.ValuesBase.values` method can be used to "fix" a
        particular set of parameters into the statement.

        Multiple calls to :meth:`.ValuesBase.values` will produce a new
        construct, each one with the parameter list modified to include
        the new parameters sent.  In the typical case of a single
        dictionary of parameters, the newly passed keys will replace
        the same keys in the previous construct.  In the case of a list-based
        "multiple values" construct, each new list of values is extended
        onto the existing list of values.

        :param \**kwargs: key value pairs representing the string key
          of a :class:`_schema.Column`
          mapped to the value to be rendered into the
          VALUES or SET clause::

                users.insert().values(name="some name")

                users.update().where(users.c.id==5).values(name="some name")

        :param \*args: As an alternative to passing key/value parameters,
         a dictionary, tuple, or list of dictionaries or tuples can be passed
         as a single positional argument in order to form the VALUES or
         SET clause of the statement.  The forms that are accepted vary
         based on whether this is an :class:`_expression.Insert` or an
         :class:`_expression.Update` construct.

         For either an :class:`_expression.Insert` or
         :class:`_expression.Update`
         construct, a single dictionary can be passed, which works the same as
         that of the kwargs form::

            users.insert().values({"name": "some name"})

            users.update().values({"name": "some new name"})

         Also for either form but more typically for the
         :class:`_expression.Insert` construct, a tuple that contains an
         entry for every column in the table is also accepted::

            users.insert().values((5, "some name"))

         The :class:`_expression.Insert` construct also supports being
         passed a list of dictionaries or full-table-tuples, which on the
         server will render the less common SQL syntax of "multiple values" -
         this syntax is supported on backends such as SQLite, PostgreSQL,
         MySQL, but not necessarily others::

            users.insert().values([
                                {"name": "some name"},
                                {"name": "some other name"},
                                {"name": "yet another name"},
                            ])

         The above form would render a multiple VALUES statement similar to::

                INSERT INTO users (name) VALUES
                                (:name_1),
                                (:name_2),
                                (:name_3)

         It is essential to note that **passing multiple values is
         NOT the same as using traditional executemany() form**.  The above
         syntax is a **special** syntax not typically used.  To emit an
         INSERT statement against multiple rows, the normal method is
         to pass a multiple values list to the
         :meth:`_engine.Connection.execute`
         method, which is supported by all database backends and is generally
         more efficient for a very large number of parameters.

           .. seealso::

               :ref:`execute_multiple` - an introduction to
               the traditional Core method of multiple parameter set
               invocation for INSERTs and other statements.

           .. versionchanged:: 1.0.0 an INSERT that uses a multiple-VALUES
              clause, even a list of length one,
              implies that the :paramref:`_expression.Insert.inline`
              flag is set to
              True, indicating that the statement will not attempt to fetch
              the "last inserted primary key" or other defaults.  The
              statement deals with an arbitrary number of rows, so the
              :attr:`_engine.CursorResult.inserted_primary_key`
              accessor does not
              apply.

           .. versionchanged:: 1.0.0 A multiple-VALUES INSERT now supports
              columns with Python side default values and callables in the
              same way as that of an "executemany" style of invocation; the
              callable is invoked for each row.   See :ref:`bug_3288`
              for other details.

          The UPDATE construct also supports rendering the SET parameters
          in a specific order.  For this feature refer to the
          :meth:`_expression.Update.ordered_values` method.

           .. seealso::

              :meth:`_expression.Update.ordered_values`


        """
        ...
    
    @_generative
    @_exclusive_against("_returning", msgs={ "_returning": "RETURNING is already configured on this statement" }, defaults={ "_returning": _returning })
    def return_defaults(self, *cols): # -> None:
        """Make use of a :term:`RETURNING` clause for the purpose
        of fetching server-side expressions and defaults.

        E.g.::

            stmt = table.insert().values(data='newdata').return_defaults()

            result = connection.execute(stmt)

            server_created_at = result.returned_defaults['created_at']

        When used against a backend that supports RETURNING, all column
        values generated by SQL expression or server-side-default will be
        added to any existing RETURNING clause, provided that
        :meth:`.UpdateBase.returning` is not used simultaneously.  The column
        values will then be available on the result using the
        :attr:`_engine.CursorResult.returned_defaults` accessor as
        a dictionary,
        referring to values keyed to the :class:`_schema.Column`
        object as well as
        its ``.key``.

        This method differs from :meth:`.UpdateBase.returning` in these ways:

        1. :meth:`.ValuesBase.return_defaults` is only intended for use with an
           INSERT or an UPDATE statement that matches exactly one row per
           parameter set. While the RETURNING construct in the general sense
           supports multiple rows for a multi-row UPDATE or DELETE statement,
           or for special cases of INSERT that return multiple rows (e.g.
           INSERT from SELECT, multi-valued VALUES clause),
           :meth:`.ValuesBase.return_defaults` is intended only for an
           "ORM-style" single-row INSERT/UPDATE statement.  The row
           returned by the statement is also consumed implicitly when
           :meth:`.ValuesBase.return_defaults` is used.  By contrast,
           :meth:`.UpdateBase.returning` leaves the RETURNING result-set intact
           with a collection of any number of rows.

        2. It is compatible with the existing logic to fetch auto-generated
           primary key values, also known as "implicit returning".  Backends
           that support RETURNING will automatically make use of RETURNING in
           order to fetch the value of newly generated primary keys; while the
           :meth:`.UpdateBase.returning` method circumvents this behavior,
           :meth:`.ValuesBase.return_defaults` leaves it intact.

        3. It can be called against any backend.  Backends that don't support
           RETURNING will skip the usage of the feature, rather than raising
           an exception.  The return value of
           :attr:`_engine.CursorResult.returned_defaults` will be ``None``

        4. An INSERT statement invoked with executemany() is supported if the
           backend database driver supports the
           ``insert_executemany_returning`` feature, currently this includes
           PostgreSQL with psycopg2.  When executemany is used, the
           :attr:`_engine.CursorResult.returned_defaults_rows` and
           :attr:`_engine.CursorResult.inserted_primary_key_rows` accessors
           will return the inserted defaults and primary keys.

           .. versionadded:: 1.4

        :meth:`.ValuesBase.return_defaults` is used by the ORM to provide
        an efficient implementation for the ``eager_defaults`` feature of
        :func:`.mapper`.

        :param cols: optional list of column key names or
         :class:`_schema.Column`
         objects.  If omitted, all column expressions evaluated on the server
         are added to the returning list.

        .. versionadded:: 0.9.0

        .. seealso::

            :meth:`.UpdateBase.returning`

            :attr:`_engine.CursorResult.returned_defaults`

            :attr:`_engine.CursorResult.returned_defaults_rows`

            :attr:`_engine.CursorResult.inserted_primary_key`

            :attr:`_engine.CursorResult.inserted_primary_key_rows`

        """
        ...
    


class Insert(ValuesBase):
    """Represent an INSERT construct.

    The :class:`_expression.Insert` object is created using the
    :func:`_expression.insert()` function.

    """
    __visit_name__ = ...
    _supports_multi_parameters = ...
    select = ...
    include_insert_from_select_defaults = ...
    is_insert = ...
    _traverse_internals = ...
    @ValuesBase._constructor_20_deprecations("insert", "Insert", ["values", "inline", "bind", "prefixes", "returning", "return_defaults"])
    def __init__(self, table, values=..., inline=..., bind=..., prefixes=..., returning=..., return_defaults=..., **dialect_kw) -> None:
        """Construct an :class:`_expression.Insert` object.

        E.g.::

            from sqlalchemy import insert

            stmt = (
                insert(user_table).
                values(name='username', fullname='Full Username')
            )

        Similar functionality is available via the
        :meth:`_expression.TableClause.insert` method on
        :class:`_schema.Table`.

        .. seealso::

            :ref:`coretutorial_insert_expressions` - in the
            :ref:`1.x tutorial <sqlexpression_toplevel>`

            :ref:`tutorial_core_insert` - in the :ref:`unified_tutorial`


        :param table: :class:`_expression.TableClause`
         which is the subject of the
         insert.

        :param values: collection of values to be inserted; see
         :meth:`_expression.Insert.values`
         for a description of allowed formats here.
         Can be omitted entirely; a :class:`_expression.Insert` construct
         will also dynamically render the VALUES clause at execution time
         based on the parameters passed to :meth:`_engine.Connection.execute`.

        :param inline: if True, no attempt will be made to retrieve the
         SQL-generated default values to be provided within the statement;
         in particular,
         this allows SQL expressions to be rendered 'inline' within the
         statement without the need to pre-execute them beforehand; for
         backends that support "returning", this turns off the "implicit
         returning" feature for the statement.

        If both :paramref:`_expression.Insert.values` and compile-time bind
        parameters are present, the compile-time bind parameters override the
        information specified within :paramref:`_expression.Insert.values` on a
        per-key basis.

        The keys within :paramref:`_expression.Insert.values` can be either
        :class:`~sqlalchemy.schema.Column` objects or their string
        identifiers. Each key may reference one of:

        * a literal data value (i.e. string, number, etc.);
        * a Column object;
        * a SELECT statement.

        If a ``SELECT`` statement is specified which references this
        ``INSERT`` statement's table, the statement will be correlated
        against the ``INSERT`` statement.

        .. seealso::

            :ref:`coretutorial_insert_expressions` - SQL Expression Tutorial

            :ref:`inserts_and_updates` - SQL Expression Tutorial

        """
        ...
    
    @_generative
    def inline(self): # -> None:
        """Make this :class:`_expression.Insert` construct "inline" .

        When set, no attempt will be made to retrieve the
        SQL-generated default values to be provided within the statement;
        in particular,
        this allows SQL expressions to be rendered 'inline' within the
        statement without the need to pre-execute them beforehand; for
        backends that support "returning", this turns off the "implicit
        returning" feature for the statement.


        .. versionchanged:: 1.4 the :paramref:`_expression.Insert.inline`
           parameter
           is now superseded by the :meth:`_expression.Insert.inline` method.

        """
        ...
    
    @_generative
    def from_select(self, names, select, include_defaults=...): # -> None:
        """Return a new :class:`_expression.Insert` construct which represents
        an ``INSERT...FROM SELECT`` statement.

        e.g.::

            sel = select(table1.c.a, table1.c.b).where(table1.c.c > 5)
            ins = table2.insert().from_select(['a', 'b'], sel)

        :param names: a sequence of string column names or
         :class:`_schema.Column`
         objects representing the target columns.
        :param select: a :func:`_expression.select` construct,
         :class:`_expression.FromClause`
         or other construct which resolves into a
         :class:`_expression.FromClause`,
         such as an ORM :class:`_query.Query` object, etc.  The order of
         columns returned from this FROM clause should correspond to the
         order of columns sent as the ``names`` parameter;  while this
         is not checked before passing along to the database, the database
         would normally raise an exception if these column lists don't
         correspond.
        :param include_defaults: if True, non-server default values and
         SQL expressions as specified on :class:`_schema.Column` objects
         (as documented in :ref:`metadata_defaults_toplevel`) not
         otherwise specified in the list of names will be rendered
         into the INSERT and SELECT statements, so that these values are also
         included in the data to be inserted.

         .. note:: A Python-side default that uses a Python callable function
            will only be invoked **once** for the whole statement, and **not
            per row**.

         .. versionadded:: 1.0.0 - :meth:`_expression.Insert.from_select`
            now renders
            Python-side and SQL expression column defaults into the
            SELECT statement for columns otherwise not included in the
            list of column names.

        .. versionchanged:: 1.0.0 an INSERT that uses FROM SELECT
           implies that the :paramref:`_expression.insert.inline`
           flag is set to
           True, indicating that the statement will not attempt to fetch
           the "last inserted primary key" or other defaults.  The statement
           deals with an arbitrary number of rows, so the
           :attr:`_engine.CursorResult.inserted_primary_key`
           accessor does not apply.

        """
        ...
    


class DMLWhereBase:
    _where_criteria = ...
    @_generative
    def where(self, *whereclause): # -> None:
        """Return a new construct with the given expression(s) added to
        its WHERE clause, joined to the existing clause via AND, if any.

        Both :meth:`_dml.Update.where` and :meth:`_dml.Delete.where`
        support multiple-table forms, including database-specific
        ``UPDATE...FROM`` as well as ``DELETE..USING``.  For backends that
        don't have multiple-table support, a backend agnostic approach
        to using multiple tables is to make use of correlated subqueries.
        See the linked tutorial sections below for examples.

        .. seealso::

            **1.x Tutorial Examples**

            :ref:`tutorial_1x_correlated_updates`

            :ref:`multi_table_updates`

            :ref:`multi_table_deletes`

            **2.0 Tutorial Examples**

            :ref:`tutorial_correlated_updates`

            :ref:`tutorial_update_from`

            :ref:`tutorial_multi_table_deletes`

        """
        ...
    
    def filter(self, *criteria): # -> None:
        """A synonym for the :meth:`_dml.DMLWhereBase.where` method.

        .. versionadded:: 1.4

        """
        ...
    
    def filter_by(self, **kwargs): # -> None:
        r"""apply the given filtering criterion as a WHERE clause
        to this select.

        """
        ...
    
    @property
    def whereclause(self): # -> Any | None:
        """Return the completed WHERE clause for this :class:`.DMLWhereBase`
        statement.

        This assembles the current collection of WHERE criteria
        into a single :class:`_expression.BooleanClauseList` construct.


        .. versionadded:: 1.4

        """
        ...
    


class Update(DMLWhereBase, ValuesBase):
    """Represent an Update construct.

    The :class:`_expression.Update` object is created using the
    :func:`_expression.update()` function.

    """
    __visit_name__ = ...
    is_update = ...
    _traverse_internals = ...
    @ValuesBase._constructor_20_deprecations("update", "Update", ["whereclause", "values", "inline", "bind", "prefixes", "returning", "return_defaults", "preserve_parameter_order"])
    def __init__(self, table, whereclause=..., values=..., inline=..., bind=..., prefixes=..., returning=..., return_defaults=..., preserve_parameter_order=..., **dialect_kw) -> None:
        r"""Construct an :class:`_expression.Update` object.

        E.g.::

            from sqlalchemy import update

            stmt = (
                update(user_table).
                where(user_table.c.id == 5).
                values(name='user #5')
            )

        Similar functionality is available via the
        :meth:`_expression.TableClause.update` method on
        :class:`_schema.Table`.

        .. seealso::

            :ref:`inserts_and_updates` - in the
            :ref:`1.x tutorial <sqlexpression_toplevel>`

            :ref:`tutorial_core_update_delete` - in the :ref:`unified_tutorial`



        :param table: A :class:`_schema.Table`
         object representing the database
         table to be updated.

        :param whereclause: Optional SQL expression describing the ``WHERE``
         condition of the ``UPDATE`` statement; is equivalent to using the
         more modern :meth:`~Update.where()` method to specify the ``WHERE``
         clause.

        :param values:
          Optional dictionary which specifies the ``SET`` conditions of the
          ``UPDATE``.  If left as ``None``, the ``SET``
          conditions are determined from those parameters passed to the
          statement during the execution and/or compilation of the
          statement.   When compiled standalone without any parameters,
          the ``SET`` clause generates for all columns.

          Modern applications may prefer to use the generative
          :meth:`_expression.Update.values` method to set the values of the
          UPDATE statement.

        :param inline:
          if True, SQL defaults present on :class:`_schema.Column` objects via
          the ``default`` keyword will be compiled 'inline' into the statement
          and not pre-executed.  This means that their values will not
          be available in the dictionary returned from
          :meth:`_engine.CursorResult.last_updated_params`.

        :param preserve_parameter_order: if True, the update statement is
          expected to receive parameters **only** via the
          :meth:`_expression.Update.values` method,
          and they must be passed as a Python
          ``list`` of 2-tuples. The rendered UPDATE statement will emit the SET
          clause for each referenced column maintaining this order.

          .. versionadded:: 1.0.10

          .. seealso::

            :ref:`updates_order_parameters` - illustrates the
            :meth:`_expression.Update.ordered_values` method.

        If both ``values`` and compile-time bind parameters are present, the
        compile-time bind parameters override the information specified
        within ``values`` on a per-key basis.

        The keys within ``values`` can be either :class:`_schema.Column`
        objects or their string identifiers (specifically the "key" of the
        :class:`_schema.Column`, normally but not necessarily equivalent to
        its "name").  Normally, the
        :class:`_schema.Column` objects used here are expected to be
        part of the target :class:`_schema.Table` that is the table
        to be updated.  However when using MySQL, a multiple-table
        UPDATE statement can refer to columns from any of
        the tables referred to in the WHERE clause.

        The values referred to in ``values`` are typically:

        * a literal data value (i.e. string, number, etc.)
        * a SQL expression, such as a related :class:`_schema.Column`,
          a scalar-returning :func:`_expression.select` construct,
          etc.

        When combining :func:`_expression.select` constructs within the
        values clause of an :func:`_expression.update`
        construct, the subquery represented
        by the :func:`_expression.select` should be *correlated* to the
        parent table, that is, providing criterion which links the table inside
        the subquery to the outer table being updated::

            users.update().values(
                    name=select(addresses.c.email_address).\
                            where(addresses.c.user_id==users.c.id).\
                            scalar_subquery()
                )

        .. seealso::

            :ref:`inserts_and_updates` - SQL Expression
            Language Tutorial


        """
        ...
    
    @_generative
    def ordered_values(self, *args): # -> None:
        """Specify the VALUES clause of this UPDATE statement with an explicit
        parameter ordering that will be maintained in the SET clause of the
        resulting UPDATE statement.

        E.g.::

            stmt = table.update().ordered_values(
                ("name", "ed"), ("ident": "foo")
            )

        .. seealso::

           :ref:`updates_order_parameters` - full example of the
           :meth:`_expression.Update.ordered_values` method.

        .. versionchanged:: 1.4 The :meth:`_expression.Update.ordered_values`
           method
           supersedes the
           :paramref:`_expression.update.preserve_parameter_order`
           parameter, which will be removed in SQLAlchemy 2.0.

        """
        ...
    
    @_generative
    def inline(self): # -> None:
        """Make this :class:`_expression.Update` construct "inline" .

        When set, SQL defaults present on :class:`_schema.Column`
        objects via the
        ``default`` keyword will be compiled 'inline' into the statement and
        not pre-executed.  This means that their values will not be available
        in the dictionary returned from
        :meth:`_engine.CursorResult.last_updated_params`.

        .. versionchanged:: 1.4 the :paramref:`_expression.update.inline`
           parameter
           is now superseded by the :meth:`_expression.Update.inline` method.

        """
        ...
    


class Delete(DMLWhereBase, UpdateBase):
    """Represent a DELETE construct.

    The :class:`_expression.Delete` object is created using the
    :func:`_expression.delete()` function.

    """
    __visit_name__ = ...
    is_delete = ...
    _traverse_internals = ...
    @ValuesBase._constructor_20_deprecations("delete", "Delete", ["whereclause", "values", "bind", "prefixes", "returning"])
    def __init__(self, table, whereclause=..., bind=..., returning=..., prefixes=..., **dialect_kw) -> None:
        r"""Construct :class:`_expression.Delete` object.

        E.g.::

            from sqlalchemy import delete

            stmt = (
                delete(user_table).
                where(user_table.c.id == 5)
            )

        Similar functionality is available via the
        :meth:`_expression.TableClause.delete` method on
        :class:`_schema.Table`.

        .. seealso::

            :ref:`inserts_and_updates` - in the
            :ref:`1.x tutorial <sqlexpression_toplevel>`

            :ref:`tutorial_core_update_delete` - in the :ref:`unified_tutorial`


        :param table: The table to delete rows from.

        :param whereclause: Optional SQL expression describing the ``WHERE``
         condition of the ``DELETE`` statement; is equivalent to using the
         more modern :meth:`~Delete.where()` method to specify the ``WHERE``
         clause.

        .. seealso::

            :ref:`deletes` - SQL Expression Tutorial

        """
        ...
    


