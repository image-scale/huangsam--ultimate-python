"""
Python provides robust support for parsing and generating common data
formats. This module demonstrates working with JSON, XML, and CSV data
for reading, writing, and transforming structured data.

This module demonstrates:
1. JSON parsing and serialization
2. XML parsing with ElementTree
3. CSV reading and writing
4. Converting between formats
5. Custom serialization
"""

import csv
import json
from dataclasses import dataclass, asdict, fields
from io import StringIO
from xml.etree import ElementTree as ET


JSON_DATA = """
[
    {"id": 1, "name": "Alice", "email": "alice@example.com", "active": true},
    {"id": 2, "name": "Bob", "email": "bob@example.com", "active": false},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com", "active": true}
]
"""

XML_DATA = """
<users>
    <user id="1">
        <name>Alice</name>
        <email>alice@example.com</email>
        <active>true</active>
    </user>
    <user id="2">
        <name>Bob</name>
        <email>bob@example.com</email>
        <active>false</active>
    </user>
    <user id="3">
        <name>Charlie</name>
        <email>charlie@example.com</email>
        <active>true</active>
    </user>
</users>
"""

CSV_DATA = """id,name,email,active
1,Alice,alice@example.com,true
2,Bob,bob@example.com,false
3,Charlie,charlie@example.com,true"""


@dataclass
class User:
    """User model for data transformation."""

    id: int
    name: str
    email: str
    active: bool

    @classmethod
    def from_dict(cls, data: dict) -> "User":
        """Create User from dictionary."""
        return cls(
            id=int(data["id"]),
            name=str(data["name"]),
            email=str(data["email"]),
            active=data["active"]
            if isinstance(data["active"], bool)
            else data["active"].lower() == "true",
        )

    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return asdict(self)

    @classmethod
    def field_names(cls) -> list[str]:
        """Get field names."""
        return [f.name for f in fields(cls)]


def parse_json(json_str: str) -> list[dict]:
    """Parse JSON string to list of dictionaries."""
    return json.loads(json_str)


def serialize_json(data, indent: int = 2) -> str:
    """Serialize data to JSON string."""
    return json.dumps(data, indent=indent)


def parse_json_to_users(json_str: str) -> list[User]:
    """Parse JSON string to list of Users."""
    data = json.loads(json_str)
    return [User.from_dict(item) for item in data]


def parse_xml(xml_str: str) -> ET.Element:
    """Parse XML string to Element."""
    return ET.fromstring(xml_str)


def parse_xml_to_users(xml_str: str) -> list[User]:
    """Parse XML string to list of Users."""
    root = ET.fromstring(xml_str)
    users = []
    for user_elem in root.findall("user"):
        data = {
            "id": user_elem.get("id"),
            "name": user_elem.findtext("name"),
            "email": user_elem.findtext("email"),
            "active": user_elem.findtext("active"),
        }
        users.append(User.from_dict(data))
    return users


def users_to_xml(users: list[User]) -> str:
    """Serialize users to XML string."""
    root = ET.Element("users")
    for user in users:
        user_elem = ET.SubElement(root, "user", id=str(user.id))
        ET.SubElement(user_elem, "name").text = user.name
        ET.SubElement(user_elem, "email").text = user.email
        ET.SubElement(user_elem, "active").text = str(user.active).lower()
    return ET.tostring(root, encoding="unicode")


def parse_csv(csv_str: str) -> list[dict]:
    """Parse CSV string to list of dictionaries."""
    reader = csv.DictReader(StringIO(csv_str))
    return list(reader)


def parse_csv_to_users(csv_str: str) -> list[User]:
    """Parse CSV string to list of Users."""
    reader = csv.DictReader(StringIO(csv_str))
    return [User.from_dict(row) for row in reader]


def users_to_csv(users: list[User]) -> str:
    """Serialize users to CSV string."""
    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=User.field_names())
    writer.writeheader()
    for user in users:
        row = user.to_dict()
        row["active"] = str(row["active"]).lower()
        writer.writerow(row)
    return output.getvalue()


def json_to_xml(json_str: str) -> str:
    """Convert JSON data to XML."""
    users = parse_json_to_users(json_str)
    return users_to_xml(users)


def xml_to_json(xml_str: str) -> str:
    """Convert XML data to JSON."""
    users = parse_xml_to_users(xml_str)
    data = [user.to_dict() for user in users]
    return json.dumps(data, indent=2)


def csv_to_json(csv_str: str) -> str:
    """Convert CSV data to JSON."""
    users = parse_csv_to_users(csv_str)
    data = [user.to_dict() for user in users]
    return json.dumps(data, indent=2)


class CustomEncoder(json.JSONEncoder):
    """Custom JSON encoder for User objects."""

    def default(self, obj):
        if isinstance(obj, User):
            return obj.to_dict()
        return super().default(obj)


def main():
    # Parse JSON data
    json_users = parse_json_to_users(JSON_DATA)
    assert len(json_users) == 3
    assert json_users[0].name == "Alice"
    assert json_users[1].active is False

    # Parse XML data
    xml_users = parse_xml_to_users(XML_DATA)
    assert len(xml_users) == 3
    assert xml_users[0].email == "alice@example.com"

    # Parse CSV data
    csv_users = parse_csv_to_users(CSV_DATA)
    assert len(csv_users) == 3
    assert csv_users[2].name == "Charlie"

    # All formats produce equivalent users
    for json_user, xml_user, csv_user in zip(json_users, xml_users, csv_users):
        assert json_user.id == xml_user.id == csv_user.id
        assert json_user.name == xml_user.name == csv_user.name
        assert json_user.email == xml_user.email == csv_user.email
        assert json_user.active == xml_user.active == csv_user.active

    # Serialize to JSON
    json_output = serialize_json([u.to_dict() for u in json_users])
    assert "Alice" in json_output
    reparsed = parse_json(json_output)
    assert len(reparsed) == 3

    # Serialize to XML
    xml_output = users_to_xml(xml_users)
    assert "<name>Alice</name>" in xml_output
    reparsed_xml = parse_xml_to_users(xml_output)
    assert len(reparsed_xml) == 3

    # Serialize to CSV
    csv_output = users_to_csv(csv_users)
    assert "alice@example.com" in csv_output
    reparsed_csv = parse_csv_to_users(csv_output)
    assert len(reparsed_csv) == 3

    # Convert between formats
    xml_from_json = json_to_xml(JSON_DATA)
    assert "<name>Bob</name>" in xml_from_json

    json_from_xml = xml_to_json(XML_DATA)
    assert '"name": "Alice"' in json_from_xml

    json_from_csv = csv_to_json(CSV_DATA)
    assert '"email": "charlie@example.com"' in json_from_csv

    # Custom encoder
    users = parse_json_to_users(JSON_DATA)
    encoded = json.dumps(users, cls=CustomEncoder)
    assert "Alice" in encoded

    # JSON with nested data
    nested_json = '{"user": {"name": "Test", "tags": ["a", "b"]}}'
    parsed = json.loads(nested_json)
    assert parsed["user"]["tags"] == ["a", "b"]

    # XML attributes vs elements
    root = parse_xml(XML_DATA)
    first_user = root.find("user")
    assert first_user.get("id") == "1"
    assert first_user.findtext("name") == "Alice"


if __name__ == "__main__":
    main()
