import Image
import random
import numpy

def downsample(image, width, height):
	downsized = image.resize((width, height), Image.ANTIALIAS)

def averageColor(image):

	colorTuple = [None, None, None]
	for channel in range(3):
		pixels = image.getdata(band=channel)
		values = []
		for pixel in pixels:
			values.append(pixel)

		colorTuple[channel] = sum(values)/len(values)

	return tuple(colorTuple)