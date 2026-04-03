print("a) In nội dung trên 1 dòng:")
with open("demo_file1.txt", "r", encoding="utf-8") as f:
    print(f.read().replace("\n", " "))

print("\nb) In từng dòng:")
with open("demo_file1.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())