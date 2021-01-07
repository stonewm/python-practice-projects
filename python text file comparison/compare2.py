from difflib import Differ

def get_file_content(file_path):
    lines = []
    with open(file_path, mode="r", encoding="utf8") as f:
        lines = f.read().splitlines()
    return lines 

text1 = get_file_content("f1.txt")
text2 = get_file_content("f2.txt")

d = Differ()
result = "\n".join(d.compare(text1, text2))
print(result)

