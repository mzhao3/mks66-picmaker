all:
	python picmaker.py
image:
	convert image.ppm image.png
	open image.png
