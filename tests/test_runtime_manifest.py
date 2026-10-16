import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_application_manifest_schema_is_present():
    schema = json.loads((ROOT / "runtime" / "manifest.schema.json").read_text())
    assert schema["type"] == "object"
    assert set(schema["required"]) >= {
        "id",
        "name",
        "version",
        "architectures",
        "runtimes",
    }


def test_x86_image_manifest_declares_development_status():
    manifest = json.loads(
        (ROOT / "os" / "build" / "x86_64" / "image-manifest.json").read_text()
    )
    assert manifest["product"] == "B.I.N.E.S.H. OS"
    assert manifest["target"] == "x86_64"
    assert manifest["channel"] == "development"
    assert manifest["release_policy"]["production"] is False
