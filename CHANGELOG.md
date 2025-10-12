# Changelog

## [1.1.0] - 2025-10-12
### Added
- Inline style headers at the start of each value:
  - Long form: `$[r,b]text` (comma-separated alphanumerics).
  - Short form: `$rtext` (single alphanumeric tag).
- Inline headers **take precedence per value**; the overall `s=` style is applied afterwards to all values.

## [1.0.3] - 2025-10-12
### Removed
- Print function of style() removed to eliminate type mismatches, as it was not a useful feature.

## [1.0.2] - 2024-08-12
### Changed
- Typing suggestions for lambda functions added.

## [1.0.1] - 2024-06-29
### Changed
- Added upper character support.
- Version check for Literal package.
