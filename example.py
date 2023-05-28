# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.1.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _example
else:
    import _example

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "this":
            set(self, name, value)
        elif name == "thisown":
            self.this.own(value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import weakref

class CallbackBase(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def run(self):
        return _example.CallbackBase_run(self)

    def __init__(self):
        if self.__class__ == CallbackBase:
            _self = None
        else:
            _self = self
        _example.CallbackBase_swiginit(self, _example.new_CallbackBase(_self, ))
    __swig_destroy__ = _example.delete_CallbackBase
    def __disown__(self):
        self.this.disown()
        _example.disown_CallbackBase(self)
        return weakref.proxy(self)

# Register CallbackBase in _example:
_example.CallbackBase_swigregister(CallbackBase)
class Callback(CallbackBase):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _example.delete_Callback

    def run(self):
        return _example.Callback_run(self)

    def __init__(self):
        if self.__class__ == Callback:
            _self = None
        else:
            _self = self
        _example.Callback_swiginit(self, _example.new_Callback(_self, ))
    def __disown__(self):
        self.this.disown()
        _example.disown_Callback(self)
        return weakref.proxy(self)

# Register Callback in _example:
_example.Callback_swigregister(Callback)
class Caller(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _example.Caller_swiginit(self, _example.new_Caller())
    __swig_destroy__ = _example.delete_Caller

    def delCallback(self):
        return _example.Caller_delCallback(self)

    def setCallback(self, cb):
        return _example.Caller_setCallback(self, cb)

    def call(self):
        return _example.Caller_call(self)

# Register Caller in _example:
_example.Caller_swigregister(Caller)

