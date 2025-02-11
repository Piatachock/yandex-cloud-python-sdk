# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/cdn/v1/origin.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/cdn/v1/origin.proto',
  package='yandex.cloud.cdn.v1',
  syntax='proto3',
  serialized_options=b'\n\027yandex.cloud.api.cdn.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/cdn/v1;cdn',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n yandex/cloud/cdn/v1/origin.proto\x12\x13yandex.cloud.cdn.v1\"\x8d\x01\n\x06Origin\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x17\n\x0forigin_group_id\x18\x02 \x01(\x03\x12\x0e\n\x06source\x18\x03 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x04 \x01(\x08\x12\x0e\n\x06\x62\x61\x63kup\x18\x05 \x01(\x08\x12-\n\x04meta\x18\x06 \x01(\x0b\x32\x1f.yandex.cloud.cdn.v1.OriginMeta\"n\n\x0cOriginParams\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\x12\x0e\n\x06\x62\x61\x63kup\x18\x03 \x01(\x08\x12-\n\x04meta\x18\x04 \x01(\x0b\x32\x1f.yandex.cloud.cdn.v1.OriginMeta\"\x89\x02\n\nOriginMeta\x12\x36\n\x06\x63ommon\x18\x01 \x01(\x0b\x32$.yandex.cloud.cdn.v1.OriginNamedMetaH\x00\x12\x36\n\x06\x62ucket\x18\x02 \x01(\x0b\x32$.yandex.cloud.cdn.v1.OriginNamedMetaH\x00\x12\x37\n\x07website\x18\x03 \x01(\x0b\x32$.yandex.cloud.cdn.v1.OriginNamedMetaH\x00\x12;\n\x08\x62\x61lancer\x18\x04 \x01(\x0b\x32\'.yandex.cloud.cdn.v1.OriginBalancerMetaH\x00\x42\x15\n\x13origin_meta_variant\"\x1f\n\x0fOriginNamedMeta\x12\x0c\n\x04name\x18\x01 \x01(\t\" \n\x12OriginBalancerMeta\x12\n\n\x02id\x18\x01 \x01(\tBV\n\x17yandex.cloud.api.cdn.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/cdn/v1;cdnb\x06proto3'
)




_ORIGIN = _descriptor.Descriptor(
  name='Origin',
  full_name='yandex.cloud.cdn.v1.Origin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.cdn.v1.Origin.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='origin_group_id', full_name='yandex.cloud.cdn.v1.Origin.origin_group_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source', full_name='yandex.cloud.cdn.v1.Origin.source', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enabled', full_name='yandex.cloud.cdn.v1.Origin.enabled', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='backup', full_name='yandex.cloud.cdn.v1.Origin.backup', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='meta', full_name='yandex.cloud.cdn.v1.Origin.meta', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=58,
  serialized_end=199,
)


_ORIGINPARAMS = _descriptor.Descriptor(
  name='OriginParams',
  full_name='yandex.cloud.cdn.v1.OriginParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='source', full_name='yandex.cloud.cdn.v1.OriginParams.source', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enabled', full_name='yandex.cloud.cdn.v1.OriginParams.enabled', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='backup', full_name='yandex.cloud.cdn.v1.OriginParams.backup', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='meta', full_name='yandex.cloud.cdn.v1.OriginParams.meta', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=201,
  serialized_end=311,
)


_ORIGINMETA = _descriptor.Descriptor(
  name='OriginMeta',
  full_name='yandex.cloud.cdn.v1.OriginMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='common', full_name='yandex.cloud.cdn.v1.OriginMeta.common', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bucket', full_name='yandex.cloud.cdn.v1.OriginMeta.bucket', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='website', full_name='yandex.cloud.cdn.v1.OriginMeta.website', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='balancer', full_name='yandex.cloud.cdn.v1.OriginMeta.balancer', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
    _descriptor.OneofDescriptor(
      name='origin_meta_variant', full_name='yandex.cloud.cdn.v1.OriginMeta.origin_meta_variant',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=314,
  serialized_end=579,
)


_ORIGINNAMEDMETA = _descriptor.Descriptor(
  name='OriginNamedMeta',
  full_name='yandex.cloud.cdn.v1.OriginNamedMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.cdn.v1.OriginNamedMeta.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=581,
  serialized_end=612,
)


_ORIGINBALANCERMETA = _descriptor.Descriptor(
  name='OriginBalancerMeta',
  full_name='yandex.cloud.cdn.v1.OriginBalancerMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.cdn.v1.OriginBalancerMeta.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=614,
  serialized_end=646,
)

_ORIGIN.fields_by_name['meta'].message_type = _ORIGINMETA
_ORIGINPARAMS.fields_by_name['meta'].message_type = _ORIGINMETA
_ORIGINMETA.fields_by_name['common'].message_type = _ORIGINNAMEDMETA
_ORIGINMETA.fields_by_name['bucket'].message_type = _ORIGINNAMEDMETA
_ORIGINMETA.fields_by_name['website'].message_type = _ORIGINNAMEDMETA
_ORIGINMETA.fields_by_name['balancer'].message_type = _ORIGINBALANCERMETA
_ORIGINMETA.oneofs_by_name['origin_meta_variant'].fields.append(
  _ORIGINMETA.fields_by_name['common'])
_ORIGINMETA.fields_by_name['common'].containing_oneof = _ORIGINMETA.oneofs_by_name['origin_meta_variant']
_ORIGINMETA.oneofs_by_name['origin_meta_variant'].fields.append(
  _ORIGINMETA.fields_by_name['bucket'])
_ORIGINMETA.fields_by_name['bucket'].containing_oneof = _ORIGINMETA.oneofs_by_name['origin_meta_variant']
_ORIGINMETA.oneofs_by_name['origin_meta_variant'].fields.append(
  _ORIGINMETA.fields_by_name['website'])
_ORIGINMETA.fields_by_name['website'].containing_oneof = _ORIGINMETA.oneofs_by_name['origin_meta_variant']
_ORIGINMETA.oneofs_by_name['origin_meta_variant'].fields.append(
  _ORIGINMETA.fields_by_name['balancer'])
_ORIGINMETA.fields_by_name['balancer'].containing_oneof = _ORIGINMETA.oneofs_by_name['origin_meta_variant']
DESCRIPTOR.message_types_by_name['Origin'] = _ORIGIN
DESCRIPTOR.message_types_by_name['OriginParams'] = _ORIGINPARAMS
DESCRIPTOR.message_types_by_name['OriginMeta'] = _ORIGINMETA
DESCRIPTOR.message_types_by_name['OriginNamedMeta'] = _ORIGINNAMEDMETA
DESCRIPTOR.message_types_by_name['OriginBalancerMeta'] = _ORIGINBALANCERMETA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Origin = _reflection.GeneratedProtocolMessageType('Origin', (_message.Message,), {
  'DESCRIPTOR' : _ORIGIN,
  '__module__' : 'yandex.cloud.cdn.v1.origin_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.cdn.v1.Origin)
  })
_sym_db.RegisterMessage(Origin)

OriginParams = _reflection.GeneratedProtocolMessageType('OriginParams', (_message.Message,), {
  'DESCRIPTOR' : _ORIGINPARAMS,
  '__module__' : 'yandex.cloud.cdn.v1.origin_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.cdn.v1.OriginParams)
  })
_sym_db.RegisterMessage(OriginParams)

OriginMeta = _reflection.GeneratedProtocolMessageType('OriginMeta', (_message.Message,), {
  'DESCRIPTOR' : _ORIGINMETA,
  '__module__' : 'yandex.cloud.cdn.v1.origin_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.cdn.v1.OriginMeta)
  })
_sym_db.RegisterMessage(OriginMeta)

OriginNamedMeta = _reflection.GeneratedProtocolMessageType('OriginNamedMeta', (_message.Message,), {
  'DESCRIPTOR' : _ORIGINNAMEDMETA,
  '__module__' : 'yandex.cloud.cdn.v1.origin_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.cdn.v1.OriginNamedMeta)
  })
_sym_db.RegisterMessage(OriginNamedMeta)

OriginBalancerMeta = _reflection.GeneratedProtocolMessageType('OriginBalancerMeta', (_message.Message,), {
  'DESCRIPTOR' : _ORIGINBALANCERMETA,
  '__module__' : 'yandex.cloud.cdn.v1.origin_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.cdn.v1.OriginBalancerMeta)
  })
_sym_db.RegisterMessage(OriginBalancerMeta)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
