# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mysql_grpc.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mysql_grpc.proto',
  package='mysql_grpc',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10mysql_grpc.proto\x12\nmysql_grpc\"H\n\nDBConnInfo\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\t\x12\x0e\n\x06\x64\x62name\x18\x03 \x01(\t\x12\x10\n\x08mysqluid\x18\x04 \x01(\t\"D\n\x0cUsersRequest\x12&\n\x06\x64\x62\x63onn\x18\x01 \x01(\x0b\x32\x16.mysql_grpc.DBConnInfo\x12\x0c\n\x04user\x18\x02 \x01(\t\"_\n\x08UserInfo\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x0c\n\x04host\x18\x02 \x01(\t\x12\x18\n\x10password_expired\x18\x03 \x01(\t\x12\x1d\n\x15password_last_changed\x18\x04 \x01(\t\"]\n\rUsersResponse\x12&\n\x06\x64\x62\x63onn\x18\x01 \x01(\x0b\x32\x16.mysql_grpc.DBConnInfo\x12$\n\x06result\x18\x02 \x03(\x0b\x32\x14.mysql_grpc.UserInfo\"H\n\x0cMySQLRequest\x12&\n\x06\x64\x62\x63onn\x18\x01 \x01(\x0b\x32\x16.mysql_grpc.DBConnInfo\x12\x10\n\x08\x64\x61tabase\x18\x02 \x01(\t\"t\n\x0c\x44\x61tabaseInfo\x12\x14\n\x0ctable_schema\x18\x01 \x01(\t\x12\x13\n\x0btable_count\x18\x02 \x01(\r\x12\x12\n\ntotal_size\x18\x03 \x01(\x02\x12\x11\n\tdata_size\x18\x04 \x01(\x02\x12\x12\n\nindex_size\x18\x05 \x01(\x02\"a\n\rMySQLResponse\x12&\n\x06\x64\x62\x63onn\x18\x01 \x01(\x0b\x32\x16.mysql_grpc.DBConnInfo\x12(\n\x06result\x18\x02 \x03(\x0b\x32\x18.mysql_grpc.DatabaseInfo\"K\n\x0f\x44\x61tabaseRequest\x12&\n\x06\x64\x62\x63onn\x18\x01 \x01(\x0b\x32\x16.mysql_grpc.DBConnInfo\x12\x10\n\x08\x64\x61tabase\x18\x02 \x01(\t\"`\n\x0f\x44\x61tabaseDetails\x12\x12\n\ntable_name\x18\x01 \x01(\t\x12\x12\n\ntotal_size\x18\x02 \x01(\x02\x12\x11\n\tdata_size\x18\x03 \x01(\x02\x12\x12\n\nindex_size\x18\x04 \x01(\x02\"g\n\x10\x44\x61tabaseResponse\x12&\n\x06\x64\x62\x63onn\x18\x01 \x01(\x0b\x32\x16.mysql_grpc.DBConnInfo\x12+\n\x06result\x18\x02 \x03(\x0b\x32\x1b.mysql_grpc.DatabaseDetails2\xdd\x01\n\tMySQLGRPC\x12\x41\n\x08GetUsers\x12\x18.mysql_grpc.UsersRequest\x1a\x19.mysql_grpc.UsersResponse\"\x00\x12\x41\n\x08GetMySQL\x12\x18.mysql_grpc.MySQLRequest\x1a\x19.mysql_grpc.MySQLResponse\"\x00\x12J\n\x0bGetDatabase\x12\x1b.mysql_grpc.DatabaseRequest\x1a\x1c.mysql_grpc.DatabaseResponse\"\x00\x62\x06proto3'
)




_DBCONNINFO = _descriptor.Descriptor(
  name='DBConnInfo',
  full_name='mysql_grpc.DBConnInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='mysql_grpc.DBConnInfo.ip', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='mysql_grpc.DBConnInfo.port', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dbname', full_name='mysql_grpc.DBConnInfo.dbname', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mysqluid', full_name='mysql_grpc.DBConnInfo.mysqluid', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=32,
  serialized_end=104,
)


_USERSREQUEST = _descriptor.Descriptor(
  name='UsersRequest',
  full_name='mysql_grpc.UsersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dbconn', full_name='mysql_grpc.UsersRequest.dbconn', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user', full_name='mysql_grpc.UsersRequest.user', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=106,
  serialized_end=174,
)


_USERINFO = _descriptor.Descriptor(
  name='UserInfo',
  full_name='mysql_grpc.UserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='mysql_grpc.UserInfo.user', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='host', full_name='mysql_grpc.UserInfo.host', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password_expired', full_name='mysql_grpc.UserInfo.password_expired', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password_last_changed', full_name='mysql_grpc.UserInfo.password_last_changed', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=176,
  serialized_end=271,
)


_USERSRESPONSE = _descriptor.Descriptor(
  name='UsersResponse',
  full_name='mysql_grpc.UsersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dbconn', full_name='mysql_grpc.UsersResponse.dbconn', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result', full_name='mysql_grpc.UsersResponse.result', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=273,
  serialized_end=366,
)


_MYSQLREQUEST = _descriptor.Descriptor(
  name='MySQLRequest',
  full_name='mysql_grpc.MySQLRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dbconn', full_name='mysql_grpc.MySQLRequest.dbconn', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='database', full_name='mysql_grpc.MySQLRequest.database', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=368,
  serialized_end=440,
)


_DATABASEINFO = _descriptor.Descriptor(
  name='DatabaseInfo',
  full_name='mysql_grpc.DatabaseInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='table_schema', full_name='mysql_grpc.DatabaseInfo.table_schema', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='table_count', full_name='mysql_grpc.DatabaseInfo.table_count', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_size', full_name='mysql_grpc.DatabaseInfo.total_size', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data_size', full_name='mysql_grpc.DatabaseInfo.data_size', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='index_size', full_name='mysql_grpc.DatabaseInfo.index_size', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=442,
  serialized_end=558,
)


_MYSQLRESPONSE = _descriptor.Descriptor(
  name='MySQLResponse',
  full_name='mysql_grpc.MySQLResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dbconn', full_name='mysql_grpc.MySQLResponse.dbconn', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result', full_name='mysql_grpc.MySQLResponse.result', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=560,
  serialized_end=657,
)


_DATABASEREQUEST = _descriptor.Descriptor(
  name='DatabaseRequest',
  full_name='mysql_grpc.DatabaseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dbconn', full_name='mysql_grpc.DatabaseRequest.dbconn', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='database', full_name='mysql_grpc.DatabaseRequest.database', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=659,
  serialized_end=734,
)


_DATABASEDETAILS = _descriptor.Descriptor(
  name='DatabaseDetails',
  full_name='mysql_grpc.DatabaseDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='table_name', full_name='mysql_grpc.DatabaseDetails.table_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_size', full_name='mysql_grpc.DatabaseDetails.total_size', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data_size', full_name='mysql_grpc.DatabaseDetails.data_size', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='index_size', full_name='mysql_grpc.DatabaseDetails.index_size', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=736,
  serialized_end=832,
)


_DATABASERESPONSE = _descriptor.Descriptor(
  name='DatabaseResponse',
  full_name='mysql_grpc.DatabaseResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dbconn', full_name='mysql_grpc.DatabaseResponse.dbconn', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result', full_name='mysql_grpc.DatabaseResponse.result', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=834,
  serialized_end=937,
)

_USERSREQUEST.fields_by_name['dbconn'].message_type = _DBCONNINFO
_USERSRESPONSE.fields_by_name['dbconn'].message_type = _DBCONNINFO
_USERSRESPONSE.fields_by_name['result'].message_type = _USERINFO
_MYSQLREQUEST.fields_by_name['dbconn'].message_type = _DBCONNINFO
_MYSQLRESPONSE.fields_by_name['dbconn'].message_type = _DBCONNINFO
_MYSQLRESPONSE.fields_by_name['result'].message_type = _DATABASEINFO
_DATABASEREQUEST.fields_by_name['dbconn'].message_type = _DBCONNINFO
_DATABASERESPONSE.fields_by_name['dbconn'].message_type = _DBCONNINFO
_DATABASERESPONSE.fields_by_name['result'].message_type = _DATABASEDETAILS
DESCRIPTOR.message_types_by_name['DBConnInfo'] = _DBCONNINFO
DESCRIPTOR.message_types_by_name['UsersRequest'] = _USERSREQUEST
DESCRIPTOR.message_types_by_name['UserInfo'] = _USERINFO
DESCRIPTOR.message_types_by_name['UsersResponse'] = _USERSRESPONSE
DESCRIPTOR.message_types_by_name['MySQLRequest'] = _MYSQLREQUEST
DESCRIPTOR.message_types_by_name['DatabaseInfo'] = _DATABASEINFO
DESCRIPTOR.message_types_by_name['MySQLResponse'] = _MYSQLRESPONSE
DESCRIPTOR.message_types_by_name['DatabaseRequest'] = _DATABASEREQUEST
DESCRIPTOR.message_types_by_name['DatabaseDetails'] = _DATABASEDETAILS
DESCRIPTOR.message_types_by_name['DatabaseResponse'] = _DATABASERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DBConnInfo = _reflection.GeneratedProtocolMessageType('DBConnInfo', (_message.Message,), {
  'DESCRIPTOR' : _DBCONNINFO,
  '__module__' : 'mysql_grpc_pb2'
  # @@protoc_insertion_point(class_scope:mysql_grpc.DBConnInfo)
  })
_sym_db.RegisterMessage(DBConnInfo)

UsersRequest = _reflection.GeneratedProtocolMessageType('UsersRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERSREQUEST,
  '__module__' : 'mysql_grpc_pb2'
  # @@protoc_insertion_point(class_scope:mysql_grpc.UsersRequest)
  })
_sym_db.RegisterMessage(UsersRequest)

UserInfo = _reflection.GeneratedProtocolMessageType('UserInfo', (_message.Message,), {
  'DESCRIPTOR' : _USERINFO,
  '__module__' : 'mysql_grpc_pb2'
  # @@protoc_insertion_point(class_scope:mysql_grpc.UserInfo)
  })
_sym_db.RegisterMessage(UserInfo)

UsersResponse = _reflection.GeneratedProtocolMessageType('UsersResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERSRESPONSE,
  '__module__' : 'mysql_grpc_pb2'
  # @@protoc_insertion_point(class_scope:mysql_grpc.UsersResponse)
  })
_sym_db.RegisterMessage(UsersResponse)

MySQLRequest = _reflection.GeneratedProtocolMessageType('MySQLRequest', (_message.Message,), {
  'DESCRIPTOR' : _MYSQLREQUEST,
  '__module__' : 'mysql_grpc_pb2'
  # @@protoc_insertion_point(class_scope:mysql_grpc.MySQLRequest)
  })
_sym_db.RegisterMessage(MySQLRequest)

DatabaseInfo = _reflection.GeneratedProtocolMessageType('DatabaseInfo', (_message.Message,), {
  'DESCRIPTOR' : _DATABASEINFO,
  '__module__' : 'mysql_grpc_pb2'
  # @@protoc_insertion_point(class_scope:mysql_grpc.DatabaseInfo)
  })
_sym_db.RegisterMessage(DatabaseInfo)

MySQLResponse = _reflection.GeneratedProtocolMessageType('MySQLResponse', (_message.Message,), {
  'DESCRIPTOR' : _MYSQLRESPONSE,
  '__module__' : 'mysql_grpc_pb2'
  # @@protoc_insertion_point(class_scope:mysql_grpc.MySQLResponse)
  })
_sym_db.RegisterMessage(MySQLResponse)

DatabaseRequest = _reflection.GeneratedProtocolMessageType('DatabaseRequest', (_message.Message,), {
  'DESCRIPTOR' : _DATABASEREQUEST,
  '__module__' : 'mysql_grpc_pb2'
  # @@protoc_insertion_point(class_scope:mysql_grpc.DatabaseRequest)
  })
_sym_db.RegisterMessage(DatabaseRequest)

DatabaseDetails = _reflection.GeneratedProtocolMessageType('DatabaseDetails', (_message.Message,), {
  'DESCRIPTOR' : _DATABASEDETAILS,
  '__module__' : 'mysql_grpc_pb2'
  # @@protoc_insertion_point(class_scope:mysql_grpc.DatabaseDetails)
  })
_sym_db.RegisterMessage(DatabaseDetails)

DatabaseResponse = _reflection.GeneratedProtocolMessageType('DatabaseResponse', (_message.Message,), {
  'DESCRIPTOR' : _DATABASERESPONSE,
  '__module__' : 'mysql_grpc_pb2'
  # @@protoc_insertion_point(class_scope:mysql_grpc.DatabaseResponse)
  })
_sym_db.RegisterMessage(DatabaseResponse)



_MYSQLGRPC = _descriptor.ServiceDescriptor(
  name='MySQLGRPC',
  full_name='mysql_grpc.MySQLGRPC',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=940,
  serialized_end=1161,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetUsers',
    full_name='mysql_grpc.MySQLGRPC.GetUsers',
    index=0,
    containing_service=None,
    input_type=_USERSREQUEST,
    output_type=_USERSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetMySQL',
    full_name='mysql_grpc.MySQLGRPC.GetMySQL',
    index=1,
    containing_service=None,
    input_type=_MYSQLREQUEST,
    output_type=_MYSQLRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetDatabase',
    full_name='mysql_grpc.MySQLGRPC.GetDatabase',
    index=2,
    containing_service=None,
    input_type=_DATABASEREQUEST,
    output_type=_DATABASERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MYSQLGRPC)

DESCRIPTOR.services_by_name['MySQLGRPC'] = _MYSQLGRPC

# @@protoc_insertion_point(module_scope)
