files := schwingung_positiv \
	schwingung_negativ \
	logo_positiv \
	logo_positiv_link \
	logo_positiv_white \
	logo_negativ \
	logo_negativ_link \
	t-shirt \
	tshirt_positiv \
	logo_datenbank

all: build/pep-logos.zip


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
	inkscape --pdf-poppler --export-dpi=600 --export-area-drawing $< -o $@

%.svg: %.pdf | build
	inkscape --pdf-poppler --export-text-to-path --export-plain-svg $< -o $@


build/pep-logos.zip: png svg pdf
	mkdir -p build/pep-logos
	cp build/*.svg build/*.png build/*.pdf build/pep-logos/
	cd build && zip -r pep-logos.zip pep-logos

FORCE:

build:
	mkdir -p build

clean:
	rm -rf build

