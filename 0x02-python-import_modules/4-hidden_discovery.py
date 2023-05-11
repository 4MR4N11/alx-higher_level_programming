#!/usr/bin/python3.8
if __name__ == "__main__":
    import importlib.util
    spec = importlib.util.spec_from_file_location("hidden_4", "./hidden_4.pyc")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    names = dir(module)
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)
