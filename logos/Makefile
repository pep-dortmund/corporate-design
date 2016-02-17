all: build/schwingung_negativ.pdf build/schwingung_positiv.pdf

texoptions = \
	     --lualatex \
	     --output-directory=build \
	     --interaction=nonstopmode \
	     --halt-on-error


build/schwingung_positiv.pdf: FORCE | build
	latexmk $(texoptions) schwingung_positiv.tex

build/schwingung_negativ.pdf: FORCE | build
	latexmk $(texoptions) schwingung_negativ.tex

FORCE:

build:
	mkdir -p build

clean:
	rm -rf clean

