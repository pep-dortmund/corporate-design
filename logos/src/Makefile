files := schwingung_positiv schwingung_negativ logo_positiv logo_negativ t-shirt

all: png svg pdf


pdf: $(addprefix build/, $(addsuffix .pdf, $(files)))
png: $(addprefix build/, $(addsuffix .png, $(files)))
svg: $(addprefix build/, $(addsuffix .svg, $(files)))


texoptions = \
	     --lualatex \
	     --output-directory=build \
	     --interaction=nonstopmode \
	     --halt-on-error


build/%.pdf: FORCE | build
	latexmk $(texoptions) $*.tex

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

