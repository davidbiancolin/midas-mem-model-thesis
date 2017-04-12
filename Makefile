PAPER = midas-mem-model-thesis

all: paper

paper:
	pdflatex $(PAPER).tex </dev/null
	biber $(PAPER)
	pdflatex $(PAPER).tex </dev/null >/dev/null
	pdflatex $(PAPER).tex </dev/null >/dev/null
	pdflatex $(PAPER).tex </dev/null

clean:
	rm -f *.aux	*.log *.lof *.bcf *.run.xml *.toc *.lot

.PHONY: clean
