"""Tests for data formats module."""

import json

from pyguide.advanced.data_formats import (
    main as data_main,
    JSON_DATA,
    XML_DATA,
    CSV_DATA,
    User,
    parse_json,
    serialize_json,
    parse_json_to_users,
    parse_xml,
    parse_xml_to_users,
    users_to_xml,
    parse_csv,
    parse_csv_to_users,
    users_to_csv,
    json_to_xml,
    xml_to_json,
    csv_to_json,
    CustomEncoder,
)


class TestDataFormatsModule:
    """Tests for the data formats demonstration module."""

    def test_main_runs_without_error(self):
        """main() should execute without raising any exceptions."""
        data_main()

    def test_user_from_dict(self):
        """User.from_dict should create User from dict."""
        data = {"id": "1", "name": "Test", "email": "test@test.com", "active": "true"}
        user = User.from_dict(data)
        assert user.id == 1
        assert user.name == "Test"
        assert user.active is True

    def test_user_to_dict(self):
        """User.to_dict should convert to dict."""
        user = User(id=1, name="Test", email="t@t.com", active=True)
        d = user.to_dict()
        assert d["id"] == 1
        assert d["name"] == "Test"

    def test_user_field_names(self):
        """User.field_names should return field names."""
        names = User.field_names()
        assert "id" in names
        assert "name" in names
        assert "email" in names
        assert "active" in names

    def test_parse_json(self):
        """parse_json should parse JSON string."""
        result = parse_json('[{"a": 1}]')
        assert result == [{"a": 1}]

    def test_serialize_json(self):
        """serialize_json should create JSON string."""
        result = serialize_json({"key": "value"})
        assert '"key": "value"' in result

    def test_parse_json_to_users(self):
        """parse_json_to_users should create User list."""
        users = parse_json_to_users(JSON_DATA)
        assert len(users) == 3
        assert users[0].name == "Alice"

    def test_parse_xml(self):
        """parse_xml should parse XML string."""
        root = parse_xml("<root><child>text</child></root>")
        assert root.tag == "root"
        assert root.find("child").text == "text"

    def test_parse_xml_to_users(self):
        """parse_xml_to_users should create User list."""
        users = parse_xml_to_users(XML_DATA)
        assert len(users) == 3
        assert users[0].email == "alice@example.com"

    def test_users_to_xml(self):
        """users_to_xml should serialize users to XML."""
        users = [User(id=1, name="Test", email="t@t.com", active=True)]
        xml = users_to_xml(users)
        assert "<name>Test</name>" in xml
        assert 'id="1"' in xml

    def test_parse_csv(self):
        """parse_csv should parse CSV string."""
        result = parse_csv("a,b\n1,2")
        assert result == [{"a": "1", "b": "2"}]

    def test_parse_csv_to_users(self):
        """parse_csv_to_users should create User list."""
        users = parse_csv_to_users(CSV_DATA)
        assert len(users) == 3
        assert users[2].name == "Charlie"

    def test_users_to_csv(self):
        """users_to_csv should serialize users to CSV."""
        users = [User(id=1, name="Test", email="t@t.com", active=True)]
        csv_str = users_to_csv(users)
        assert "id,name,email,active" in csv_str
        assert "Test" in csv_str

    def test_json_to_xml(self):
        """json_to_xml should convert JSON to XML."""
        xml = json_to_xml(JSON_DATA)
        assert "<name>Alice</name>" in xml

    def test_xml_to_json(self):
        """xml_to_json should convert XML to JSON."""
        json_str = xml_to_json(XML_DATA)
        assert '"name": "Alice"' in json_str

    def test_csv_to_json(self):
        """csv_to_json should convert CSV to JSON."""
        json_str = csv_to_json(CSV_DATA)
        assert '"name": "Alice"' in json_str

    def test_custom_encoder(self):
        """CustomEncoder should encode User objects."""
        user = User(id=1, name="Test", email="t@t.com", active=True)
        result = json.dumps(user, cls=CustomEncoder)
        assert "Test" in result

    def test_formats_equivalent(self):
        """All formats should produce equivalent users."""
        json_users = parse_json_to_users(JSON_DATA)
        xml_users = parse_xml_to_users(XML_DATA)
        csv_users = parse_csv_to_users(CSV_DATA)

        for j, x, c in zip(json_users, xml_users, csv_users):
            assert j.id == x.id == c.id
            assert j.name == x.name == c.name

    def test_user_active_from_bool(self):
        """User should handle bool active value."""
        data = {"id": 1, "name": "T", "email": "e", "active": True}
        user = User.from_dict(data)
        assert user.active is True

    def test_roundtrip_json(self):
        """JSON should round-trip correctly."""
        users = parse_json_to_users(JSON_DATA)
        json_str = serialize_json([u.to_dict() for u in users])
        reparsed = parse_json_to_users(json_str)
        assert len(reparsed) == len(users)
        assert reparsed[0].name == users[0].name

    def test_roundtrip_xml(self):
        """XML should round-trip correctly."""
        users = parse_xml_to_users(XML_DATA)
        xml_str = users_to_xml(users)
        reparsed = parse_xml_to_users(xml_str)
        assert len(reparsed) == len(users)

    def test_roundtrip_csv(self):
        """CSV should round-trip correctly."""
        users = parse_csv_to_users(CSV_DATA)
        csv_str = users_to_csv(users)
        reparsed = parse_csv_to_users(csv_str)
        assert len(reparsed) == len(users)
