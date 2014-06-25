from PIL import Image
import StringIO

# resize image to keep aspect ratio and fit within the constraints of maxwidth and maxheight
def upload_original_image(f, name, maxwidth, maxheight, blob_service, container_name):
	
	im = Image.open(f)
	width = im.size[0]
	height = im.size[1]

	# resize original if necessary
	new_size = width, height
	if height > maxheight or width > maxwidth:
		ratio = min(maxwidth/width, maxheight/height)
		new_size = int(width*ratio), int(height*ratio)
	  im.thumbnail(new_size, Image.ANTIALIAS)
	buf = StringIO.StringIO()
	im.save(buf, 'PNG', quality=90, optimize=True)
	content = buf.getvalue()
	# upload buffer to blob
	blob_service.put_blob(container_name, name, content, x_ms_blob_type='BlockBlob')
	buf.close()

	return True

# create square thumbnail image centered in middle of image, resize to thumb_width by thumb_height
def create_thumbnail(f, thumb_name, thumb_size, blob_service, container_name):

	im = Image.open(f)
	width = im.size[0]
	height = im.size[1]

	if width > height:
		left_crop = int((width - height)//2)
		right_crop = int((width + height)//2)
		cropped = im.crop((left_crop, 0, right_crop, height))
	else:
		upper_crop = int((height - width)//2)
		lower_crop = int((height + width)//2)
		cropped = im.crop((0, upper_crop, width, lower_crop))

	std_size = thumb_size, thumb_size
	cropped.thumbnail(std_size, Image.ANTIALIAS)
	# create buffer
	buf = StringIO.StringIO()
	# save image to buffer
	cropped.save(buf, 'PNG', quality=90, optimize=True)
	# get buffer value
	content = buf.getvalue()
	# upload buffer to blob
	blob_service.put_blob(container_name, thumb_name, content, x_ms_blob_type='BlockBlob')
	# clear the buffer
	buf.close()

	return True
