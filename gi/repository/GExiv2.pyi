from _typeshed import Incomplete

class Metadata(GExiv2.Metadata):
    def __init__(self, path: Incomplete | None = ...) -> Metadata: ...
    def open_path(self, path) -> None: ...
    def save_file(self, path: Incomplete | None = ...) -> None: ...
    def get_date_time(self): ...
    def set_date_time(self, value) -> None: ...
    def get_exposure_time(self): ...
    def get_exif_tag_rational(self, key): ...
    def set_exif_tag_rational(self, key, fraction): ...
    def get_tags(self): ...
    def get(self, key, default: Incomplete | None = ...): ...
    def get_raw(self, key): ...
    def __iter__(self): ...
    def __contains__(self, key): ...
    def __len__(self): ...
    def __getitem__(self, key): ...
    def __delitem__(self, key) -> None: ...
    __setitem__: Incomplete
