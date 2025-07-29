import os
import yaml

def update_subcategory_in_info(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".yaml") or filename.endswith(".yml"):
            filepath = os.path.join(folder_path, filename)

            with open(filepath, 'r') as file:
                try:
                    data = yaml.safe_load(file)
                except Exception as e:
                    print(f"[ERROR] Failed to parse {filename}: {e}")
                    continue

            if not isinstance(data, dict) or 'id' not in data:
                print(f"[SKIPPED] {filename} has no top-level 'id'.")
                continue

            if 'info' not in data or not isinstance(data['info'], dict):
                data['info'] = {}

            data['info']['subCategory'] = data['id']

            with open(filepath, 'w') as file:
                yaml.dump(data, file, sort_keys=False)

            print(f"[UPDATED] {filename}: info.subCategory set to '{data['id']}'")

# 🔁 Replace with your YAML test folder
folder_path = "chargebee_tests"
update_subcategory_in_info(folder_path)
