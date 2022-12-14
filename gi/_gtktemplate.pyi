from _typeshed import Incomplete

class Child:
    def __init__(self, name: Incomplete | None = ..., **kwargs) -> None: ...

class CallThing:
    def __init__(self, name, func) -> None: ...

class Callback:
    def __init__(self, name: Incomplete | None = ...) -> None: ...
    def __call__(self, func): ...

class Template:
    string: Incomplete
    filename: Incomplete
    resource_path: Incomplete
    def __init__(self, **kwargs) -> None: ...
    @classmethod
    def from_file(cls, filename): ...
    @classmethod
    def from_string(cls, string): ...
    @classmethod
    def from_resource(cls, resource_path): ...
    Callback: Incomplete
    Child: Incomplete
    def __call__(self, cls): ...
