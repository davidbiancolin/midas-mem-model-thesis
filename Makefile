PAPER = davidbiancolin-dissertation

all: paper

paper:
	pdflatex $(PAPER).tex </dev/null
	biber $(PAPER)
	pdflatex $(PAPER).tex </dev/null >/dev/null
	pdflatex $(PAPER).tex </dev/null >/dev/null
	pdflatex $(PAPER).tex </dev/null
	./run-shame.sh $(PAPER).log
	rm shame.png

clean:
	rm -f *.aux	*.log *.lof *.bcf *.run.xml *.toc *.lot *.bbl

.PHONY: clean

################################################################################
# PDF generation from Graffle
################################################################################
tex_files = $(wildcard tex/*.tex)

# From the tex, generate a makefrag with recipes for each pdf
graffle-figures.mk: $(tex_files)
	python gen-graffle-makefrag.py

-include graffle-figures.mk

graffle2pdf: $(graffle_figures) graffle-figures.mk
.PHONY:graffle2pdf
