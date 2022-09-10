import gi as __gi
import gobject as __gobject
from _typeshed import Incomplete


def module_build_path(directory: str, module_name: str) -> str: ...
def module_error() -> str: ...
def module_error_quark() -> int: ...
def module_supported() -> bool: ...


class Module(__gi.Struct):
    @staticmethod
    def build_path(directory: str, module_name: str) -> str: ...
    def close(self) -> bool: ...
    @staticmethod
    def error() -> str: ...
    @staticmethod
    def error_quark() -> int: ...
    def make_resident(self) -> None: ...
    def name(self) -> str: ...
    @staticmethod
    def supported() -> bool: ...
    def symbol(self, symbol_name: str) -> tuple[bool, symbol]: ...
    def __delattr__(self, name) -> None: ...
    @staticmethod
    def __dir__() -> None: ...
    def __eq__(self, *args, **kwargs): ...
    def __format__(self, *args, **kwargs) -> None: ...
    def __getattribute__(self, *args, **kwargs) -> None: ...
    def __ge__(self, *args, **kwargs): ...
    def __gt__(self, *args, **kwargs): ...
    def __hash__(self): ...
    def __init_subclass__(self, *args, **kwargs) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __le__(self, *args, **kwargs): ...
    def __lt__(self, *args, **kwargs): ...
    @staticmethod
    def __new__(*args, **kwargs) -> None: ...
    def __ne__(self, *args, **kwargs): ...
    def __reduce_ex__(self, *args, **kwargs) -> None: ...
    def __reduce__(self, *args, **kwargs) -> None: ...
    def __setattr__(self, name, value) -> None: ...
    def __sizeof__(self, *args, **kwargs) -> None: ...
    def __subclasshook__(self, *args, **kwargs) -> None: ...

class ModuleError(__gobject.GEnum):
    G_MODULE_ERROR_FAILED: int
    G_MODULE_ERROR_CHECK_FAILED: int
    @staticmethod
    def as_integer_ratio() -> None: ...
    @staticmethod
    def bit_count() -> None: ...
    @staticmethod
    def bit_length() -> None: ...
    def conjugate(self, *args, **kwargs) -> None: ...
    def from_bytes(self, *args, **kwargs) -> None: ...
    def to_bytes(self, *args, **kwargs) -> None: ...
    def __abs__(self) -> None: ...
    def __add__(self, *args, **kwargs) -> None: ...
    def __and__(self, *args, **kwargs) -> None: ...
    def __bool__(self, *args, **kwargs) -> None: ...
    def __ceil__(self, *args, **kwargs) -> None: ...
    def __delattr__(self, name) -> None: ...
    @staticmethod
    def __dir__() -> None: ...
    def __divmod__(self, value) -> None: ...
    def __eq__(self, *args, **kwargs): ...
    def __float__(self) -> None: ...
    def __floordiv__(self, *args, **kwargs) -> None: ...
    def __floor__(self, *args, **kwargs) -> None: ...
    def __format__(self, *args, **kwargs) -> None: ...
    def __getattribute__(self, *args, **kwargs) -> None: ...
    def __getnewargs__(self, *args, **kwargs) -> None: ...
    def __ge__(self, *args, **kwargs): ...
    def __gt__(self, *args, **kwargs): ...
    def __hash__(self): ...
    def __index__(self, *args, **kwargs) -> None: ...
    def __init_subclass__(self, *args, **kwargs) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __int__(self) -> None: ...
    def __invert__(self, *args, **kwargs) -> None: ...
    def __le__(self, *args, **kwargs): ...
    def __lshift__(self, *args, **kwargs) -> None: ...
    def __lt__(self, *args, **kwargs): ...
    def __mod__(self, *args, **kwargs) -> None: ...
    def __mul__(self, *args, **kwargs) -> None: ...
    def __neg__(self, *args, **kwargs) -> None: ...
    @staticmethod
    def __new__(*args, **kwargs) -> None: ...
    def __ne__(self, *args, **kwargs): ...
    def __or__(self, *args, **kwargs) -> None: ...
    def __pos__(self, *args, **kwargs) -> None: ...
    def __pow__(self, value, mod) -> None: ...
    def __radd__(self, *args, **kwargs) -> None: ...
    def __rand__(self, *args, **kwargs) -> None: ...
    def __rdivmod__(self, *args, **kwargs) -> None: ...
    def __reduce_ex__(self, *args, **kwargs) -> None: ...
    def __reduce__(self, *args, **kwargs) -> None: ...
    def __rfloordiv__(self, *args, **kwargs) -> None: ...
    def __rlshift__(self, *args, **kwargs) -> None: ...
    def __rmod__(self, *args, **kwargs) -> None: ...
    def __rmul__(self, *args, **kwargs) -> None: ...
    def __ror__(self, *args, **kwargs) -> None: ...
    def __round__(self, *args, **kwargs) -> None: ...
    def __rpow__(self, *args, **kwargs) -> None: ...
    def __rrshift__(self, *args, **kwargs) -> None: ...
    def __rshift__(self, *args, **kwargs) -> None: ...
    def __rsub__(self, *args, **kwargs) -> None: ...
    def __rtruediv__(self, *args, **kwargs) -> None: ...
    def __rxor__(self, *args, **kwargs) -> None: ...
    def __setattr__(self, name, value) -> None: ...
    def __sizeof__(self, *args, **kwargs) -> None: ...
    def __subclasshook__(self, *args, **kwargs) -> None: ...
    def __sub__(self, *args, **kwargs) -> None: ...
    def __truediv__(self, *args, **kwargs) -> None: ...
    def __trunc__(self, *args, **kwargs) -> None: ...
    def __xor__(self, *args, **kwargs) -> None: ...
    denominator: Incomplete
    imag: Incomplete
    numerator: Incomplete
    real: Incomplete
    value_name: Incomplete
    value_nick: Incomplete
    CHECK_FAILED: int
    FAILED: int

class ModuleFlags(__gobject.GFlags):
    G_MODULE_BIND_LAZY: int
    G_MODULE_BIND_LOCAL: int
    G_MODULE_BIND_MASK: int
    @staticmethod
    def as_integer_ratio() -> None: ...
    @staticmethod
    def bit_count() -> None: ...
    @staticmethod
    def bit_length() -> None: ...
    def conjugate(self, *args, **kwargs) -> None: ...
    def from_bytes(self, *args, **kwargs) -> None: ...
    def to_bytes(self, *args, **kwargs) -> None: ...
    def __abs__(self) -> None: ...
    def __add__(self, *args, **kwargs) -> None: ...
    def __and__(self, *args, **kwargs) -> None: ...
    def __bool__(self, *args, **kwargs) -> None: ...
    def __ceil__(self, *args, **kwargs) -> None: ...
    def __delattr__(self, name) -> None: ...
    @staticmethod
    def __dir__() -> None: ...
    def __divmod__(self, value) -> None: ...
    def __eq__(self, *args, **kwargs): ...
    def __float__(self) -> None: ...
    def __floordiv__(self, *args, **kwargs) -> None: ...
    def __floor__(self, *args, **kwargs) -> None: ...
    def __format__(self, *args, **kwargs) -> None: ...
    def __getattribute__(self, *args, **kwargs) -> None: ...
    def __getnewargs__(self, *args, **kwargs) -> None: ...
    def __ge__(self, *args, **kwargs): ...
    def __gt__(self, *args, **kwargs): ...
    def __hash__(self): ...
    def __index__(self, *args, **kwargs) -> None: ...
    def __init_subclass__(self, *args, **kwargs) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __int__(self) -> None: ...
    def __invert__(self, *args, **kwargs) -> None: ...
    def __le__(self, *args, **kwargs): ...
    def __lshift__(self, *args, **kwargs) -> None: ...
    def __lt__(self, *args, **kwargs): ...
    def __mod__(self, *args, **kwargs) -> None: ...
    def __mul__(self, *args, **kwargs) -> None: ...
    def __neg__(self, *args, **kwargs) -> None: ...
    @staticmethod
    def __new__(*args, **kwargs) -> None: ...
    def __ne__(self, *args, **kwargs): ...
    def __or__(self, *args, **kwargs) -> None: ...
    def __pos__(self, *args, **kwargs) -> None: ...
    def __pow__(self, value, mod) -> None: ...
    def __radd__(self, *args, **kwargs) -> None: ...
    def __rand__(self, *args, **kwargs) -> None: ...
    def __rdivmod__(self, *args, **kwargs) -> None: ...
    def __reduce_ex__(self, *args, **kwargs) -> None: ...
    def __reduce__(self, *args, **kwargs) -> None: ...
    def __rfloordiv__(self, *args, **kwargs) -> None: ...
    def __rlshift__(self, *args, **kwargs) -> None: ...
    def __rmod__(self, *args, **kwargs) -> None: ...
    def __rmul__(self, *args, **kwargs) -> None: ...
    def __ror__(self, *args, **kwargs) -> None: ...
    def __round__(self, *args, **kwargs) -> None: ...
    def __rpow__(self, *args, **kwargs) -> None: ...
    def __rrshift__(self, *args, **kwargs) -> None: ...
    def __rshift__(self, *args, **kwargs) -> None: ...
    def __rsub__(self, *args, **kwargs) -> None: ...
    def __rtruediv__(self, *args, **kwargs) -> None: ...
    def __rxor__(self, *args, **kwargs) -> None: ...
    def __setattr__(self, name, value) -> None: ...
    def __sizeof__(self, *args, **kwargs) -> None: ...
    def __subclasshook__(self, *args, **kwargs) -> None: ...
    def __sub__(self, *args, **kwargs) -> None: ...
    def __truediv__(self, *args, **kwargs) -> None: ...
    def __trunc__(self, *args, **kwargs) -> None: ...
    def __xor__(self, *args, **kwargs) -> None: ...
    denominator: Incomplete
    first_value_name: Incomplete
    first_value_nick: Incomplete
    imag: Incomplete
    numerator: Incomplete
    real: Incomplete
    value_names: Incomplete
    value_nicks: Incomplete
    LAZY: int
    LOCAL: int
    MASK: int

class __class__:
    def __delattr__(self, name) -> None: ...
    def __dir__(self) -> None: ...
    def __eq__(self, *args, **kwargs): ...
    def __format__(self, *args, **kwargs) -> None: ...
    def __getattribute__(self, *args, **kwargs) -> None: ...
    def __getattr__(self, name) -> None: ...
    def __ge__(self, *args, **kwargs): ...
    def __gt__(self, *args, **kwargs): ...
    def __hash__(self): ...
    def __init_subclass__(self, *args, **kwargs) -> None: ...
    def __init__(self, namespace, version: Incomplete | None = ...) -> None: ...
    def __le__(self, *args, **kwargs): ...
    def __lt__(self, *args, **kwargs): ...
    @staticmethod
    def __new__(*args, **kwargs) -> None: ...
    def __ne__(self, *args, **kwargs): ...
    def __reduce_ex__(self, *args, **kwargs) -> None: ...
    def __reduce__(self, *args, **kwargs) -> None: ...
    def __setattr__(self, name, value) -> None: ...
    def __sizeof__(self, *args, **kwargs) -> None: ...
    def __subclasshook__(self, *args, **kwargs) -> None: ...

__loader__: Incomplete
__path__: Incomplete
__spec__: Incomplete
