import os
import imp
import inspect
import re

def _fetch_entity(script_filepath, regex, entity, def_within=True):
    script_name = os.path.basename(script_filepath)
    # mod_name = os.path.splitext(script_name)[0]
    mod_name = inspect.getmodulename(script_filepath)
    mod = imp.load_source(mod_name, script_filepath)

    funcs = []
    for func in inspect.getmembers(mod, entity):
        if def_within:
            if mod_name != func[1].__module__:
                continue
        func_name = func[0]
        m = re.match(regex, func_name)
        if m:
            funcs.append(func[1])

    return funcs


def fetch_functions(script_filepath, regex):
    return _fetch_entity(script_filepath, regex, inspect.isfunction)

def fetch_classes(script_filepath, regex):
    return _fetch_entity(script_filepath, regex, inspect.isclass)