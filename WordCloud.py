import matplotlib.pyplot as plt
import os.path
from scipy.misc import imread
from wordcloud import WordCloud
import json

working_path = os.path.dirname(__file__)

name = r'Frequency_list_of_all'

with open(os.path.join(working_path,r'data',name + r'.json'),encoding='utf-8') as f:
    fre_dict = json.loads(f.read())

#mask_image = imread(path.join(working_path, "depedencies\nba.png"))
wordcloud = WordCloud(
        width=800,
        height=600,
        scale=4,
        font_path=r'depedencies\simhei.ttf',
        background_color="White",
        #mask=mask_image,
        max_words=150
            ).generate_from_frequencies(fre_dict)
    # Display the generated image:
plt.imshow(wordcloud)
plt.axis("off")
wordcloud.to_file(os.path.join(working_path, name + '.png'))
plt.show()