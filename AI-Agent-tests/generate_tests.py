#!/usr/bin/env python3
"""
Generate LLM test YAML files from subcategory and strategy meta prompts.
"""

import csv
import os
import re
from pathlib import Path


def read_csv_file(filepath):
    """Read CSV file and return rows as list of dictionaries."""
    rows = []
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Skip empty rows
            if all(not v or not v.strip() for v in row.values()):
                continue
            rows.append(row)
    return rows


def generate_id(top_category, subcategory, strategy):
    """Generate test ID from category, subcategory and strategy."""
    # Convert to uppercase and replace spaces/special chars with underscores
    parts = []
    for part in [top_category, subcategory, strategy]:
        cleaned = re.sub(r'[^A-Za-z0-9]+', '_', part.strip())
        cleaned = cleaned.upper().strip('_')
        parts.append(cleaned)

    return '_'.join(parts)


def generate_name(top_category, subcategory, strategy):
    """Generate test name."""
    return f"{top_category} - {subcategory} - {strategy}"


def generate_description(subcategory, strategy, subcategory_prompt):
    """Generate test description."""
    # Extract first sentence or first 100 chars from subcategory prompt
    first_sentence = subcategory_prompt.split('.')[0]
    if len(first_sentence) > 150:
        first_sentence = first_sentence[:150] + "..."

    return f"Tests {subcategory} vulnerability using {strategy} strategy. {first_sentence}."


def generate_details(subcategory_prompt, strategy_prompt):
    """Generate detailed description."""
    # Keep it simple and on one line to avoid YAML issues
    subcat_short = subcategory_prompt[:150].replace('\n', ' ').strip()
    strategy_short = strategy_prompt[:150].replace('\n', ' ').strip()

    details = f"This test combines {subcat_short}... with the strategy: {strategy_short}..."
    return details


def generate_impact(top_category, subcategory):
    """Generate impact statement based on category."""
    impact_map = {
        'Security': f"Successful exploitation of {subcategory} vulnerabilities could lead to unauthorized access, data breaches, or system compromise.",
        'Safety': f"This {subcategory} vulnerability could result in harmful outputs, policy violations, or exposure of sensitive information.",
        'Hallucination & Trustworthiness': f"Failures in {subcategory} could undermine user trust and lead to misinformation or incorrect decisions.",
        'Business Alignment': f"Violations in {subcategory} could lead to business policy breaches, legal liability, or misalignment with intended use cases."
    }

    return impact_map.get(top_category, f"This vulnerability in {subcategory} could have significant security or operational implications.")


def escape_yaml_string(value):
    """Escape a string value for YAML."""
    if not isinstance(value, str):
        return str(value)

    # Remove newlines and extra whitespace
    value = value.replace('\n', ' ').replace('\r', ' ')
    value = ' '.join(value.split())  # Normalize whitespace

    # Escape special YAML characters
    # If the string contains special characters, we need to quote it
    special_chars = [':', '{', '}', '[', ']', ',', '&', '*', '#', '?', '|', '-', '<', '>', '=', '!', '%', '@', '`']
    needs_quoting = any(char in value for char in special_chars)

    # Check for leading/trailing spaces or quotes
    if value.startswith(' ') or value.endswith(' ') or '"' in value or "'" in value:
        needs_quoting = True

    if needs_quoting:
        # Use double quotes and escape internal quotes
        value = value.replace('\\', '\\\\').replace('"', '\\"')
        return f'"{value}"'

    return value


def fill_template(template_content, replacements):
    """Fill template with replacement values."""
    result = template_content
    for key, value in replacements.items():
        placeholder = f"{{{{{key}}}}}"
        # Escape value for YAML
        if isinstance(value, str):
            value = escape_yaml_string(value)
        result = result.replace(placeholder, str(value))
    return result


def generate_tests(subcategory_file, strategy_file, template_file, output_dir):
    """Generate all test files."""
    # Read input files
    subcategories = read_csv_file(subcategory_file)
    strategies = read_csv_file(strategy_file)

    with open(template_file, 'r', encoding='utf-8') as f:
        template_content = f.read()

    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    generated_count = 0

    # Generate test for each combination
    for subcat in subcategories:
        top_category = subcat['TopCategory'].strip()
        subcategory = subcat['Subcategory'].strip()
        category_prompt = subcat['MetaPrompt'].strip()

        if not top_category or not subcategory or not category_prompt:
            continue

        for strat in strategies:
            strategy = strat['Strategy'].strip()
            strategy_prompt = strat['MetaPrompt'].strip()

            if not strategy or not strategy_prompt:
                continue

            # Generate test metadata
            test_id = generate_id(top_category, subcategory, strategy)
            test_name = generate_name(top_category, subcategory, strategy)
            description = generate_description(subcategory, strategy, category_prompt)
            details = generate_details(category_prompt, strategy_prompt)
            impact = generate_impact(top_category, subcategory)

            # Prepare replacements
            replacements = {
                'ID': test_id,
                'NAME': test_name,
                'DESCRIPTION': description,
                'DETAILS': details,
                'IMPACT': impact,
                'CATEGORY_PROMPT': category_prompt,
                'STRATEGY_PROMPT': strategy_prompt
            }

            # Fill template
            test_content = fill_template(template_content, replacements)

            # Write output file
            output_file = output_path / f"{test_id}.yml"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(test_content)

            generated_count += 1
            print(f"Generated: {output_file.name}")

    print(f"\n✓ Successfully generated {generated_count} test files in {output_dir}/")
    return generated_count


def main():
    """Main entry point."""
    script_dir = Path(__file__).parent

    subcategory_file = script_dir / "subcategory_meta_prompts.csv"
    strategy_file = script_dir / "strategy_meta_prompts.csv"
    template_file = script_dir / "template.yml"
    output_dir = script_dir / "generated_tests"

    print("=" * 60)
    print("LLM Security Test Generator")
    print("=" * 60)
    print(f"\nInput files:")
    print(f"  - Subcategories: {subcategory_file.name}")
    print(f"  - Strategies: {strategy_file.name}")
    print(f"  - Template: {template_file.name}")
    print(f"\nOutput directory: {output_dir.name}/")
    print("\nGenerating tests...\n")

    # Check if files exist
    for filepath in [subcategory_file, strategy_file, template_file]:
        if not filepath.exists():
            print(f"ERROR: File not found: {filepath}")
            return 1

    # Generate tests
    try:
        count = generate_tests(subcategory_file, strategy_file, template_file, output_dir)
        return 0
    except Exception as e:
        print(f"\nERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    exit(main())
