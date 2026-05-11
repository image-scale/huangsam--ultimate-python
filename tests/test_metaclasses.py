"""Tests for metaclass module."""

from pyguide.advanced.metaclasses import (
    main as metaclasses_main,
    UppercaseAttrMeta,
    RequiredMethodsMeta,
    PluginMeta,
    SingletonMeta,
    ValidatedFieldsMeta,
    UpperDemo,
    BasePlugin,
    DatabaseConnection,
    ValidatedPerson,
)


class TestMetaclassModule:
    """Tests for the metaclass demonstration module."""

    def test_main_runs_without_error(self):
        """main() should execute without raising any exceptions."""
        metaclasses_main()

    def test_uppercase_attr_meta(self):
        """UppercaseAttrMeta should convert attributes to uppercase."""
        assert hasattr(UpperDemo, "NAME")
        assert hasattr(UpperDemo, "VALUE")
        assert UpperDemo.NAME == "demo"
        assert not hasattr(UpperDemo, "name")

    def test_uppercase_preserves_dunder(self):
        """UppercaseAttrMeta should preserve dunder attributes."""
        assert hasattr(UpperDemo, "__module__")
        assert hasattr(UpperDemo, "__doc__")

    def test_plugin_registry(self):
        """PluginMeta should register plugins automatically."""
        PluginMeta.clear_registry()

        class TestPlugin(BasePlugin):
            __plugin_name__ = "test_plugin"

            def execute(self):
                return "result"

        assert "test_plugin" in PluginMeta.registry
        assert PluginMeta.get_plugin("test_plugin") is TestPlugin

    def test_plugin_default_name(self):
        """PluginMeta should use lowercase class name if no custom name."""
        PluginMeta.clear_registry()

        class MyCustomPlugin(BasePlugin):
            def execute(self):
                return "custom"

        assert "mycustomplugin" in PluginMeta.registry

    def test_abstract_not_registered(self):
        """Abstract classes should not be registered."""
        PluginMeta.clear_registry()

        class AbstractPlugin(BasePlugin):
            __abstract__ = True

        assert "abstractplugin" not in PluginMeta.registry

    def test_singleton_meta(self):
        """SingletonMeta should return same instance."""
        SingletonMeta.clear_instances()
        conn1 = DatabaseConnection("host1", 1234)
        conn2 = DatabaseConnection("host2", 5678)
        assert conn1 is conn2
        assert conn1.host == "host1"

    def test_singleton_different_classes(self):
        """Different singleton classes should have different instances."""
        SingletonMeta.clear_instances()

        class SingletonA(metaclass=SingletonMeta):
            pass

        class SingletonB(metaclass=SingletonMeta):
            pass

        a1 = SingletonA()
        a2 = SingletonA()
        b1 = SingletonB()

        assert a1 is a2
        assert a1 is not b1

    def test_validated_fields_valid(self):
        """ValidatedFieldsMeta should accept valid types."""
        person = ValidatedPerson(name="Alice", age=30)
        assert person.name == "Alice"
        assert person.age == 30

    def test_validated_fields_invalid(self):
        """ValidatedFieldsMeta should reject invalid types."""
        try:
            ValidatedPerson(name=123, age=30)
            assert False, "Should raise TypeError"
        except TypeError as e:
            assert "must be str" in str(e)

    def test_metaclass_isinstance(self):
        """Classes should be instances of their metaclass."""
        assert isinstance(UpperDemo, UppercaseAttrMeta)
        assert isinstance(BasePlugin, PluginMeta)
        assert isinstance(DatabaseConnection, SingletonMeta)

    def test_metaclass_is_type(self):
        """All metaclasses should be subclasses of type."""
        assert issubclass(UppercaseAttrMeta, type)
        assert issubclass(PluginMeta, type)
        assert issubclass(SingletonMeta, type)
        assert issubclass(ValidatedFieldsMeta, type)

    def test_required_methods_meta(self):
        """RequiredMethodsMeta should enforce method implementation."""

        class StrictMeta(RequiredMethodsMeta):
            required_methods = ["process", "validate"]

        try:

            class IncompleteClass(metaclass=StrictMeta):
                def process(self):
                    pass

            assert False, "Should raise TypeError"
        except TypeError as e:
            assert "must implement method 'validate'" in str(e)

    def test_required_methods_satisfied(self):
        """RequiredMethodsMeta should allow complete implementations."""

        class StrictMeta(RequiredMethodsMeta):
            required_methods = ["process"]

        class CompleteClass(metaclass=StrictMeta):
            def process(self):
                return "done"

        obj = CompleteClass()
        assert obj.process() == "done"
