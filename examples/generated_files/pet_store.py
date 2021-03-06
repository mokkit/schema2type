from pathlib import Path

import schema2type
from schema2type import SchemaBasedObject

globals().update(schema2type.SchemaBasedTypeBuilder(
    Path(__file__).parent.joinpath('../../examples/pet_store_openapi_spec.yml'),
    'openapi',
).get_all_types())
