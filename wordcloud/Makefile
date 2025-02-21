all: build/logo_tasche_negativ_schwarz_weiss.png


build/wordcloud.png: ../logos/build/schwingung_positiv.png
build/wordcloud_negativ.png: specific_pep_words.txt words_of_physics.txt schwingung_negativ_high_res.png| build
	python pep_wordcloud.py

../logos/build/schwingung_positiv.png:
	make -C ../logos build/schwingung_positiv.png

build/logo_tasche_negativ_schwarz_weiss.png: build/wordcloud_negativ.png | build
	python pep_taschen.py


build:
	mkdir -p build

clean:
	rm -rf build

.PHONY: all clean
