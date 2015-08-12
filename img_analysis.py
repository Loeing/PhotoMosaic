from __future__ import print_function
from PIL import Image
import numpy

def downsample(image, width, height):
	downsized = image.resize((width, height), Image.ANTIALIAS)

def averageColor(image):
	colorTuple = [None, None, None]
	for channel in range(3):
		if image.mode != 'RBG':
			image = image.convert('RGB')
		pixels = image.getdata(band=channel)
		values = []
		for pixel in pixels:
			values.append(pixel)

		colorTuple[channel] = sum(values)/len(values)

	return tuple(colorTuple)

def cutMosaic(image, mWidth, mHeight):
	tiles = []
	for x in range(0,image.size[0]/mWidth):
		for y in range(0, image.size[1]/mHeight):
			box = (x,y,x+mWidth,y+mHeight)
			tile = image.crop(box)
			tiles.append(tile)

	return tiles

def run():
	image = Image.open("10star.jpg")
	mWidth = 10
	mHeight = 10
	tiles =  cutMosaic(image, mWidth, mHeight)
	for tile in tiles:
		print(averageColor(tile), tile.mode)
		r,g,b = tile.getpixel((1,1))
		print(r,g,b)
	print("done")
