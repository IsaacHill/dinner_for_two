from data.schema import schema
from graphql.utils import schema_printer

my_schema_str = schema_printer.print_schema(schema)
fp = open("schema.graphql", "w")
fp.write(my_schema_str)
fp.close()
