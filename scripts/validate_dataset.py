import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "destinations.json"
REQUIRED_FIELDS = {
    "id",
    "destination_name",
    "country_code",
    "region",
    "primary_language",
    "currency_code",
    "solo_travel_score",
    "digital_nomad_score",
}


def validate_record(record, index):
    missing = REQUIRED_FIELDS - set(record)
    if missing:
        raise ValueError(f"Record {index} is missing fields: {sorted(missing)}")

    for field in ("solo_travel_score", "digital_nomad_score"):
        value = record[field]
        if not isinstance(value, int) or not (0 <= value <= 100):
            raise ValueError(f"Record {index} field '{field}' must be an integer from 0 to 100")


def main():
    data = json.loads(DATA_FILE.read_text(encoding="utf8"))
    if not isinstance(data, list):
        raise ValueError("Dataset must be a JSON array")

    for index, record in enumerate(data, start=1):
        if not isinstance(record, dict):
            raise ValueError(f"Record {index} must be an object")
        validate_record(record, index)

    print(f"Validated {len(data)} records successfully.")


if __name__ == "__main__":
    main()
