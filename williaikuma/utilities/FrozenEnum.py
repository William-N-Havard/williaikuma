#!usr/bin/env python
#-*- coding: utf8 -*-
#
# -----------------------------------------------------------------------------
#   File: ${FILE_NAME} (as part of project Williaikuma)
#   Created: 20/04/2023 12:23
#   Last Modified: 20/04/2023 12:23
# -----------------------------------------------------------------------------
#   Author: William N. Havard
#           Postdoctoral Researcher
#
#   Mail  : william.havard@ens.fr / william.havard@gmail.com
#  
#   Institution: ENS / Laboratoire de Sciences Cognitives et Psycholinguistique
#
# ------------------------------------------------------------------------------
#   Description: 
#       • 
# -----------------------------------------------------------------------------
from enum import Enum, EnumMeta


class FrozenEnum(EnumMeta):
    """
    This EnumMeta allows the subclass to call the _accessed() function
    everytime a member of the class is accessed.
    Most code from https://stackoverflow.com/questions/54274002/python-enum-prevent-invalid-attribute-assignment
    """
    def __new__(mcls, name, bases, classdict):
        classdict['__frozenenummeta_creating_class__'] = True
        enum = super().__new__(mcls, name, bases, classdict)
        del enum.__frozenenummeta_creating_class__
        return enum

    def __call__(cls, value, names=None, *, module=None, **kwargs):
        if names is None:  # simple value lookup
            return cls.__new__(cls, value)
        enum = Enum._create_(value, names, module=module, **kwargs)
        enum.__class__ = type(cls)
        return enum

    def __setattr__(cls, name, value):
        members = cls.__dict__.get('_member_map_', {})
        if hasattr(cls, '__frozenenummeta_creating_class__') or name in members:
            return super().__setattr__(name, value)
        if hasattr(cls, name):
            msg = "{!r} object attribute {!r} is read-only"
        else:
            msg = "{!r} object has no attribute {!r}"
        raise AttributeError(msg.format(cls.__name__, name))

    def __delattr__(cls, name):
        members = cls.__dict__.get('_member_map_', {})
        if hasattr(cls, '__frozenenummeta_creating_class__') or name in members:
            return super().__delattr__(name)
        if hasattr(cls, name):
            msg = "{!r} object attribute {!r} is read-only"
        else:
            msg = "{!r} object has no attribute {!r}"
        raise AttributeError(msg.format(cls.__name__, name))

    def __getattribute__(cls, name):
        obj = super().__getattribute__(name)
        if isinstance(obj, cls):
            obj = obj._accessed()
        return obj
