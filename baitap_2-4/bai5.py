import os
import re

path = os.path.join(os.path.dirname(__file__), "demo_file2.txt")

with open(path, "r", encoding="utf-8") as f:
    text = f.read().lower()

words = re.findall(r'\b\w+\b', text)

count = {}
for w in words:
    count[w] = count.get(w, 0) + 1

print(count)