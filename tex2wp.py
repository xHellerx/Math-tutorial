import re

def convert(filename):
    with open(filename, encoding="utf-8") as src:
        with open("out.txt", "w") as dst:
            for line in src:
                line = re.sub(r"~", "&nbsp;", line)
                line = re.sub(r"---", "&mdash;", line)
                line = re.sub(r"\$", "$$", line)
                line = re.sub(r"\${2,}", "$$", line)
                line = re.sub(r"<<", "&laquo;", line)
                line = re.sub(r">>", "&raquo;", line)
                line = re.sub(r"\\S", "&sect;", line)
                line = re.sub(r"\\begin\{exercise\}",
                              "<strong>Упражнение</strong>", line)
                line = re.sub(r"\\end\{exercise\}", "", line)
                dst.write(line)

