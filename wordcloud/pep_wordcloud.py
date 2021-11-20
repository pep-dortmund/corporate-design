import os
import numpy as np
#  from PIL import Image
from matplotlib import image
from wordcloud import WordCloud
#  from collections import Counter


WIDTH = 4000
HEIGHT = 4000

np.random.seed(42)

# Not in use
def read_img_resize(img_path, width, height, invert=False):
    '''
    Function to read in an image and convert it into the RGB space.

    :param img_path: Path to image
    :param invert: Boolean to invert an image
    :return img_jpg: Return the converted image as numpy array
    '''
    img = Image.open(img_path)
    if img.mode != 'RGB':
        # convert to RGB if not.
        # https://stackoverflow.com/questions/9166400/convert-rgba-png-to-rgb-with-pil
        img_rgb = Image.new("RGB", img.size, (255, 255, 255))
        img_rgb.paste(img, mask=img.split()[3])
        img = img_rgb

    img = img.resize((WIDTH, HEIGHT), resample=Image.BICUBIC)
    img = np.array(img)

    if invert:
        img = np.invert(img)

    return img


# Not in use
def repeat_words(words, min_repeat, max_repeat):
    '''
    Function add multiples of a list element. The number of elements added
    is determinded by a random number in the range of [min_multi, max_multi]

    :param words: words to be repeated.
    :param min_repeat: minimum number of repitions
    :param max_repeat: maximum number of repitions
    :return: list with repeated words
    '''
    return np.repeat(
        words,
        np.random.randint(min_repeat, max_repeat + 1, len(words))
    ).tolist()


# Not in use
def higlight_pep(word, **kwargs):
    '''
    Function to highlight the word "PeP" by changing the color

    :param word: Word of the cloud
    '''
    if word != 'PeP':
        return "hsl(0, 0%, 0%)"
    else:
        return "hsl(209, 100%, 62%)"


with open('words_of_physics.txt') as f:
    pwords = f.read()

with open('specific_pep_words.txt') as f:
    pepwords = f.read()

words = pepwords + pepwords + pwords

#  path_to_logo = os.path.join('..', 'logos', 'build', 'schwingung_positiv.png')
#  mask = read_img_resize(path_to_logo, width=WIDTH, height=HEIGHT, invert=True)

# mask the wordcloud with the pep logo
alphaimg = image.imread('schwingung_negativ_high_res.png')[:, :, -1]
rimg = image.imread('schwingung_negativ_high_res.png')[:, :, 0]
mask = (alphaimg == 0.0) | (rimg == 1)
mask = 255 * mask.astype(int)

# Link to documentation
# https://amueller.github.io/word_cloud/generated/wordcloud.WordCloud.html
wc = WordCloud(
    font_path = 'AkkBd_Office.otf',
    background_color = "rgba(255, 255, 255, 0)",
    mode = "RGBA",
    random_state = 42,
    mask = mask,
    width = WIDTH,
    height = HEIGHT,
    max_words = 250,
    color_func = lambda *args,
    **kwargs: 'rgb(255, 255, 255)'
)

word_cloud = wc.generate(words)
# Invert wordcloud for black text
word_cloud.recolor(
        random_state=42,
        color_func=lambda *args,
        **kwargs : 'rgb(0, 0, 0)')

save_path = os.path.join('build/pep_wordcloud.png')
word_cloud.to_file(save_path)
