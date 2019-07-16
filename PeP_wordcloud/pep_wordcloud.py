import os
import numpy as np
from PIL import Image
from pathlib import Path
from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt


def read_png_img_as_jpg(img_path, invert=False):
    ''' Function to read in a png image and convert it into the RGB space.
        This is the same space used for jpg images, which do not have an
        alpha channel.
        :param img_path: Path to png image
        :param invert: Boolean to invert an image
        :return img_jpg: Return the converted image as numpy array
    '''
    img_png = Image.open(img_path)
    # Remove the alpha channel of the png image
    # Source:
    # https://stackoverflow.com/questions/9166400/convert-rgba-png-to-rgb-with-pil
    img_jpg = Image.new("RGB", img_png.size, (255, 255, 255))
    img_jpg.paste(img_png, mask=img_png.split()[3])

    img_jpg = np.array(img_jpg)
    if invert:
        img_jpg = np.invert(img_jpg)

    return img_jpg


def extend_list(list, min_multi, max_multi):
    ''' Function add multiples of a list element. The number of elements added
        is determinded by a random number in the range of [min_multi, max_multi]
        :param list: List to be extended.
        :param min_multi: Lower limit for an extentions factor of a list element
        :param max_multi: Upper limit for an extentions factor of a list element
        :return extended_list: Return extended input list
    '''
    extended_list = []
    for element in list:
        multiplier = int(np.random.uniform(min_multi, max_multi))
        extended_list += [element] * multiplier
    return extended_list


def higlight_pep(word, **kwargs):
        ''' Function to highlight the word "PeP" by changing the color
            :param word: Word of the cloud
        '''
        if word is not 'PeP':
            return "hsl(0, 0%, 0%)"
        else:
            return "hsl(209, 100%, 62%)"


path_to_dict = Path(os.path.abspath(__file__)).parents[0]

path_to_physics_words = os.path.join(path_to_dict, 'words_of_physics.txt')
pwords = np.loadtxt(path_to_physics_words,
                    comments="#",
                    delimiter=",",
                    unpack=False,
                    dtype=str)

path_to_specific_pep_words = os.path.join(path_to_dict, 'specific_pep_words.txt')
pepwords = np.loadtxt(path_to_specific_pep_words,
                      comments="#",
                      delimiter=",",
                      unpack=False,
                      dtype=str)

max_multi = 10
min_multi = 1
pwords = extend_list(pwords, min_multi, max_multi)
pepwords = extend_list(pepwords, min_multi, max_multi)

words = pwords + pepwords + ['PeP'] * 3 * max_multi
number_of_words = int(len(words))
# wordcloud requires a dict that contains the word with his frequency
words = dict(Counter(words))


path_to_logo = os.path.join(Path(os.path.abspath(__file__)).parents[2],
                            'corporate-design',
                            'logos',
                            'build',
                            'schwingung_positiv.png'
                            )
mask = read_png_img_as_jpg(path_to_logo, invert=True)


# Link to documentation
# https://amueller.github.io/word_cloud/generated/wordcloud.WordCloud.html
wc = WordCloud(mask=mask,
               mode="RGBA",
               width=1000,
               height=1000,
               repeat=False,
               min_font_size=4,
               max_font_size=None,
               contour_width=0,
               max_words=number_of_words,
               color_func=higlight_pep,
               contour_color='firebrick',
               background_color="rgba(255, 255, 255, 0)"
               )

wordcloud = wc.generate_from_frequencies(words)


plt.figure(figsize=(10, 10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

save_path = os.path.join(path_to_dict, 'pep_wordcloud.png')
plt.savefig(save_path)
