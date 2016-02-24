TARGET = styleguide

texoptions = \
	     --lualatex \
	     --output-directory=build \
	     --interaction=nonstopmode \
	     --halt-on-error

all: build/$(TARGET).pdf


build/$(TARGET).pdf: FORCE | build
	latexmk $(texoptions) $(TARGET).tex

FORCE:

build:
	mkdir -p build

clean:
	rm -rf build

