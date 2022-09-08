import optparse
from _typeshed import Incomplete
from optparse import BadOptionError as BadOptionError, OptParseError as OptParseError, OptionConflictError as OptionConflictError, OptionError as OptionError, OptionValueError as OptionValueError

class Option(optparse.Option):
    TYPES: Incomplete
    ATTRS: Incomplete
    REMAINING: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class OptionGroup(optparse.OptionGroup):
    name: Incomplete
    parser: Incomplete
    help_description: Incomplete
    defaults: Incomplete
    values: Incomplete
    translation_domain: Incomplete
    def __init__(self, name, description, help_description: str = ..., option_list: Incomplete | None = ..., defaults: Incomplete | None = ..., translation_domain: Incomplete | None = ...) -> None: ...
    def get_option_group(self, parser: Incomplete | None = ...): ...
    def set_values_to_defaults(self) -> None: ...

class OptionParser(optparse.OptionParser):
    help_enabled: Incomplete
    ignore_unknown_options: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    usage: str
    def set_usage(self, usage) -> None: ...
    def add_option_group(self, *args, **kwargs) -> None: ...
    def parse_args(self, args: Incomplete | None = ..., values: Incomplete | None = ...): ...
make_option = Option
