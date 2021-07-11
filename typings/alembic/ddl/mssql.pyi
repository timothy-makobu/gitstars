"""
This type stub file was generated by pyright.
"""

from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql.expression import ClauseElement, Executable
from .base import AddColumn, ColumnDefault, ColumnName, ColumnNullable, ColumnType, RenameTable
from .impl import DefaultImpl

class MSSQLImpl(DefaultImpl):
    __dialect__ = ...
    transactional_ddl = ...
    batch_separator = ...
    type_synonyms = ...
    identity_attrs_ignore = ...
    def __init__(self, *arg, **kw) -> None:
        ...
    
    def emit_begin(self): # -> None:
        ...
    
    def emit_commit(self): # -> None:
        ...
    
    def alter_column(self, table_name, column_name, nullable=..., server_default=..., name=..., type_=..., schema=..., existing_type=..., existing_server_default=..., existing_nullable=..., **kw): # -> None:
        ...
    
    def create_index(self, index): # -> None:
        ...
    
    def bulk_insert(self, table, rows, **kw): # -> None:
        ...
    
    def drop_column(self, table_name, column, schema=..., **kw): # -> None:
        ...
    
    def compare_server_default(self, inspector_column, metadata_column, rendered_metadata_default, rendered_inspector_default):
        ...
    


class _ExecDropConstraint(Executable, ClauseElement):
    def __init__(self, tname, colname, type_, schema) -> None:
        ...
    


class _ExecDropFKConstraint(Executable, ClauseElement):
    def __init__(self, tname, colname, schema) -> None:
        ...
    


@compiles(AddColumn, "mssql")
def visit_add_column(element, compiler, **kw): # -> str:
    ...

def mssql_add_column(compiler, column, **kw):
    ...

@compiles(ColumnNullable, "mssql")
def visit_column_nullable(element, compiler, **kw): # -> str:
    ...

@compiles(ColumnDefault, "mssql")
def visit_column_default(element, compiler, **kw): # -> str:
    ...

@compiles(ColumnName, "mssql")
def visit_rename_column(element, compiler, **kw): # -> str:
    ...

@compiles(ColumnType, "mssql")
def visit_column_type(element, compiler, **kw): # -> str:
    ...

@compiles(RenameTable, "mssql")
def visit_rename_table(element, compiler, **kw): # -> str:
    ...

