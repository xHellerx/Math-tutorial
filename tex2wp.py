import re

# Todo:
# corollary environment

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
                line = re.sub(r"\\end\{exercise\}", "", line)
                line = re.sub(r"\\end\{thm\}", "", line)
                line = re.sub(r"\\end\{proof\}", "$$\square$$", line)
                line = re.sub(r"\\end\{example\}", "", line)
                line = re.sub(r"\\end\{definition\}", "", line)
                line = re.sub(r"\\term\{(.+?)\}", "<i>\g<1></i>", line)

                line = re.sub(r"\\sstirling\{(.+?)\}\{(.+?)\}",
                              r"\\genfrac{\\{}{\\}}{0pt}{}{\1}{\2}",
                              line)
                
                oldlen = len(line)
                line = re.sub(r"\\begin\{exercise\}",
                              "\n<strong>Упражнение.</strong>", line)
                line = re.sub(r"\\begin\{thm\}",
                              "\n<strong>Теорема.</strong>", line)
                line = re.sub(r"\\begin\{proof\}",
                              "<strong>Доказательство.</strong>", line)
                line = re.sub(r"\\begin\{example\}",
                              "\n<strong>Пример.</strong>", line)
                line = re.sub(r"\\begin\{definition\}",
                              "\n<strong>Определение.</strong>", line)
                if oldlen != len(line):
                    line = line.rstrip()
                    line += " "
                dst.write(line)

