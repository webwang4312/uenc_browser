# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: block.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import transaction_pb2 as transaction__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='block.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0b\x62lock.proto\x1a\x11transaction.proto\"(\n\nCOwnerAddr\x12\x0f\n\x07txOwner\x18\x01 \x01(\t\x12\t\n\x01n\x18\x02 \x01(\r\"\xcd\x01\n\x0c\x43\x42lockHeader\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x0c\n\x04hash\x18\x02 \x01(\t\x12\x10\n\x08prevHash\x18\x03 \x01(\t\x12\x0e\n\x06height\x18\x04 \x01(\x03\x12\x12\n\nmerkleRoot\x18\x05 \x01(\t\x12\x1a\n\x03txs\x18\x06 \x03(\x0b\x32\r.CTransaction\x12\x1e\n\taddresses\x18\x07 \x03(\x0b\x32\x0b.COwnerAddr\x12\r\n\x05\x65xtra\x18\x08 \x01(\t\x12\x0f\n\x07\x63omment\x18\t \x01(\t\x12\x0c\n\x04time\x18\n \x01(\x04\"F\n\x06\x43\x42lock\x12\x0c\n\x04hash\x18\x01 \x01(\t\x12\x10\n\x08prevHash\x18\x02 \x01(\t\x12\x0e\n\x06height\x18\x03 \x01(\x03\x12\x0c\n\x04time\x18\x04 \x01(\x04\x62\x06proto3'
  ,
  dependencies=[transaction__pb2.DESCRIPTOR,])




_COWNERADDR = _descriptor.Descriptor(
  name='COwnerAddr',
  full_name='COwnerAddr',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='txOwner', full_name='COwnerAddr.txOwner', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='n', full_name='COwnerAddr.n', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=74,
)


_CBLOCKHEADER = _descriptor.Descriptor(
  name='CBlockHeader',
  full_name='CBlockHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='CBlockHeader.version', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hash', full_name='CBlockHeader.hash', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prevHash', full_name='CBlockHeader.prevHash', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='CBlockHeader.height', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='merkleRoot', full_name='CBlockHeader.merkleRoot', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='txs', full_name='CBlockHeader.txs', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='addresses', full_name='CBlockHeader.addresses', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extra', full_name='CBlockHeader.extra', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='comment', full_name='CBlockHeader.comment', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='CBlockHeader.time', index=9,
      number=10, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=77,
  serialized_end=282,
)


_CBLOCK = _descriptor.Descriptor(
  name='CBlock',
  full_name='CBlock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash', full_name='CBlock.hash', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prevHash', full_name='CBlock.prevHash', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='CBlock.height', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='CBlock.time', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=284,
  serialized_end=354,
)

_CBLOCKHEADER.fields_by_name['txs'].message_type = transaction__pb2._CTRANSACTION
_CBLOCKHEADER.fields_by_name['addresses'].message_type = _COWNERADDR
DESCRIPTOR.message_types_by_name['COwnerAddr'] = _COWNERADDR
DESCRIPTOR.message_types_by_name['CBlockHeader'] = _CBLOCKHEADER
DESCRIPTOR.message_types_by_name['CBlock'] = _CBLOCK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

COwnerAddr = _reflection.GeneratedProtocolMessageType('COwnerAddr', (_message.Message,), {
  'DESCRIPTOR' : _COWNERADDR,
  '__module__' : 'block_pb2'
  # @@protoc_insertion_point(class_scope:COwnerAddr)
  })
_sym_db.RegisterMessage(COwnerAddr)

CBlockHeader = _reflection.GeneratedProtocolMessageType('CBlockHeader', (_message.Message,), {
  'DESCRIPTOR' : _CBLOCKHEADER,
  '__module__' : 'block_pb2'
  # @@protoc_insertion_point(class_scope:CBlockHeader)
  })
_sym_db.RegisterMessage(CBlockHeader)

CBlock = _reflection.GeneratedProtocolMessageType('CBlock', (_message.Message,), {
  'DESCRIPTOR' : _CBLOCK,
  '__module__' : 'block_pb2'
  # @@protoc_insertion_point(class_scope:CBlock)
  })
_sym_db.RegisterMessage(CBlock)


# @@protoc_insertion_point(module_scope)
