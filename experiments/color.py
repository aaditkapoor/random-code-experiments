"""
    A Color class to emulate text style functionality.
"""
from dataclasses import dataclass
from typing import Union
# import rich

@dataclass
class Color:
    """Base Color"""
    text: str
    def __repr__(self):
        raise NotImplementedError

# colors
class Red(Color):
    def __init__(self, text: str):
        super().__init__(text)
    def __repr__(self):
        return f'<red>{self.text}</red>'

class Black(Color):
    def __init__(self, text: str):
        super().__init__(text)
    def __repr__(self):
        return f'<black>{self.text}</black>'

class Green(Color):
    def __init__(self, text: str):
        super().__init__(text)
    def __repr__(self):
        return f'<green>{self.text}</green>'


# styles
class Style:
    """Base Style"""
    text: str = None
    instance: Union[Red, Black, Green,None] = None

    def __init__(self, text: str = None, instance: Union[Red, Black, Green, None] = None):
        if text and instance:
            raise Exception
        if not text:
            self.instance = instance
            self.text = None
        else:
            self.text = text
            self.instance = None
    def __repr__(self):
        raise NotImplementedError

class Bold(Style):
    def __init__(self, text: str = None, instance: Union[Red, Black, Green, None] = None):
        super().__init__(text, instance)
    def __repr__(self):
        if self.text:
            return f'<bold>{self.text}</bold>'
        else:
            return f'<bold>{repr(self.instance)}</bold>'

class Italic(Style):
    def __init__(self, text: str = None, instance: Union[Red, Black, Green, None] = None):
        super().__init__(text=text, instance=instance)
    def __repr__(self):
        if self.text:
            return f'<italic>{self.text}</italic>'
        else:
            return f'<italic>{repr(self.instance)}</italic>'

class Underline(Style):
    def __init__(self, text: str = None, instance: Union[Red, Black, Green, None] = None):
        super().__init__(text=text, instance=instance)
    def __repr__(self):
        if self.text:
            return f'<underline>{self.text}</underline>'
        else:
            return f'<underline>{repr(self.instance)}</underline>'

# Usage
print(Bold("aadit"))
print(Bold(instance=Red("aadit")))
print(Italic(instance=Bold(instance=Red("aadit"))))


