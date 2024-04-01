from jinja2 import contextfilter
from hmd_lib_mickey.phases import BuildEnvironment
from hmd_lib_mickey.types import MickeyRunConfiguration


def snake_to_pascal(name_in_snake):
    return "".join([n.capitalize() for n in name_in_snake.split("_")])


def extract_namespace(fully_qualified_name):
    parts = fully_qualified_name.rsplit(".", maxsplit=1)
    return "" if len(parts) == 1 else parts[0]


def extract_class(fully_qualified_name):
    parts = fully_qualified_name.rsplit(".", maxsplit=1)
    return snake_to_pascal(parts[-1])


def extract_attribute_ts_type(attr_spec):
    attr_type = attr_spec.get("type", None)

    if attr_type == "string":
        return "string"
    elif attr_type == "integer" or attr_type == "float":
        return "number"
    elif attr_type == "enum":
        return " | ".join(list(map(lambda d: f"'{d}'", attr_spec.get("enum_def", []))))
    else:
        return "any"


field_type_mapping = {
    "enum": "str",
    "float": "float",
    "integer": "int",
    "string": "str",
    "timestamp": "datetime",
    "collection": "List",
    "mapping": "Dict",
    "blob": "bytes",
}


def python_field_type(hmd_field_type: str):
    return field_type_mapping.get(hmd_field_type, "Any")


@contextfilter
def insert_context(context, _):
    return str(context["data"])


@contextfilter
def entity_type(context, _):
    return snake_to_pascal(context["data"]["metatype"])


def reverse_namespace(namespace):
    return "_".join(reversed(namespace.split(".")))


def puml_line_string(relationship_data):
    result = "--"
    if "adornments" in relationship_data:
        from_arrow = "<" if relationship_data["adornments"]["ref_from"]["arrow"] else ""
        from_card = relationship_data["adornments"]["ref_from"]["cardinality"]
        to_arrow = ">" if relationship_data["adornments"]["ref_to"]["arrow"] else ""
        to_card = relationship_data["adornments"]["ref_to"]["cardinality"]
        result = f'"{from_card}" {from_arrow}{result}{to_arrow} "{to_card}"'

    return result


def puml_line_string_from(relationship_data):
    result = "--"
    if "adornments" in relationship_data:
        from_arrow = "<" if relationship_data["adornments"]["ref_from"]["arrow"] else ""
        from_card = relationship_data["adornments"]["ref_from"]["cardinality"]
        result = f'"{from_card}" {from_arrow}{result}'

    return result


def puml_line_string_to(relationship_data):
    result = "--"
    if "adornments" in relationship_data:
        to_arrow = ">" if relationship_data["adornments"]["ref_to"]["arrow"] else ""
        to_card = relationship_data["adornments"]["ref_to"]["cardinality"]
        result = f'{result}{to_arrow} "{to_card}"'

    return result


def extract_top_level_namespace(namespace: str) -> str:
    return namespace.split(".")[0]


def is_dict(value):
    return isinstance(value, dict)


@BuildEnvironment.post_hook
def add_jinja_filters(config: MickeyRunConfiguration):
    env = config.environment

    env.filters["snake_to_pascal"] = snake_to_pascal
    env.filters["extract_namespace"] = extract_namespace
    env.filters["extract_class"] = extract_class
    env.filters["insert_context"] = insert_context
    env.filters["entity_type"] = entity_type
    env.filters["reverse_namespace"] = reverse_namespace
    env.filters["extract_attribute_ts_type"] = extract_attribute_ts_type
    env.filters["python_field_type"] = python_field_type
    env.filters["puml_line_string"] = puml_line_string
    env.filters["puml_line_string_from"] = puml_line_string_from
    env.filters["puml_line_string_to"] = puml_line_string_to
    env.filters["is_dict"] = is_dict

    return config.copy(environment=env)
