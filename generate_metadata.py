import os
import json
import re

PROBLEMS_DIR = "problems"
OUTPUT_FILE = "metadata.json"

def extract_metadata(docstring):
    metadata = {
        "number": "",
        "title": ""
    }

    number_match = re.search(r"Question Number:\s*(\d+)", docstring)
    title_match = re.search(r"Title:\s*(.+)", docstring)

    if number_match:
        metadata["number"] = number_match.group(1).zfill(3)
    if title_match:
        metadata["title"] = title_match.group(1).strip()

    return metadata

def read_docstring(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    match = re.search(r'"""(.*?)"""', content, re.DOTALL) or \
            re.search(r"'''(.*?)'''", content, re.DOTALL)

    return match.group(1).strip() if match else ""

def generate_metadata():
    metadata_list = []

    for folder in sorted(os.listdir(PROBLEMS_DIR)):
        folder_path = os.path.join(PROBLEMS_DIR, folder)
        question_path = os.path.join(folder_path, "question.py")

        if os.path.isdir(folder_path) and os.path.isfile(question_path):
            docstring = read_docstring(question_path)
            metadata = extract_metadata(docstring)
            metadata["folder"] = folder

            if metadata["number"] and metadata["title"]:
                metadata_list.append(metadata)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(metadata_list, f, indent=4)

    print(f"Generated {OUTPUT_FILE} with {len(metadata_list)} entries.")

if __name__ == "__main__":
    generate_metadata()
