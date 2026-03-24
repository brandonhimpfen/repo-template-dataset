# solo-travel-sample-dataset

A gold-standard example dataset repository containing a small fictional dataset for solo traveler destination snapshots.

## Purpose

This repository demonstrates how a structured open dataset repository can be documented, validated, and maintained using repository standards and checklists.

## Dataset

The sample dataset includes fictional destination records with fields for:

- identifier
- destination name
- country code
- region
- primary language
- currency code
- solo travel suitability score
- digital nomad suitability score

## Files

```text
data/
  destinations.json
schema/
  destinations.schema.json
docs/
  data-dictionary.md
scripts/
  validate_dataset.py
```

## Validation

The included validation script checks:

- that the JSON file is valid
- that required fields are present
- that numeric scores fall within expected ranges

Run:

```bash
python scripts/validate_dataset.py
```

## Notes

This is a fictional dataset intended only as a repository quality example.

## License

MIT
