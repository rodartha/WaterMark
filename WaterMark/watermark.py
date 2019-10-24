import os
from PIL import Image, ImageFont, ImageDraw

def watermark_image(filename, watermark, color, font_file="Roboto-Medium.ttf"):
	file_split = filename.split('.')
	if file_split[1] != 'jpg' and file_split[1] != 'png':
		raise("The file must be a jpg or png")

	output_file = file_split[0] + '_wm.' + file_split[1]
	img = Image.open(filename)
	width, height = img.size
	if width < (7.8 * len(watermark)) or height < 20:
		raise("This image is too small must be at least {}x20".format(7.8 * len(watermark)))
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype(font_file, 16)
	draw.text((width - (7.8 * len(watermark)),height - 20), watermark, color, font=font)
	img.save(output_file)

def watermark_image_f(filename, watermark, color, font):
	file_split = filename.split('.')
	if file_split[1] != 'jpg' and file_split[1] != 'png':
		raise("The file must be a jpg or png")

	output_file = file_split[0] + '_wm.' + file_split[1]
	img = Image.open(filename)
	width, height = img.size
	if width < 100 or height < 20:
		raise("This image is too small must be at least {}x20".format(7.8 * len(watermark)))
	draw = ImageDraw.Draw(img)
	draw.text((width - (7.8 * len(watermark)),height - 20), watermark, color, font=font)
	img.save(output_file)

def batch_watermark(folder, watermark, color, font_file="Roboto-Medium.ttf"):
	font = ImageFont.truetype(font_file, 16)
	prev_dir = os.getcwd()
	os.chdir(folder)
	for root, dirs, files in os.walk(os.getcwd()):
	    for file in files:
	        if file.endswith(".jpg") or file.endswith(".png"):
	        	watermark_image_f(file, watermark, color, font)
	os.chdir(prev_dir)
