from ._gi import CallableInfo as CallableInfo, Direction as Direction, FunctionInfo as FunctionInfo, ObjectInfo as ObjectInfo, StructInfo as StructInfo, TypeTag as TypeTag, VFuncInfo as VFuncInfo

def set_doc_string_generator(func) -> None: ...
def get_doc_string_generator(): ...
def generate_doc_string(info): ...
