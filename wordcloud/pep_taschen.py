import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image, font_manager
import os


WIDTH = 4000   # 1920
HEIGHT = WIDTH*1.1  # 1920


def px2inch(pixel, ppi=96):
    '''
    Transform a number of pixel to the size in inch

    param pixel:    The number of pixels
    param ppi:      The pixel per inch resolution
    return:         The size in inches
    '''
    return pixel / ppi


# Use Akkurat font
font_path = os.path.expanduser('~/.fonts/AkkBd_Office.otf')
pepfont=font_manager.FontProperties(fname=font_path)

# Import the wordcloud and logos
logo_neg = image.imread('schwingung_negativ_high_res.png')
#  logo_neg_grey = image.imread('schwingung_negativ_grey.png')
wordcloud_pos = image.imread(os.path.join('build', 'pep_wordcloud_positiv.png'))
wordcloud_neg = image.imread(os.path.join('build', 'pep_wordcloud_negativ.png'))


def two_color_logo(width, height, pep_logo, pep_wordcloud, color_address, filepath):
    '''
    Create a pep logo with the wordcloud and the web address

    param width:            Figure width in pixel
    param height:           Figure height in pixel
    param pep_logo:         Numpy array of the pep_logo image (see matplotlib.image)
    param pep_wordcloud:    Numpy array of the wordcloud image (see matplotlib.image)
    param color_address:    Color of the web address
    param filename:         Path to save the image
    '''
    plt.figure(figsize = (px2inch(width), px2inch(height)), facecolor = None)
    plt.imshow(pep_logo)
    plt.imshow(pep_wordcloud)
    axes = plt.gca()
    upper, lower = axes.get_ylim() # Logo size
    plt.text(0.5*upper, upper*1.1,
            'www.pep-dortmund.org',
            fontproperties=pepfont,
            verticalalignment='bottom',
            horizontalalignment='center',
            size=WIDTH/25,
            color=color_address)
    plt.ylim([upper*1.11, lower])
    plt.xlim([lower, upper])
    plt.axis("off")
    plt.tight_layout(pad=0, h_pad=0, w_pad=0)
    plt.savefig(filepath, transparent=True)
    plt.clf()

# PeP bag logo in black and white
two_color_logo(
        width=WIDTH,
        height=HEIGHT,
        pep_logo=logo_neg,
        pep_wordcloud=wordcloud_pos,
        color_address='black',
        filepath=os.path.join('build', 'logo_tasche_negativ_schwarz_weiss.png'),
        )

# PeP bag logo in grey and white
#  two_color_logo(
        #  width=WIDTH,
        #  height=HEIGHT,
        #  pep_logo=logo_neg_grey,
        #  pep_wordcloud=wordcloud_pos,
        #  color_address=(86/255, 86/255, 86/255, 1),
        #  filepath=os.path.join('build', 'logo_tasche_negativ_grau_weiss.png'),
        #  )
