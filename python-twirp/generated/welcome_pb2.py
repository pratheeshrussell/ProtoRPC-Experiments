# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: welcome.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rwelcome.proto\x12\x12twirp.fastapi.demo\"+\n\x04Name\x12\x11\n\tfirstname\x18\x01 \x01(\t\x12\x10\n\x08lastname\x18\x02 \x01(\t\"\x19\n\x06Result\x12\x0f\n\x07message\x18\x02 \x01(\t2K\n\x07Welcome\x12@\n\x08SayHello\x12\x18.twirp.fastapi.demo.Name\x1a\x1a.twirp.fastapi.demo.Result2J\n\x08\x46\x61rewell\x12>\n\x06SayBye\x12\x18.twirp.fastapi.demo.Name\x1a\x1a.twirp.fastapi.demo.Resultb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'welcome_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_NAME']._serialized_start=37
  _globals['_NAME']._serialized_end=80
  _globals['_RESULT']._serialized_start=82
  _globals['_RESULT']._serialized_end=107
  _globals['_WELCOME']._serialized_start=109
  _globals['_WELCOME']._serialized_end=184
  _globals['_FAREWELL']._serialized_start=186
  _globals['_FAREWELL']._serialized_end=260
# @@protoc_insertion_point(module_scope)
