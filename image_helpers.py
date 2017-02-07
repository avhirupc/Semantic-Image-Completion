import scipy.misc
import numpy as np
from PIL import Image
from glob import glob

# Helpers for image handling
def get_image(image_path, image_size, is_crop=True):
    return transform(imread(image_path), image_size, is_crop)

def save_images(images, image_path):
    for imgindex in range(images.shape[0]):
        scipy.misc.imsave(image_path+str(imgindex)+'.jpg',images[imgindex])

def imread(path):
    return scipy.misc.imread(path).astype(np.float)

def transform(image, npx=64, is_crop=True):
    # npx : # of pixels width/height of image
    if is_crop:
        cropped_image = center_crop(image, npx)
    else:
        cropped_image = image
    return np.array(cropped_image)/127.5 - 1.

def center_crop(x, crop_h, crop_w=None, resize_w=64): 
    if crop_w is None:
        crop_w = crop_h
    h, w = x.shape[:2]
    j = int(round((h - crop_h)/2.))
    i = int(round((w - crop_w)/2.))
    return scipy.misc.imresize(x[j:j+crop_h, i:i+crop_w], [resize_w, resize_w])

#def imsave(images, size, path):
 #   return scipy.misc.imsave(path, merge(images, size))

def inverse_transform(images):
    return (images+1.)/2.

def merge(images, size):
    h, w = images.shape[1], images.shape[2]
    img = np.zeros((h * size[0], w * size[1], 3))

    for idx, image in enumerate(images):
        i = idx % size[1]
        j = idx / size[1]
        img[j*h:j*h+h, i*w:i*w+w, :] = image

    return img


def convert_to_lower_resolution():
    images=glob(os.path.join('cars_train\cars_train/','*.jpg'))
    i=0
    size=108,108
    for image in images:

        im=Image.open(image)
        im_resized=im.resize(size,Image.ANTIALIAS)
        im_resized.save("cars_train/"+str(i)+'.jpg')

