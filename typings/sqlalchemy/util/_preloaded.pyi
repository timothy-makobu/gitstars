"""
This type stub file was generated by pyright.
"""

"""supplies the "preloaded" registry to resolve circular module imports at
runtime.

"""
class _ModuleRegistry:
    """Registry of modules to load in a package init file.

    To avoid potential thread safety issues for imports that are deferred
    in a function, like https://bugs.python.org/issue38884, these modules
    are added to the system module cache by importing them after the packages
    has finished initialization.

    A global instance is provided under the name :attr:`.preloaded`. Use
    the function :func:`.preload_module` to register modules to load and
    :meth:`.import_prefix` to load all the modules that start with the
    given path.

    While the modules are loaded in the global module cache, it's advisable
    to access them using :attr:`.preloaded` to ensure that it was actually
    registered. Each registered module is added to the instance ``__dict__``
    in the form `<package>_<module>`, omitting ``sqlalchemy`` from the package
    name. Example: ``sqlalchemy.sql.util`` becomes ``preloaded.sql_util``.
    """
    def __init__(self, prefix=...) -> None:
        ...
    
    def preload_module(self, *deps): # -> (fn: Unknown) -> Unknown:
        """Adds the specified modules to the list to load.

        This method can be used both as a normal function and as a decorator.
        No change is performed to the decorated object.
        """
        ...
    
    def import_prefix(self, path): # -> None:
        """Resolve all the modules in the registry that start with the
        specified path.
        """
        ...
    


preloaded = ...
preload_module = ...
