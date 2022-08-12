import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator

# The text you would like to use in the wordcloud. In this example it is the simplest form - one word
text = "믕"

# opening the mask image. Find an image you would like to us and insert it here.
# I used a 1080 by 1080 heart image. Image needs to have a background.
mask = np.array(Image.open("[Insert PNG/JPEG Image name here without the brackets]"))

# word cloud appearance and generation
wc = WordCloud(background_color="white",
                repeat=True,
                mask=mask,
                font_path="NotoSansKR-Medium.otf",
                contour_width=3,
                contour_color="black",
                max_words=2000,
                random_state=1)
wc.generate(text)

# create the image colors from the colors in the mask
image_colors = ImageColorGenerator(mask)

# to display the wordcloud
plt.axis("off")
plt.imshow(wc.recolor(color_func=image_colors),  interpolation="bilinear")
plt.show()

# saveing image
wc.to_file("wc_heart.png")