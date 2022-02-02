from enum import IntEnum, unique

import enum_tools
from hbutils.model import int_enum_loads


@enum_tools.documentation.document_enum
@int_enum_loads(enable_int=False, name_preprocess=str.upper)
@unique
class SortOrder(IntEnum):
    FILE = 1
    PACKAGE = 2
    CLASS = 3
    ENTRY = 4

    @property
    def order_func(self):
        if self == SortOrder.FILE:
            return lambda x: x.filename or ''
        elif self == SortOrder.PACKAGE:
            return lambda x: x.package or ''
        elif self == SortOrder.CLASS:
            return lambda x: x.clazz
        elif self == SortOrder.ENTRY:
            return lambda x: x.full_name
        else:
            raise ValueError(f'Unknown sort order - {repr(self)}.')  # pragma: no cover


DEFAULT_SORT_ORDER = SortOrder.FILE
