import json
import os

path = input("Please enter the absolute path of the JSON file: ").strip()

if not os.path.isfile(path):
    print("Error: File does not exist")
else:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    items = sorted(data.items(), key=lambda x: x[0])

    base = os.path.splitext(os.path.basename(path))[0]
    output_path = os.path.join(os.path.dirname(path), base + ".txt")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("| Date | DQ |\n")
        f.write("|---|---|\n")
        for date, value in items:
            f.write(f"| {date} | DQ{value} |\n")

    print("Conversion completed")
    print("Output file:", output_path)