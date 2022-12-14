import gi as __gi
import gobject as __gobject
from _typeshed import Incomplete


ALPHA_FLOOR: int
ALPHA_FLOOR_F: int
MAJOR_VERSION: int
MICRO_VERSION: int
MINOR_VERSION: int

def component(name: str) -> Babl.Object: ...
def conversion_get_destination_space(conversion: Babl.Object) -> Babl.Object: ...
def conversion_get_source_space(conversion: Babl.Object) -> Babl.Object: ...
def exit() -> None: ...
def fast_fish(source_format, destination_format, performance: str) -> Babl.Object: ...
def fish(source_format, destination_format) -> Babl.Object: ...
def format(encoding: str) -> Babl.Object: ...
def format_exists(name: str) -> int: ...
def format_get_bytes_per_pixel(format: Babl.Object) -> int: ...
def format_get_encoding(babl: Babl.Object) -> str: ...
def format_get_model(format: Babl.Object) -> Babl.Object: ...
def format_get_n_components(format: Babl.Object) -> int: ...
def format_get_space(format: Babl.Object) -> Babl.Object: ...
def format_get_type(format: Babl.Object, component_index: int) -> Babl.Object: ...
def format_has_alpha(format: Babl.Object) -> int: ...
def format_is_format_n(format: Babl.Object) -> int: ...
def format_is_palette(format: Babl.Object) -> int: ...
def format_n(type: Babl.Object, components: int) -> Babl.Object: ...
def format_with_space(encoding: str, space: Babl.Object) -> Babl.Object: ...
def get_model_flags(model: Babl.Object) -> Babl.ModelFlag: ...
def get_name(babl: Babl.Object) -> str: ...
def get_version() -> tuple[None, None, None]: ...
def icc_get_key(icc_data: str, icc_length: int, key: str, language: str, country: str) -> str: ...
def icc_make_space(icc_data: str, icc_length: int, intent: Babl.IccIntent, error: str) -> Babl.Object: ...
def init() -> None: ...
def introspect(babl: Babl.Object): ...
def model(name: str) -> Babl.Object: ...
def model_is(babl: Babl.Object, model_name: str) -> int: ...
def model_with_space(name: str, space: Babl.Object) -> Babl.Object: ...
def new_palette(name: str, format_u8: Babl.Object, format_u8_with_alpha: Babl.Object) -> Babl.Object: ...
def new_palette_with_space(name: str, space: Babl.Object, format_u8: Babl.Object, format_u8_with_alpha: Babl.Object) -> Babl.Object: ...
def palette_reset(babl: Babl.Object): ...
def palette_set_palette(babl: Babl.Object, format: Babl.Object, data: list, count: int): ...
def process(babl_fish: Babl.Object, source, destination, n: int) -> int: ...
def process_rows(babl_fish: Babl.Object, source, source_stride: int, dest, dest_stride: int, n: int, rows: int) -> int: ...
def sampling(horizontal: int, vertical: int) -> Babl.Object: ...
def space(name: str) -> Babl.Object: ...
def space_from_chromaticities(name: str, wx: float, wy: float, rx: float, ry: float, gx: float, gy: float, bx: float, by: float, trc_red: Babl.Object, trc_green: Babl.Object, trc_blue: Babl.Object, flags: Babl.SpaceFlags) -> Babl.Object: ...
def space_from_icc(icc_data: str, icc_length: int, intent: Babl.IccIntent) -> tuple[Babl.Object, None]: ...
def space_from_rgbxyz_matrix(name: str, wx: float, wy: float, wz: float, rx: float, gx: float, bx: float, ry: float, gy: float, by: float, rz: float, gz: float, bz: float, trc_red: Babl.Object, trc_green: Babl.Object, trc_blue: Babl.Object) -> Babl.Object: ...
def space_get(space: Babl.Object) -> tuple[None, None, None, None, None, None, None, None, None, None, None]: ...
def space_get_gamma(space: Babl.Object) -> float: ...
def space_get_icc(babl: Babl.Object) -> tuple[str, None]: ...
def space_get_rgb_luminance(space: Babl.Object) -> tuple[None, None, None]: ...
def space_is_cmyk(space: Babl.Object) -> int: ...
def space_is_gray(space: Babl.Object) -> int: ...
def space_with_trc(space: Babl.Object, trc: Babl.Object) -> Babl.Object: ...
def trc(name: str) -> Babl.Object: ...
def trc_gamma(gamma: float) -> Babl.Object: ...
def type(name: str) -> Babl.Object: ...

class IccIntent(__gobject.GEnum):
    BABL_ICC_INTENT_PERCEPTUAL: int
    BABL_ICC_INTENT_RELATIVE_COLORIMETRIC: int
    BABL_ICC_INTENT_SATURATION: int
    BABL_ICC_INTENT_ABSOLUTE_COLORIMETRIC: int
    BABL_ICC_INTENT_PERFORMANCE: int
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
    ABSOLUTE_COLORIMETRIC: int
    PERCEPTUAL: int
    PERFORMANCE: int
    RELATIVE_COLORIMETRIC: int
    SATURATION: int

class ModelFlag(__gobject.GFlags):
    BABL_MODEL_FLAG_ALPHA: int
    BABL_MODEL_FLAG_ASSOCIATED: int
    BABL_MODEL_FLAG_INVERTED: int
    BABL_MODEL_FLAG_LINEAR: int
    BABL_MODEL_FLAG_NONLINEAR: int
    BABL_MODEL_FLAG_PERCEPTUAL: int
    BABL_MODEL_FLAG_GRAY: int
    BABL_MODEL_FLAG_RGB: int
    BABL_MODEL_FLAG_CIE: int
    BABL_MODEL_FLAG_CMYK: int
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
    ALPHA: int
    ASSOCIATED: int
    CIE: int
    CMYK: int
    GRAY: int
    INVERTED: int
    LINEAR: int
    NONLINEAR: int
    PERCEPTUAL: int
    RGB: int

class Object(__gi.Struct):
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

class SpaceFlags(__gobject.GEnum):
    BABL_SPACE_FLAG_NONE: int
    BABL_SPACE_FLAG_EQUALIZE: int
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
    EQUALIZE: int
    NONE: int

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
