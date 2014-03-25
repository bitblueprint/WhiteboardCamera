from django.shortcuts import render,redirect
from django.http import HttpResponse
from PIL import Image
from StringIO import StringIO
import ImageFilter
import random, math

'''
def is_point_inside(p, im):
	return p[0] >= 0 and p[1] >= 0 and p[0] < im.size[0] and p[1] < im.size[1]

def getgray(rgb):
	return (rgb[0] + rgb[1] + rgb[2]) / 3.0

def explode(im, origin, particles = 100):
	impacts = []
	im_edges = im.filter(ImageFilter.FIND_EDGES)
	im_edges.show()
	#im_edges = im_edges.filter(ImageFilter.MedianFilter())
	#im_edges.show()
	im.putpixel(origin, (255, 0, 0)) # debug
	for i in range(particles):
		p = origin
		angle = random.uniform(0, 2*math.pi)
		direction = (math.cos(angle), math.sin(angle))
		length = 0.0
		trace = []
		max_diff = 0.0
		# Keep within the bounds.
		while is_point_inside(p, im):
			last_value = getgray(im_edges.getpixel(p))
			# Next ..
			length += 1.0
			offset = (direction[0]*length, direction[1]*length)
			p = (int(round(origin[0] + offset[0])), int(round(origin[1] + offset[1])))
			if is_point_inside(p, im):
				grayness = getgray(im_edges.getpixel(p))
				diff = math.fabs(last_value - grayness)
				if diff > max_diff:
					max_diff = diff
				trace.append( (p, length, grayness, diff) )
			else:
				break
		# Now the max_diff is known.
		for (p, length, grayness, diff) in trace:
			diff = diff / max_diff # Normalize
			im.putpixel(p, (0, 255, 0)) # debug
			if diff > 0.08:
				break
			#print length, diff
	return impacts
'''

def get_board():
	filename = "temp6.jpg"
	return Image.open(filename)

def original_board(request):
	im = get_board()
	# Save and return
	out = StringIO()
	im.save(out, 'PNG')
	return HttpResponse(out.getvalue(), content_type="image/png")

def default_board(request):
	default_bounds = (957, 880, 904, 1609, 1668, 1641, 1669, 903)
	return redirect('board', size=500, bounds=",".join(map(str, default_bounds)) )

# Create your views here.
def board(request, size, bounds):
	im = get_board()
	bounds = map(int, bounds.split(","))
	size = int(size)
	if len(bounds) == 8:
		whiteboard = im.transform( (size, size), Image.QUAD, bounds, Image.BICUBIC)
		# Save and return
		out = StringIO()
		whiteboard.save(out, 'PNG')
		return HttpResponse(out.getvalue(), content_type="image/png")