all: build/wordcloud.png


build/wordcloud.png: ../logos/build/schwingung_positiv.png 
build/wordcloud.png: specific_pep_words.txt words_of_physics.txt | build
	python pep_wordcloud.py

../logos/build/schwingung_positiv.png:
	make -C ../logos build/schwingung_positiv.png

build:
	mkdir -p build

clean:
	rm -rf build

.PHONY: all clean
