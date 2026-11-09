.PHONY: all pdf

LATEX = pdflatex -interaction=nonstopmode -halt-on-error -output-directory=.build main.tex

# Resolve the bibliography first, then the auxiliary bibliography biblatex
# may generate. The final pass incorporates both into the PDF.
all: pdf

pdf:
	mkdir -p elaborato/.build/capitoli
	cd elaborato && $(LATEX)
	cd elaborato/.build && BIBINPUTS="../:$$BIBINPUTS" bibtex main
	cd elaborato && $(LATEX)
	cd elaborato/.build && BIBINPUTS="../:$$BIBINPUTS" bibtex main
	cd elaborato && $(LATEX)
	cd elaborato/.build && if test -f main1-blx.aux; then BIBINPUTS="../:$$BIBINPUTS" bibtex main1-blx; fi
	cd elaborato && $(LATEX)
	cd elaborato && $(LATEX)
	mv elaborato/.build/main.pdf elaborato/main.pdf
