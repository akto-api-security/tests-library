#!/usr/bin/env python3
"""
Generate LLM test YAML files from scenario prompts and strategy meta prompts.

Each scenario is a specific test case (e.g. XSS via variable reassignment).
For each scenario x strategy combination, one YAML test file is generated.

Usage:
    python3 generate_new_tests.py <template_file>

Example:
    python3 generate_new_tests.py template.yml
"""

import argparse
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
            if all(not v or not v.strip() for v in row.values()):
                continue
            rows.append(row)
    return rows


def generate_id(scenario_id, strategy):
    """Generate test ID from scenario ID and strategy."""
    parts = []
    for part in [scenario_id, strategy]:
        cleaned = re.sub(r'[^A-Za-z0-9]+', '_', part.strip())
        cleaned = cleaned.upper().strip('_')
        parts.append(cleaned)
    return '_'.join(parts)


def generate_name(scenario_name, strategy):
    """Generate human-readable test name."""
    return f"{scenario_name} - {strategy}"


def generate_description(scenario_name, strategy, scenario_prompt):
    """Generate test description."""
    first_sentence = scenario_prompt.split('.')[0].strip()
    return f"Tests {scenario_name} using {strategy} strategy. {first_sentence}."


def generate_details(scenario_prompt, strategy_prompt):
    """Generate detailed description."""
    subcat_short = scenario_prompt.split('.')[0].replace('\n', ' ').strip()
    strategy_short = strategy_prompt.split('.')[0].replace('\n', ' ').strip()
    return f"This test combines {subcat_short} with the strategy: {strategy_short}"


def generate_category_name(top_category):
    """Generate AGENTIC_* category name from top category."""
    cleaned = re.sub(r'[^A-Za-z0-9]+', '_', top_category.strip())
    cleaned = cleaned.upper().strip('_')
    return f"AGENTIC_{cleaned}"


def generate_category_display_name(top_category):
    """Generate human-readable category display name."""
    return top_category.strip()


def generate_impact(top_category, scenario_name):
    """Generate impact statement based on top category."""
    impact_map = {
        'Security': f"Successful exploitation of {scenario_name} could lead to unauthorized access, data breaches, or system compromise.",
        'Safety': f"This {scenario_name} vulnerability could result in harmful outputs, policy violations, or exposure of sensitive information.",
        'Hallucination and Trustworthiness': f"Failures in {scenario_name} could undermine user trust and lead to misinformation or incorrect decisions.",
        'Business Alignment': f"Violations in {scenario_name} could lead to business policy breaches, legal liability, or misalignment with intended use cases."
    }
    return impact_map.get(
        top_category,
        f"This vulnerability in {scenario_name} could have significant security or operational implications."
    )


def escape_yaml_string(value):
    """Escape a string value for YAML."""
    if not isinstance(value, str):
        return str(value)

    value = value.replace('\n', ' ').replace('\r', ' ')
    value = ' '.join(value.split())

    special_chars = [':', '{', '}', '[', ']', ',', '&', '*', '#', '?', '|', '-', '<', '>', '=', '!', '%', '@', '`']
    needs_quoting = any(char in value for char in special_chars)

    if value.startswith(' ') or value.endswith(' ') or '"' in value or "'" in value:
        needs_quoting = True

    if needs_quoting:
        value = value.replace('\\', '\\\\').replace('"', '\\"')
        return f'"{value}"'

    return value


def fill_template(template_content, replacements):
    """Fill template placeholders with replacement values."""
    result = template_content
    for key, value in replacements.items():
        placeholder = f"{{{{{key}}}}}"
        if isinstance(value, str):
            value = escape_yaml_string(value)
        result = result.replace(placeholder, str(value))
    return result


def generate_tests(scenario_file, strategy_file, template_file, output_dir):
    """Generate all test files from scenario x strategy combinations."""
    scenarios = read_csv_file(scenario_file)
    strategies = read_csv_file(strategy_file)

    with open(template_file, 'r', encoding='utf-8') as f:
        template_content = f.read()

    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    generated_count = 0
    category_pairs = set()

    for scenario in scenarios:
        scenario_id = scenario['ScenarioID'].strip()
        scenario_name = scenario['ScenarioName'].strip()
        top_category = scenario['TopCategory'].strip()
        scenario_prompt = scenario['MetaPrompt'].strip()

        if not scenario_id or not scenario_name or not top_category or not scenario_prompt:
            continue

        category_name = generate_category_name(top_category)
        category_display_name = "Agent " + generate_category_display_name(top_category)
        category_pairs.add((category_name, category_display_name))

        for strat in strategies:
            strategy = strat['Strategy'].strip()
            strategy_prompt = strat['MetaPrompt'].strip()

            if not strategy or not strategy_prompt:
                continue

            test_id = generate_id(scenario_id, strategy)
            test_name = generate_name(scenario_name, strategy)
            description = generate_description(scenario_name, strategy, scenario_prompt)
            details = generate_details(scenario_prompt, strategy_prompt)
            impact = generate_impact(top_category, scenario_name)

            replacements = {
                'ID': test_id,
                'NAME': test_name,
                'DESCRIPTION': description,
                'DETAILS': details,
                'IMPACT': impact,
                'CATEGORY_NAME': category_name,
                'CATEGORY_DISPLAY_NAME': category_display_name,
                'CATEGORY_PROMPT': scenario_prompt,
                'STRATEGY_PROMPT': strategy_prompt
            }

            test_content = fill_template(template_content, replacements)

            output_file = output_path / f"{test_id}.yml"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(test_content)

            generated_count += 1
            print(f"Generated: {output_file.name}")

    print(f"\n✓ Successfully generated {generated_count} test files in {output_dir}/")

    print("\n" + "=" * 60)
    print("Category Name and Display Name Pairs:")
    print("=" * 60)
    for cat_name, cat_display_name in sorted(category_pairs):
        print(f"  {cat_name} -> {cat_display_name}")
    print("=" * 60)

    return generated_count, category_pairs


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Generate LLM test YAML files from scenario and strategy meta prompts.'
    )
    parser.add_argument(
        'template',
        type=str,
        help='Template YAML file name (e.g., template.yml)'
    )

    args = parser.parse_args()

    script_dir = Path(__file__).parent

    scenario_file = script_dir / "scenario_prompts.csv"
    strategy_file = script_dir / "strategy_meta_prompts.csv"
    template_file = script_dir / args.template
    output_dir = script_dir / "new_generated_tests"

    print("=" * 60)
    print("LLM Security Test Generator - Scenario-Based")
    print("=" * 60)
    print(f"\nInput files:")
    print(f"  - Scenarios:   {scenario_file.name}")
    print(f"  - Strategies:  {strategy_file.name}")
    print(f"  - Template:    {template_file.name}")
    print(f"\nOutput directory: {output_dir.name}/")
    print("\nGenerating tests...\n")

    for filepath in [scenario_file, strategy_file, template_file]:
        if not filepath.exists():
            print(f"ERROR: File not found: {filepath}")
            return 1

    try:
        count, category_pairs = generate_tests(scenario_file, strategy_file, template_file, output_dir)
        return 0
    except Exception as e:
        print(f"\nERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    exit(main())
