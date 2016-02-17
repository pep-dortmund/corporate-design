all: build/schwingung_negativ.pdf \
	build/schwingung_positiv.pdf \
	build/logo_negativ.pdf \
	build/logo_positiv.pdf \

texoptions = \
	     --lualatex \
	     --output-directory=build \
	     --interaction=nonstopmode \
	     --halt-on-error


build/schwingung_positiv.pdf: FORCE | build
	latexmk $(texoptions) schwingung_positiv.tex

build/schwingung_negativ.pdf: FORCE | build
	latexmk $(texoptions) schwingung_negativ.tex

build/logo_negativ.pdf: FORCE | build
	latexmk $(texoptions) logo_negativ.tex

build/logo_positiv.pdf: FORCE | build
	latexmk $(texoptions) logo_positiv.tex

FORCE:

build:
	mkdir -p build

clean:
	rm -rf clean

