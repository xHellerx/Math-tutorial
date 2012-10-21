#!/usr/bin/python

import re

f = open("raw.tex")
content = f.read()

content = re.sub(r"\$latex ", "$", content)
content = re.sub(r"&amp;", "&", content)
content = re.sub(r"\$\\blacksquare\$", r"\\qed", content)
content = re.sub(r"<em>(.*?)</em>", r"{\\slshape \1}", content)
content = re.sub(r"<strong>(.*?)</strong>", r"{\\bfseries \1}", content)

newfile = open("result.tex", "w")
newfile.write(content)
