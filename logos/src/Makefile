all: build/schwingung_negativ.pdf \
	build/schwingung_negativ.png \
	build/schwingung_negativ.svg \
	build/schwingung_positiv.pdf \
	build/schwingung_positiv.png \
	build/schwingung_positiv.svg \
	build/logo_negativ.pdf \
	build/logo_negativ.png \
	build/logo_negativ.svg \
	build/logo_positiv.pdf \
	build/logo_positiv.png \
	build/logo_positiv.svg \

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

publish: all
	cp build/*.{svg,pdf,png} ..


%.png: %.pdf | build
	pdftoppm -png -r 600 $^ > $@

%.svg: %.pdf | build
	inkscape --without-gui --export-plain-svg $@ $^


FORCE:

build:
	mkdir -p build

clean:
	rm -rf build

