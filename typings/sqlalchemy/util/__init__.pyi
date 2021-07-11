"""
This type stub file was generated by pyright.
"""

from collections import defaultdict
from contextlib import contextmanager
from functools import partial, update_wrapper
from ._collections import EMPTY_DICT, EMPTY_SET, FacadeDict, IdentitySet, ImmutableContainer, ImmutableProperties, LRUCache, OrderedDict, OrderedIdentitySet, OrderedProperties, OrderedSet, PopulateDict, Properties, ScopedRegistry, ThreadLocalRegistry, UniqueAppender, WeakPopulateDict, WeakSequence, coerce_generator_arg, coerce_to_immutabledict, collections_abc, column_dict, column_set, flatten_iterator, has_dupes, has_intersection, immutabledict, ordered_column_set, sort_dictionary, to_column_set, to_list, to_set, unique_list, update_copy
from ._preloaded import preload_module, preloaded
from .compat import ABC, StringIO, TYPE_CHECKING, arm, b, b64decode, b64encode, binary_type, byte_buffer, callable, cmp, cpython, dataclass_fields, decode_backslashreplace, dottedgetter, has_refcount_gc, inspect_getfullargspec, int_types, iterbytes, itertools_filter, itertools_filterfalse, local_dataclass_fields, namedtuple, next, nullcontext, osx, parse_qsl, perf_counter, pickle, print_, py2k, py37, py3k, pypy, quote_plus, raise_, raise_from_cause, reduce, reraise, string_types, text_type, threading, timezone, u, ue, unquote, unquote_plus, win32, with_metaclass, zip_longest
from .concurrency import asyncio, await_fallback, await_only, greenlet_spawn, is_exit_exception
from .deprecations import SQLALCHEMY_WARN_20, deprecated, deprecated_20, deprecated_20_cls, deprecated_cls, deprecated_params, inject_docstring_text, moved_20, warn_deprecated, warn_deprecated_20
from .langhelpers import EnsureKWArgType, HasMemoized, MemoizedSlots, NoneType, PluginLoader, add_parameter_text, as_interface, asbool, asint, assert_arg_type, attrsetter, bool_or_str, chop_traceback, class_hierarchy, classproperty, clsname_as_plain_name, coerce_kw_type, constructor_copy, constructor_key, counter, create_proxy_methods, decode_slice, decorator, dictlike_iteritems, duck_type_collection, ellipses_string, format_argspec_init, format_argspec_plus, generic_repr, get_callable_argspec, get_cls_kwargs, get_func_kwargs, getargspec_init, has_compiled_ext, hybridmethod, hybridproperty, iterate_attributes, map_bits, md5_hex, memoized_instancemethod, memoized_property, method_is_overridden, methods_equivalent, monkeypatch_proxied_specials, only_once, portable_instancemethod, quoted_token_parser, safe_reraise, set_creation_order, string_or_unprintable, symbol, unbound_method_to_callable, walk_subclasses, warn, warn_exception, warn_limited, wrap_callable

