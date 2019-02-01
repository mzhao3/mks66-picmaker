all:
	python picmaker.py
	convert image.ppm image.png
image:
	open image.png
