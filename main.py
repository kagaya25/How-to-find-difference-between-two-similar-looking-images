from PIL import Image ,ImageChops
img1=Image.open("1test.jpg")
img2=Image.open("2test.jpg")
diff=ImageChops.difference(img1,img2)
if diff.getbbox():
	diff.show()