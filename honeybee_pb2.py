# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: honeybee.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='honeybee.proto',
  package='honeybee.recipe',
  syntax='proto3',
  serialized_pb=_b('\n\x0ehoneybee.proto\x12\x0fhoneybee.recipe\"\xc8\x01\n\x1aSolarAccessRecipeGridBased\x12\n\n\x02id\x18\x01 \x01(\x05\x12+\n\x08location\x18\x02 \x01(\x0b\x32\x19.honeybee.recipe.Location\x12\x0c\n\x04hoys\x18\x03 \x03(\x02\x12,\n\x08surfaces\x18\x04 \x03(\x0b\x32\x1a.honeybee.recipe.HBSurface\x12\x35\n\x0e\x61nalysis_grids\x18\x05 \x03(\x0b\x32\x1d.honeybee.recipe.AnalysisGrid\"c\n\x08Location\x12\x0c\n\x04\x63ity\x18\x01 \x01(\t\x12\x10\n\x08latitude\x18\x02 \x01(\x02\x12\x11\n\tlongitude\x18\x03 \x01(\x02\x12\x11\n\ttime_zone\x18\x04 \x01(\x02\x12\x11\n\televation\x18\x05 \x01(\x02\"&\n\x03XYZ\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\"3\n\rXYZCollection\x12\"\n\x04xyzs\x18\x01 \x03(\x0b\x32\x14.honeybee.recipe.XYZ\"`\n\rAnalysisPoint\x12&\n\x08location\x18\x01 \x01(\x0b\x32\x14.honeybee.recipe.XYZ\x12\'\n\tdirection\x18\x02 \x01(\x0b\x32\x14.honeybee.recipe.XYZ\"G\n\x0c\x41nalysisGrid\x12\x37\n\x0f\x61nalysis_points\x18\x01 \x03(\x0b\x32\x1e.honeybee.recipe.AnalysisPoint\"a\n\tHBSurface\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0csurface_type\x18\x02 \x01(\x05\x12\x30\n\x08vertices\x18\x03 \x03(\x0b\x32\x1e.honeybee.recipe.XYZCollection\"<\n\x0eRadianceResult\x12\x0b\n\x03hoy\x18\x01 \x01(\x02\x12\r\n\x05total\x18\x02 \x01(\x05\x12\x0e\n\x06\x64irect\x18\x03 \x01(\x05\"l\n\x06Result\x12\x0e\n\x06job_id\x18\x01 \x01(\t\x12\x0f\n\x07success\x18\x02 \x01(\x08\x12/\n\x06values\x18\x03 \x03(\x0b\x32\x1f.honeybee.recipe.RadianceResult\x12\x10\n\x08log_info\x18\x04 \x01(\t2X\n\tRunRecipe\x12K\n\x03run\x12+.honeybee.recipe.SolarAccessRecipeGridBased\x1a\x17.honeybee.recipe.Resultb\x06proto3')
)




_SOLARACCESSRECIPEGRIDBASED = _descriptor.Descriptor(
  name='SolarAccessRecipeGridBased',
  full_name='honeybee.recipe.SolarAccessRecipeGridBased',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='honeybee.recipe.SolarAccessRecipeGridBased.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='location', full_name='honeybee.recipe.SolarAccessRecipeGridBased.location', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hoys', full_name='honeybee.recipe.SolarAccessRecipeGridBased.hoys', index=2,
      number=3, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='surfaces', full_name='honeybee.recipe.SolarAccessRecipeGridBased.surfaces', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='analysis_grids', full_name='honeybee.recipe.SolarAccessRecipeGridBased.analysis_grids', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=236,
)


_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='honeybee.recipe.Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='city', full_name='honeybee.recipe.Location.city', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='honeybee.recipe.Location.latitude', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='honeybee.recipe.Location.longitude', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_zone', full_name='honeybee.recipe.Location.time_zone', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='elevation', full_name='honeybee.recipe.Location.elevation', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=238,
  serialized_end=337,
)


_XYZ = _descriptor.Descriptor(
  name='XYZ',
  full_name='honeybee.recipe.XYZ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='honeybee.recipe.XYZ.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='honeybee.recipe.XYZ.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='z', full_name='honeybee.recipe.XYZ.z', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=339,
  serialized_end=377,
)


_XYZCOLLECTION = _descriptor.Descriptor(
  name='XYZCollection',
  full_name='honeybee.recipe.XYZCollection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='xyzs', full_name='honeybee.recipe.XYZCollection.xyzs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=379,
  serialized_end=430,
)


_ANALYSISPOINT = _descriptor.Descriptor(
  name='AnalysisPoint',
  full_name='honeybee.recipe.AnalysisPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='location', full_name='honeybee.recipe.AnalysisPoint.location', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='direction', full_name='honeybee.recipe.AnalysisPoint.direction', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=432,
  serialized_end=528,
)


_ANALYSISGRID = _descriptor.Descriptor(
  name='AnalysisGrid',
  full_name='honeybee.recipe.AnalysisGrid',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='analysis_points', full_name='honeybee.recipe.AnalysisGrid.analysis_points', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=530,
  serialized_end=601,
)


_HBSURFACE = _descriptor.Descriptor(
  name='HBSurface',
  full_name='honeybee.recipe.HBSurface',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='honeybee.recipe.HBSurface.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='surface_type', full_name='honeybee.recipe.HBSurface.surface_type', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vertices', full_name='honeybee.recipe.HBSurface.vertices', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=603,
  serialized_end=700,
)


_RADIANCERESULT = _descriptor.Descriptor(
  name='RadianceResult',
  full_name='honeybee.recipe.RadianceResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hoy', full_name='honeybee.recipe.RadianceResult.hoy', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total', full_name='honeybee.recipe.RadianceResult.total', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='direct', full_name='honeybee.recipe.RadianceResult.direct', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=702,
  serialized_end=762,
)


_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='honeybee.recipe.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='job_id', full_name='honeybee.recipe.Result.job_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='success', full_name='honeybee.recipe.Result.success', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='values', full_name='honeybee.recipe.Result.values', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='log_info', full_name='honeybee.recipe.Result.log_info', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=764,
  serialized_end=872,
)

_SOLARACCESSRECIPEGRIDBASED.fields_by_name['location'].message_type = _LOCATION
_SOLARACCESSRECIPEGRIDBASED.fields_by_name['surfaces'].message_type = _HBSURFACE
_SOLARACCESSRECIPEGRIDBASED.fields_by_name['analysis_grids'].message_type = _ANALYSISGRID
_XYZCOLLECTION.fields_by_name['xyzs'].message_type = _XYZ
_ANALYSISPOINT.fields_by_name['location'].message_type = _XYZ
_ANALYSISPOINT.fields_by_name['direction'].message_type = _XYZ
_ANALYSISGRID.fields_by_name['analysis_points'].message_type = _ANALYSISPOINT
_HBSURFACE.fields_by_name['vertices'].message_type = _XYZCOLLECTION
_RESULT.fields_by_name['values'].message_type = _RADIANCERESULT
DESCRIPTOR.message_types_by_name['SolarAccessRecipeGridBased'] = _SOLARACCESSRECIPEGRIDBASED
DESCRIPTOR.message_types_by_name['Location'] = _LOCATION
DESCRIPTOR.message_types_by_name['XYZ'] = _XYZ
DESCRIPTOR.message_types_by_name['XYZCollection'] = _XYZCOLLECTION
DESCRIPTOR.message_types_by_name['AnalysisPoint'] = _ANALYSISPOINT
DESCRIPTOR.message_types_by_name['AnalysisGrid'] = _ANALYSISGRID
DESCRIPTOR.message_types_by_name['HBSurface'] = _HBSURFACE
DESCRIPTOR.message_types_by_name['RadianceResult'] = _RADIANCERESULT
DESCRIPTOR.message_types_by_name['Result'] = _RESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SolarAccessRecipeGridBased = _reflection.GeneratedProtocolMessageType('SolarAccessRecipeGridBased', (_message.Message,), dict(
  DESCRIPTOR = _SOLARACCESSRECIPEGRIDBASED,
  __module__ = 'honeybee_pb2'
  # @@protoc_insertion_point(class_scope:honeybee.recipe.SolarAccessRecipeGridBased)
  ))
_sym_db.RegisterMessage(SolarAccessRecipeGridBased)

Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), dict(
  DESCRIPTOR = _LOCATION,
  __module__ = 'honeybee_pb2'
  # @@protoc_insertion_point(class_scope:honeybee.recipe.Location)
  ))
_sym_db.RegisterMessage(Location)

XYZ = _reflection.GeneratedProtocolMessageType('XYZ', (_message.Message,), dict(
  DESCRIPTOR = _XYZ,
  __module__ = 'honeybee_pb2'
  # @@protoc_insertion_point(class_scope:honeybee.recipe.XYZ)
  ))
_sym_db.RegisterMessage(XYZ)

XYZCollection = _reflection.GeneratedProtocolMessageType('XYZCollection', (_message.Message,), dict(
  DESCRIPTOR = _XYZCOLLECTION,
  __module__ = 'honeybee_pb2'
  # @@protoc_insertion_point(class_scope:honeybee.recipe.XYZCollection)
  ))
_sym_db.RegisterMessage(XYZCollection)

AnalysisPoint = _reflection.GeneratedProtocolMessageType('AnalysisPoint', (_message.Message,), dict(
  DESCRIPTOR = _ANALYSISPOINT,
  __module__ = 'honeybee_pb2'
  # @@protoc_insertion_point(class_scope:honeybee.recipe.AnalysisPoint)
  ))
_sym_db.RegisterMessage(AnalysisPoint)

AnalysisGrid = _reflection.GeneratedProtocolMessageType('AnalysisGrid', (_message.Message,), dict(
  DESCRIPTOR = _ANALYSISGRID,
  __module__ = 'honeybee_pb2'
  # @@protoc_insertion_point(class_scope:honeybee.recipe.AnalysisGrid)
  ))
_sym_db.RegisterMessage(AnalysisGrid)

HBSurface = _reflection.GeneratedProtocolMessageType('HBSurface', (_message.Message,), dict(
  DESCRIPTOR = _HBSURFACE,
  __module__ = 'honeybee_pb2'
  # @@protoc_insertion_point(class_scope:honeybee.recipe.HBSurface)
  ))
_sym_db.RegisterMessage(HBSurface)

RadianceResult = _reflection.GeneratedProtocolMessageType('RadianceResult', (_message.Message,), dict(
  DESCRIPTOR = _RADIANCERESULT,
  __module__ = 'honeybee_pb2'
  # @@protoc_insertion_point(class_scope:honeybee.recipe.RadianceResult)
  ))
_sym_db.RegisterMessage(RadianceResult)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), dict(
  DESCRIPTOR = _RESULT,
  __module__ = 'honeybee_pb2'
  # @@protoc_insertion_point(class_scope:honeybee.recipe.Result)
  ))
_sym_db.RegisterMessage(Result)



_RUNRECIPE = _descriptor.ServiceDescriptor(
  name='RunRecipe',
  full_name='honeybee.recipe.RunRecipe',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=874,
  serialized_end=962,
  methods=[
  _descriptor.MethodDescriptor(
    name='run',
    full_name='honeybee.recipe.RunRecipe.run',
    index=0,
    containing_service=None,
    input_type=_SOLARACCESSRECIPEGRIDBASED,
    output_type=_RESULT,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_RUNRECIPE)

DESCRIPTOR.services_by_name['RunRecipe'] = _RUNRECIPE

# @@protoc_insertion_point(module_scope)