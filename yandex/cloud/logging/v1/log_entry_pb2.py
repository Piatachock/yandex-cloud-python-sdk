# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/logging/v1/log_entry.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud.logging.v1 import log_resource_pb2 as yandex_dot_cloud_dot_logging_dot_v1_dot_log__resource__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/logging/v1/log_entry.proto',
  package='yandex.cloud.logging.v1',
  syntax='proto3',
  serialized_options=b'\n\033yandex.cloud.api.logging.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/logging/v1;logging',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\'yandex/cloud/logging/v1/log_entry.proto\x12\x17yandex.cloud.logging.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a*yandex/cloud/logging/v1/log_resource.proto\x1a\x1dyandex/cloud/validation.proto\"\xda\x02\n\x08LogEntry\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12;\n\x08resource\x18\x02 \x01(\x0b\x32).yandex.cloud.logging.v1.LogEntryResource\x12-\n\ttimestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bingested_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08saved_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x36\n\x05level\x18\x06 \x01(\x0e\x32\'.yandex.cloud.logging.v1.LogLevel.Level\x12\x0f\n\x07message\x18\x07 \x01(\t\x12-\n\x0cjson_payload\x18\x08 \x01(\x0b\x32\x17.google.protobuf.Struct\"\xd9\x01\n\x10IncomingLogEntry\x12\x33\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe8\xc7\x31\x01\x12\x36\n\x05level\x18\x02 \x01(\x0e\x32\'.yandex.cloud.logging.v1.LogLevel.Level\x12\x1c\n\x07message\x18\x03 \x01(\tB\x0b\xba\xc8\x31\x07<=65536\x12:\n\x0cjson_payload\x18\x04 \x01(\x0b\x32\x17.google.protobuf.StructB\x0b\xba\xc8\x31\x07<=65536\"\x86\x01\n\x10LogEntryDefaults\x12\x36\n\x05level\x18\x02 \x01(\x0e\x32\'.yandex.cloud.logging.v1.LogLevel.Level\x12:\n\x0cjson_payload\x18\x04 \x01(\x0b\x32\x17.google.protobuf.StructB\x0b\xba\xc8\x31\x07<=65536\"\x99\x01\n\x0b\x44\x65stination\x12;\n\x0clog_group_id\x18\x01 \x01(\tB#\xf2\xc7\x31\x1f([a-zA-Z][-a-zA-Z0-9_.]{0,63})?H\x00\x12\x38\n\tfolder_id\x18\x02 \x01(\tB#\xf2\xc7\x31\x1f([a-zA-Z][-a-zA-Z0-9_.]{0,63})?H\x00\x42\x13\n\x0b\x64\x65stination\x12\x04\xc0\xc1\x31\x01\"\xa2\x01\n\x08LogLevel\x12\x36\n\x05level\x18\x01 \x01(\x0e\x32\'.yandex.cloud.logging.v1.LogLevel.Level\"^\n\x05Level\x12\x15\n\x11LEVEL_UNSPECIFIED\x10\x00\x12\t\n\x05TRACE\x10\x01\x12\t\n\x05\x44\x45\x42UG\x10\x02\x12\x08\n\x04INFO\x10\x03\x12\x08\n\x04WARN\x10\x04\x12\t\n\x05\x45RROR\x10\x05\x12\t\n\x05\x46\x41TAL\x10\x06\x42\x62\n\x1byandex.cloud.api.logging.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/logging/v1;loggingb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,yandex_dot_cloud_dot_logging_dot_v1_dot_log__resource__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])



_LOGLEVEL_LEVEL = _descriptor.EnumDescriptor(
  name='Level',
  full_name='yandex.cloud.logging.v1.LogLevel.Level',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LEVEL_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TRACE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEBUG', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INFO', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WARN', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FATAL', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1137,
  serialized_end=1231,
)
_sym_db.RegisterEnumDescriptor(_LOGLEVEL_LEVEL)


_LOGENTRY = _descriptor.Descriptor(
  name='LogEntry',
  full_name='yandex.cloud.logging.v1.LogEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='yandex.cloud.logging.v1.LogEntry.uid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resource', full_name='yandex.cloud.logging.v1.LogEntry.resource', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='yandex.cloud.logging.v1.LogEntry.timestamp', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ingested_at', full_name='yandex.cloud.logging.v1.LogEntry.ingested_at', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='saved_at', full_name='yandex.cloud.logging.v1.LogEntry.saved_at', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='level', full_name='yandex.cloud.logging.v1.LogEntry.level', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='yandex.cloud.logging.v1.LogEntry.message', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='json_payload', full_name='yandex.cloud.logging.v1.LogEntry.json_payload', index=7,
      number=8, type=11, cpp_type=10, label=1,
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
  serialized_start=207,
  serialized_end=553,
)


_INCOMINGLOGENTRY = _descriptor.Descriptor(
  name='IncomingLogEntry',
  full_name='yandex.cloud.logging.v1.IncomingLogEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='yandex.cloud.logging.v1.IncomingLogEntry.timestamp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='level', full_name='yandex.cloud.logging.v1.IncomingLogEntry.level', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='yandex.cloud.logging.v1.IncomingLogEntry.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\272\3101\007<=65536', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='json_payload', full_name='yandex.cloud.logging.v1.IncomingLogEntry.json_payload', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\272\3101\007<=65536', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=556,
  serialized_end=773,
)


_LOGENTRYDEFAULTS = _descriptor.Descriptor(
  name='LogEntryDefaults',
  full_name='yandex.cloud.logging.v1.LogEntryDefaults',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='level', full_name='yandex.cloud.logging.v1.LogEntryDefaults.level', index=0,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='json_payload', full_name='yandex.cloud.logging.v1.LogEntryDefaults.json_payload', index=1,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\272\3101\007<=65536', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=776,
  serialized_end=910,
)


_DESTINATION = _descriptor.Descriptor(
  name='Destination',
  full_name='yandex.cloud.logging.v1.Destination',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='log_group_id', full_name='yandex.cloud.logging.v1.Destination.log_group_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\3071\037([a-zA-Z][-a-zA-Z0-9_.]{0,63})?', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.logging.v1.Destination.folder_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\3071\037([a-zA-Z][-a-zA-Z0-9_.]{0,63})?', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
      name='destination', full_name='yandex.cloud.logging.v1.Destination.destination',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[], serialized_options=b'\300\3011\001'),
  ],
  serialized_start=913,
  serialized_end=1066,
)


_LOGLEVEL = _descriptor.Descriptor(
  name='LogLevel',
  full_name='yandex.cloud.logging.v1.LogLevel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='level', full_name='yandex.cloud.logging.v1.LogLevel.level', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LOGLEVEL_LEVEL,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1069,
  serialized_end=1231,
)

_LOGENTRY.fields_by_name['resource'].message_type = yandex_dot_cloud_dot_logging_dot_v1_dot_log__resource__pb2._LOGENTRYRESOURCE
_LOGENTRY.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LOGENTRY.fields_by_name['ingested_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LOGENTRY.fields_by_name['saved_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LOGENTRY.fields_by_name['level'].enum_type = _LOGLEVEL_LEVEL
_LOGENTRY.fields_by_name['json_payload'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_INCOMINGLOGENTRY.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_INCOMINGLOGENTRY.fields_by_name['level'].enum_type = _LOGLEVEL_LEVEL
_INCOMINGLOGENTRY.fields_by_name['json_payload'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_LOGENTRYDEFAULTS.fields_by_name['level'].enum_type = _LOGLEVEL_LEVEL
_LOGENTRYDEFAULTS.fields_by_name['json_payload'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_DESTINATION.oneofs_by_name['destination'].fields.append(
  _DESTINATION.fields_by_name['log_group_id'])
_DESTINATION.fields_by_name['log_group_id'].containing_oneof = _DESTINATION.oneofs_by_name['destination']
_DESTINATION.oneofs_by_name['destination'].fields.append(
  _DESTINATION.fields_by_name['folder_id'])
_DESTINATION.fields_by_name['folder_id'].containing_oneof = _DESTINATION.oneofs_by_name['destination']
_LOGLEVEL.fields_by_name['level'].enum_type = _LOGLEVEL_LEVEL
_LOGLEVEL_LEVEL.containing_type = _LOGLEVEL
DESCRIPTOR.message_types_by_name['LogEntry'] = _LOGENTRY
DESCRIPTOR.message_types_by_name['IncomingLogEntry'] = _INCOMINGLOGENTRY
DESCRIPTOR.message_types_by_name['LogEntryDefaults'] = _LOGENTRYDEFAULTS
DESCRIPTOR.message_types_by_name['Destination'] = _DESTINATION
DESCRIPTOR.message_types_by_name['LogLevel'] = _LOGLEVEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LogEntry = _reflection.GeneratedProtocolMessageType('LogEntry', (_message.Message,), {
  'DESCRIPTOR' : _LOGENTRY,
  '__module__' : 'yandex.cloud.logging.v1.log_entry_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.logging.v1.LogEntry)
  })
_sym_db.RegisterMessage(LogEntry)

IncomingLogEntry = _reflection.GeneratedProtocolMessageType('IncomingLogEntry', (_message.Message,), {
  'DESCRIPTOR' : _INCOMINGLOGENTRY,
  '__module__' : 'yandex.cloud.logging.v1.log_entry_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.logging.v1.IncomingLogEntry)
  })
_sym_db.RegisterMessage(IncomingLogEntry)

LogEntryDefaults = _reflection.GeneratedProtocolMessageType('LogEntryDefaults', (_message.Message,), {
  'DESCRIPTOR' : _LOGENTRYDEFAULTS,
  '__module__' : 'yandex.cloud.logging.v1.log_entry_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.logging.v1.LogEntryDefaults)
  })
_sym_db.RegisterMessage(LogEntryDefaults)

Destination = _reflection.GeneratedProtocolMessageType('Destination', (_message.Message,), {
  'DESCRIPTOR' : _DESTINATION,
  '__module__' : 'yandex.cloud.logging.v1.log_entry_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.logging.v1.Destination)
  })
_sym_db.RegisterMessage(Destination)

LogLevel = _reflection.GeneratedProtocolMessageType('LogLevel', (_message.Message,), {
  'DESCRIPTOR' : _LOGLEVEL,
  '__module__' : 'yandex.cloud.logging.v1.log_entry_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.logging.v1.LogLevel)
  })
_sym_db.RegisterMessage(LogLevel)


DESCRIPTOR._options = None
_INCOMINGLOGENTRY.fields_by_name['timestamp']._options = None
_INCOMINGLOGENTRY.fields_by_name['message']._options = None
_INCOMINGLOGENTRY.fields_by_name['json_payload']._options = None
_LOGENTRYDEFAULTS.fields_by_name['json_payload']._options = None
_DESTINATION.oneofs_by_name['destination']._options = None
_DESTINATION.fields_by_name['log_group_id']._options = None
_DESTINATION.fields_by_name['folder_id']._options = None
# @@protoc_insertion_point(module_scope)
