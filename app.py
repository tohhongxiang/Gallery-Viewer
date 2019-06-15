from flask import Flask, render_template, url_for
import os
from random import shuffle

app = Flask(__name__)

image_dir = "static/images"
images = os.listdir(image_dir)
len_images = len(images)
print(str(len(images)) + "images loaded")

@app.route("/")
def home():
	shuffle(images)
	return render_template("index.html", images=images, len_images=len_images)

@app.route("/list")
def list():
	shuffle(images)
	return render_template("index.html", images=images, len_images=len_images)

if __name__ == "__main__":
	app.run(debug=True)