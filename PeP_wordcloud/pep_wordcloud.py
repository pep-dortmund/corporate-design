import os
import numpy as np
from PIL import Image
from pathlib import Path
from wordcloud import WordCloud
from collections import Counter


WIDTH = 4000
HEIGHT = 4000


def read_img_resize(img_path, width, height, invert=False):
    '''
    Function to read in an image and convert it into the RGB space.

    :param img_path: Path to image
    :param invert: Boolean to invert an image
    :return img_jpg: Return the converted image as numpy array
    '''
    img = Image.open(img_path)
    # if image is already rgb, just return it
    if img.mode == 'RGB':
        return img

    # convert to RGB if not.
    # https://stackoverflow.com/questions/9166400/convert-rgba-png-to-rgb-with-pil
    img_rgb = Image.new("RGB", img.size, (255, 255, 255))
    img_rgb.paste(img, mask=img.split()[3])
    img_rgb = img_rgb.resize((WIDTH, HEIGHT), resample=Image.BICUBIC)
    img_rgb = np.array(img_rgb)

    if invert:
        img_rgb = np.invert(img_rgb)

    return img_rgb


def extend_list(list, min_multi, max_multi):
    '''
    Function add multiples of a list element. The number of elements added
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
    '''
    Function to highlight the word "PeP" by changing the color

    :param word: Word of the cloud
    '''
    if word != 'PeP':
        return "hsl(0, 0%, 0%)"
    else:
        return "hsl(209, 100%, 62%)"


path_to_dict = Path(os.path.abspath(__file__)).parents[0]

path_to_physics_words = os.path.join(path_to_dict, 'words_of_physics.txt')
with open(path_to_physics_words) as f:
    pwords = [line.strip() for line in f if not line.startswith('#')]

path_to_specific_pep_words = os.path.join(path_to_dict, 'specific_pep_words.txt')
with open(path_to_specific_pep_words) as f:
    pepwords = [line.strip() for line in f if not line.startswith('#')]

max_multi = 10
min_multi = 1
pwords = extend_list(pwords, min_multi, max_multi)
pepwords = extend_list(pepwords, min_multi, max_multi)

words = pwords + pepwords + ['PeP'] * 3 * max_multi
number_of_words = int(len(words))
# wordcloud requires a dict that contains the word with his frequency
words = dict(Counter(words))


path_to_logo = os.path.join(
    Path(os.path.abspath(__file__)).parents[2],
    'corporate-design',
    'logos',
    'build',
    'schwingung_positiv.png'
)
mask = read_img_resize(path_to_logo, width=WIDTH, height=HEIGHT, invert=True)


# Link to documentation
# https://amueller.github.io/word_cloud/generated/wordcloud.WordCloud.html
wc = WordCloud(
    font_path='/home/maxnoe/.local/share/fonts/AkkBd_Office.otf',
    mask=mask,
    mode="RGBA",
    width=WIDTH,
    height=HEIGHT,
    repeat=False,
    min_font_size=4,
    max_font_size=None,
    contour_width=0,
    max_words=number_of_words,
    color_func=higlight_pep,
    contour_color='firebrick',
    background_color="rgba(255, 255, 255, 0)"
)
print(wc.width, wc.height, wc.scale)

save_path = os.path.join(path_to_dict, 'pep_wordcloud.png')
word_cloud = wc.generate_from_frequencies(words)
print(word_cloud.width, word_cloud.height)
print(word_cloud.to_array().shape)
word_cloud.to_file(save_path)
