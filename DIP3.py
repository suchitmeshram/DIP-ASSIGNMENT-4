#Task : Read the color image and display its reddish, greenish and bluish image

import imageio
image = imageio.imread('Rengoku.jpg')
image.shape

imageio.imwrite('red.jpg', image[:, :, 0])
imageio.imwrite('green.jpg', image[:, :, 1])
imageio.imwrite('blue.jpg', image[:, :, 2])

image[:, :, 1].shape

red_image = image.copy()
red_image[:, :, 1] = 0
red_image[:, :, 2] = 0

blue_image = image.copy()
blue_image[:, :, 0] = 0
blue_image[:, :, 1] = 0

green_image = image.copy()
green_image[:, :, 0] = 0
green_image[:, :, 2] = 0

imageio.imwrite('red_image.jpg', red_image)
imageio.imwrite('blue_image.jpg', blue_image)
imageio.imwrite('green_image.jpg', green_image)