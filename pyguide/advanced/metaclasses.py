"""
Metaclasses are classes that create classes. They allow you to modify
class creation at runtime, enabling patterns like automatic registration,
attribute validation, and singleton enforcement.

This module demonstrates several metaclass patterns:
1. Basic metaclass with __new__ and __init__
2. Attribute enforcement metaclass
3. Class registry pattern
4. Singleton metaclass
"""

from abc import ABC


class UppercaseAttrMeta(type):
    """Metaclass that converts class attribute names to uppercase."""

    def __new__(mcs, name, bases, namespace):
        uppercase_attrs = {}
        for attr_name, attr_value in namespace.items():
            if not attr_name.startswith("_"):
                uppercase_attrs[attr_name.upper()] = attr_value
            else:
                uppercase_attrs[attr_name] = attr_value
        return super().__new__(mcs, name, bases, uppercase_attrs)


class RequiredMethodsMeta(type):
    """Metaclass that enforces required methods on subclasses."""

    required_methods: list[str] = []

    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)

        if namespace.get("__abstract__"):
            return cls

        for method in mcs.required_methods:
            if method not in namespace or not callable(namespace[method]):
                raise TypeError(
                    f"Class '{name}' must implement method '{method}'"
                )
        return cls


class PluginMeta(type):
    """Metaclass that automatically registers classes in a registry."""

    registry: dict[str, type] = {}

    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)

        if namespace.get("__abstract__"):
            return cls

        plugin_name = namespace.get("__plugin_name__", name.lower())
        mcs.registry[plugin_name] = cls
        return cls

    @classmethod
    def get_plugin(mcs, name: str):
        """Retrieve a plugin by name."""
        return mcs.registry.get(name)

    @classmethod
    def clear_registry(mcs):
        """Clear the registry for testing."""
        mcs.registry.clear()


class SingletonMeta(type):
    """Metaclass that ensures only one instance of a class exists."""

    _instances: dict[type, object] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

    @classmethod
    def clear_instances(mcs):
        """Clear instances for testing."""
        mcs._instances.clear()


class ValidatedFieldsMeta(type):
    """Metaclass that validates field types on class creation."""

    def __new__(mcs, name, bases, namespace):
        field_types = namespace.get("__field_types__", {})
        cls = super().__new__(mcs, name, bases, namespace)

        if field_types:
            original_init = cls.__init__

            def validated_init(self, **kwargs):
                for field, expected_type in field_types.items():
                    if field in kwargs:
                        value = kwargs[field]
                        if not isinstance(value, expected_type):
                            raise TypeError(
                                f"Field '{field}' must be {expected_type.__name__}, "
                                f"got {type(value).__name__}"
                            )
                original_init(self, **kwargs)

            cls.__init__ = validated_init

        return cls


class UpperDemo(metaclass=UppercaseAttrMeta):
    """Demo class using UppercaseAttrMeta."""

    name = "demo"
    value = 42


class BasePlugin(metaclass=PluginMeta):
    """Base class for plugins."""

    __abstract__ = True

    def execute(self):
        raise NotImplementedError


class JSONPlugin(BasePlugin):
    """JSON format plugin."""

    __plugin_name__ = "json"

    def execute(self):
        return "JSON output"


class XMLPlugin(BasePlugin):
    """XML format plugin."""

    __plugin_name__ = "xml"

    def execute(self):
        return "XML output"


class DatabaseConnection(metaclass=SingletonMeta):
    """Database connection that should only exist once."""

    def __init__(self, host="localhost", port=5432):
        self.host = host
        self.port = port
        self.connected = True


class ValidatedPerson(metaclass=ValidatedFieldsMeta):
    """Person class with validated fields."""

    __field_types__ = {"name": str, "age": int}

    def __init__(self, **kwargs):
        self.name = kwargs.get("name", "")
        self.age = kwargs.get("age", 0)


def main():
    # UppercaseAttrMeta converts attribute names to uppercase
    assert hasattr(UpperDemo, "NAME")
    assert hasattr(UpperDemo, "VALUE")
    assert UpperDemo.NAME == "demo"
    assert UpperDemo.VALUE == 42
    assert not hasattr(UpperDemo, "name")

    # PluginMeta automatically registers classes
    PluginMeta.clear_registry()

    class TestPlugin(BasePlugin):
        __plugin_name__ = "test"

        def execute(self):
            return "test"

    assert "test" in PluginMeta.registry
    assert PluginMeta.get_plugin("test") is TestPlugin

    # SingletonMeta ensures only one instance
    SingletonMeta.clear_instances()
    conn1 = DatabaseConnection("db.example.com", 3306)
    conn2 = DatabaseConnection("other.host.com", 5432)
    assert conn1 is conn2
    assert conn1.host == "db.example.com"
    assert conn2.host == "db.example.com"

    # ValidatedFieldsMeta validates field types
    person = ValidatedPerson(name="Alice", age=30)
    assert person.name == "Alice"
    assert person.age == 30

    try:
        ValidatedPerson(name="Bob", age="thirty")
        assert False, "Should have raised TypeError"
    except TypeError as e:
        assert "must be int" in str(e)

    # Metaclass hierarchy
    assert isinstance(UpperDemo, UppercaseAttrMeta)
    assert isinstance(UppercaseAttrMeta, type)
    assert isinstance(type, type)

    # All metaclasses derive from type
    assert issubclass(UppercaseAttrMeta, type)
    assert issubclass(PluginMeta, type)
    assert issubclass(SingletonMeta, type)

    # type creates classes, metaclasses customize that creation
    DynamicClass = type("DynamicClass", (), {"x": 10})
    assert DynamicClass.x == 10
    assert isinstance(DynamicClass, type)


if __name__ == "__main__":
    main()
