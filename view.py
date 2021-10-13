from pptx import Presentation
from pptx.util import Inches
from wand.image import Image
from wand.display import display

images = ['image1.jpg', 'image2.jpg', 'image3.jpg', 'image4.jpg', 'image5.jpg']
logo = 'nike_black.png'

# for i in range(0, len(images)):
    # display(Image(filename=images[i]).watermark(logo, 0.2, 50, 50))
image=Image(filename='image1.jpg')
    # with image.clone() as a:
    #     b=a.watermark(logo)
    #     b.save('new.jpg')

display(image)
# Import library from Image
# Import the image
for i in range(0,len(images)):
    with Image(filename =images[i]) as image:
        with Image(filename =logo) as water:
            water.resize(800,350)
            image.watermark(water, 0.2, 50, 50)
            a=image
            display(a)

