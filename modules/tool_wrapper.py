# tool_wrapper.py

class Tool:
    def __init__(self, func, name, description):
        self.func = func
        self.name = name
        self.description = description

    def call(self, *args, **kwargs):
        return self.func(*args, **kwargs)
