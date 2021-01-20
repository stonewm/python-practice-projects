from difflib import HtmlDiff

def get_file_content(file_path):
    lines = []
    with open(file_path, mode="r", encoding="utf8") as f:
        lines = f.read().splitlines()
    return lines 

def compare_file(file1, file2):
    lines1 = get_file_content(file1)
    lines2 = get_file_content(file2)

    # 找出差异输出到result(str)
    html_diff = HtmlDiff()
    result = html_diff.make_file(lines1, lines2)
    
    # 将差异写入html文件
    with open("comparison.html", "w", encoding="utf8") as f:
        f.write(result)
    
if __name__ == "__main__":
    compare_file("f1.txt", "f2.txt")

