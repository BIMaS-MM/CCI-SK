import os
import json
import yaml

SOURCE_DIR = os.path.join("data", "yaml")
OUTPUT_DIR = os.path.join("data", "json")

def convert_yaml_to_json():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    full_database = {}

    for filename in os.listdir(SOURCE_DIR):
        if filename.endswith(".yaml") or filename.endswith(".yml"):
            class_code = os.path.splitext(filename)[0]
            yaml_path = os.path.join(SOURCE_DIR, filename)
            json_path = os.path.join(OUTPUT_DIR, f"{class_code}.json")

            with open(yaml_path, "r", encoding="utf-8") as yf:
                data = yaml.safe_load(yf)

            # Write individual class JSON
            with open(json_path, "w", encoding="utf-8") as jf:
                json.dump(data, jf, indent=2, ensure_ascii=False)

            full_database[class_code] = data
            print(f"Converted: {filename} -> {class_code}.json")

    # Write aggregated full database file
    full_json_path = os.path.join(OUTPUT_DIR, "cci_full.json")
    with open(full_json_path, "w", encoding="utf-8") as fjf:
        json.dump(full_database, fjf, indent=2, ensure_ascii=False)
    
    print(f"Aggregated database created at: {full_json_path}")

if __name__ == "__main__":
    convert_yaml_to_json()