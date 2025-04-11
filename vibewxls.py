import sys
import json
from pathlib import Path

def clean_text_and_dates(data): return [x.strip().title() if isinstance(x, str) else x for x in data]
def fix_encoding(data): return [x.encode('utf-8', errors='ignore').decode('utf-8') if isinstance(x, str) else x for x in data]

TASKS = {
    "1": clean_text_and_dates,
    "2": fix_encoding
}

def main():
    task_id, excel_range, input_file = sys.argv[1:4]
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    task_func = TASKS.get(task_id, lambda d: d)
    result = [{"cleaned": str(v)} for v in task_func(data)]
    with open("output.txt", "w", encoding='utf-8') as f:
        json.dump({"results": result}, f)

if __name__ == "__main__":
    main()
