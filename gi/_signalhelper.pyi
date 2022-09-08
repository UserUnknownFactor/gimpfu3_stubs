from _typeshed import Incomplete

class Signal(str):
    class BoundSignal(str):
        def __new__(cls, name, *args, **kargs): ...
        signal: Incomplete
        gobj: Incomplete
        def __init__(self, signal, gobj) -> None: ...
        def __call__(self, *args, **kargs): ...
        def connect(self, callback, *args, **kargs): ...
        def connect_detailed(self, callback, detail, *args, **kargs): ...
        def disconnect(self, handler_id) -> None: ...
        def emit(self, *args, **kargs): ...
    def __new__(cls, name: str = ..., *args, **kargs): ...
    func: Incomplete
    flags: Incomplete
    return_type: Incomplete
    arg_types: Incomplete
    __doc__: Incomplete
    accumulator: Incomplete
    accu_data: Incomplete
    def __init__(self, name: str = ..., func: Incomplete | None = ..., flags=..., return_type: Incomplete | None = ..., arg_types: Incomplete | None = ..., doc: str = ..., accumulator: Incomplete | None = ..., accu_data: Incomplete | None = ...) -> None: ...
    def __get__(self, instance, owner: Incomplete | None = ...): ...
    def __call__(self, obj, *args, **kargs): ...
    def copy(self, newName: Incomplete | None = ...): ...
    def get_signal_args(self): ...

class SignalOverride(Signal):
    def get_signal_args(self): ...

def get_signal_annotations(func): ...
def install_signals(cls) -> None: ...
