import inspect
def introspection_info(obj):
    type_obj = type(obj)                                                               # Тип объекта
    attr_obj = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]         # Атрибуты объекта
    metod_obj = [func for func in dir(obj) if callable(getattr(obj, func))]            # Методы объекта
    getmodule_obj = inspect.getmodule(obj)                                             # Модуль, к которому объект принадлежит
    return f"'type': {type_obj}, 'attributes': {attr_obj}, 'methods': {metod_obj}, 'module': {getmodule_obj}"

number_info = introspection_info(42)
print(number_info)