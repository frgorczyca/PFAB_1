from PIL import Image

im = Image.open("ascii-pineapple.jpg")

arr = im.load()
print(arr[44,44])
