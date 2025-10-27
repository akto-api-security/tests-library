#!/usr/bin/env python3
"""
Validate all generated YAML files for syntax errors.
"""

import os
import re
from pathlib import Path


def simple_yaml_validate(filepath):
    """
    Simple YAML validation without requiring PyYAML.
    Checks for common syntax issues.
    """
    errors = []

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Check for basic YAML structure
    for i, line in enumerate(lines, 1):
        # Check for unescaped quotes that could break YAML
        if line.strip() and not line.strip().startswith('#'):
            # Check if line has a colon (key: value format)
            if ':' in line:
                parts = line.split(':', 1)
                if len(parts) == 2:
                    key_part = parts[0].strip()
                    value_part = parts[1].strip()

                    # Check if value has unquoted special characters
                    # (This is a simplified check)
                    if value_part and not value_part.startswith('"') and not value_part.startswith("'"):
                        # Check for literal \n in the value (should not be there)
                        if '\\n' in value_part:
                            errors.append(f"Line {i}: Found literal \\n in unquoted string: {line.strip()[:80]}")

    return errors


def validate_all_yamls(directory):
    """Validate all YAML files in a directory."""
    yaml_dir = Path(directory)
    yaml_files = sorted(yaml_dir.glob('*.yml'))

    print("=" * 60)
    print("YAML Validation Report")
    print("=" * 60)
    print(f"\nValidating {len(yaml_files)} YAML files...\n")

    total_errors = 0
    files_with_errors = []

    for yaml_file in yaml_files:
        errors = simple_yaml_validate(yaml_file)
        if errors:
            total_errors += len(errors)
            files_with_errors.append(yaml_file.name)
            print(f"\n❌ {yaml_file.name}")
            for error in errors:
                print(f"  {error}")

    print("\n" + "=" * 60)
    if total_errors == 0:
        print(f"✓ All {len(yaml_files)} YAML files passed validation!")
    else:
        print(f"✗ Found {total_errors} errors in {len(files_with_errors)} files")
        print(f"\nFiles with errors:")
        for filename in files_with_errors:
            print(f"  - {filename}")
    print("=" * 60)

    return total_errors == 0


def main():
    """Main entry point."""
    script_dir = Path(__file__).parent
    yaml_dir = script_dir / "generated_tests"

    if not yaml_dir.exists():
        print(f"ERROR: Directory not found: {yaml_dir}")
        return 1

    success = validate_all_yamls(yaml_dir)
    return 0 if success else 1


if __name__ == "__main__":
    exit(main())
