from flask import Flask, render_template, url_for
import os
from random import shuffle

app = Flask(__name__)

image_dir = "static/images"
images = os.listdir(image_dir)
images_without_ext = [image.split(".")[0] for image in images]
len_images = len(images)
print(str(len(images)) + "images loaded")

@app.route("/")
@app.route("/carousel")
def carousel():
	shuffle(images)
	return render_template("pic_gallery.html", images=images, len_images=len_images, title="Carousel")

@app.route("/list")
def list():
	shuffle(images)
	return render_template("list.html", images=images, len_images=len_images, images_without_ext=images_without_ext, title="List")

if __name__ == "__main__":
	app.run(debug=True)
