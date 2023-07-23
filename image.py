from PIL import Image , ImageFilter

img = Image.open('./astro.jpg')
#filtered_img = img.filter(ImageFilter.BLUR)
#filtered_img.save("blur.png", 'png')
#filtered_img=img.convert('L')
#filtered_img.save("grey.png",'png')
#filtered_img.show()
#resize=filtered_img.resize((300,300))
#resize.save("grey.png",'png')
#thumbnail keeps the aspect ratio
img.thumbnail((400,400))
img.save('thumbnail.jpg')

