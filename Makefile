all:
	pdflatex book.tex

clean:
	rm -f book.aux book.log book.pdf book.toc
