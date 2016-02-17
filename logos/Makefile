all: build/schwingung_negativ.pdf build/schwingung_positiv.pdf

texoptions = \
	     --output-directory=build \
	     --interaction=nonstopmode \
	     --halt-on-error

build/%.pdf: %.tex | build
	lualatex $(texoptions) $^

build:
	mkdir -p build

clean:
	rm -rf clean

