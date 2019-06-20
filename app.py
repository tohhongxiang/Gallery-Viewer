from flask import Flask, render_template, url_for
import os
from random import shuffle

app = Flask(__name__)

image_dir = "static/images"
images = [image for image in os.listdir(image_dir) if image.split(".")[-1].lower() in ["jpg", "png", "jpeg", "bmp", "gif"]]
print(images)
len_images = len(images)
print(str(len(images)) + "images loaded")

@app.route("/")
@app.route("/carousel")
def carousel():
	shuffle(images)
	return render_template("pic_gallery.html", images=images, len_images=len_images)

@app.route("/list")
def list():
	shuffle(images)
	return render_template("list.html", images=images, len_images=len_images)

if __name__ == "__main__":
	app.run(debug=True)