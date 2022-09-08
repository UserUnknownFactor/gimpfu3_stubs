from ._constants import TYPE_BOOLEAN as TYPE_BOOLEAN, TYPE_BOXED as TYPE_BOXED, TYPE_CHAR as TYPE_CHAR, TYPE_DOUBLE as TYPE_DOUBLE, TYPE_ENUM as TYPE_ENUM, TYPE_FLAGS as TYPE_FLAGS, TYPE_FLOAT as TYPE_FLOAT, TYPE_GTYPE as TYPE_GTYPE, TYPE_INT as TYPE_INT, TYPE_INT64 as TYPE_INT64, TYPE_INTERFACE as TYPE_INTERFACE, TYPE_LONG as TYPE_LONG, TYPE_NONE as TYPE_NONE, TYPE_OBJECT as TYPE_OBJECT, TYPE_PARAM as TYPE_PARAM, TYPE_POINTER as TYPE_POINTER, TYPE_PYOBJECT as TYPE_PYOBJECT, TYPE_STRING as TYPE_STRING, TYPE_STRV as TYPE_STRV, TYPE_UCHAR as TYPE_UCHAR, TYPE_UINT as TYPE_UINT, TYPE_UINT64 as TYPE_UINT64, TYPE_ULONG as TYPE_ULONG, TYPE_VARIANT as TYPE_VARIANT
from _typeshed import Incomplete

G_MAXFLOAT: Incomplete
G_MAXDOUBLE: Incomplete
G_MININT: Incomplete
G_MAXINT: Incomplete
G_MAXUINT: Incomplete
G_MINLONG: Incomplete
G_MAXLONG: Incomplete
G_MAXULONG: Incomplete

class Property:
    class __metaclass__(type): ...
    name: Incomplete
    type: Incomplete
    default: Incomplete
    nick: Incomplete
    blurb: Incomplete
    __doc__: Incomplete
    flags: Incomplete
    fset: Incomplete
    minimum: Incomplete
    maximum: Incomplete
    def __init__(self, getter: Incomplete | None = ..., setter: Incomplete | None = ..., type: Incomplete | None = ..., default: Incomplete | None = ..., nick: str = ..., blurb: str = ..., flags=..., minimum: Incomplete | None = ..., maximum: Incomplete | None = ...) -> None: ...
    def __get__(self, instance, klass): ...
    def __set__(self, instance, value) -> None: ...
    def __call__(self, fget): ...
    fget: Incomplete
    def getter(self, fget): ...
    def setter(self, fset): ...
    def get_pspec_args(self): ...

def install_properties(cls): ...
