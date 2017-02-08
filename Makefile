NAME = midas-mem-model-thesis

all: paper

paper:
	pdflatex $(NAME).tex
	pdflatex $(NAME).tex
	pdflatex $(NAME).tex

clean:
	rm -f *.aux	*.log *.lof *.bcf *.run.xml *.toc *.lot

.PHONY: clean
