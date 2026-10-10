# solo-travel-sample-dataset

[![Support Open Work](https://img.shields.io/badge/Support-Open%20Work-0A0A0A?style=flat&logo=github)](https://github.com/brandonhimpfen/support) 
[![GitHub Sponsor](https://srv-cdn.himpfen.io/badges/github/github-flat.svg)](https://github.com/sponsors/brandonhimpfen) 
[![Buy Me a Coffee](https://srv-cdn.himpfen.io/badges/buymeacoffee/buymeacoffee-flat.svg)](https://buymeacoffee.com/brandonhimpfen) 
[![Ko-Fi](https://srv-cdn.himpfen.io/badges/kofi/kofi-flat.svg)](https://ko-fi.com/brandonhimpfen) 
[![PayPal](https://srv-cdn.himpfen.io/badges/paypal/paypal-flat.svg)](https://paypal.me/brandonhimpfen)

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
