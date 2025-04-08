import json

# Input and output file paths
input_file = "./data/cybersecurity/ilab_generated/test_gen.jsonl"
output_file = "test_gen.jsonl"

# Read from original JSONL and reformat
with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
    for line in infile:
        entry = json.loads(line)
        new_format = {
            "messages": [
                {"role": "system", "content": entry["system"]},
                {"role": "user", "content": entry["user"]},
                {"role": "assistant", "content": entry["assistant"]}
            ]
        }
        outfile.write(json.dumps(new_format, ensure_ascii=False) + "\n")