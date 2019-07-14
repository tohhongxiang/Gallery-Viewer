from flask import Flask, render_template, url_for, request, redirect
from urllib.parse import unquote
import os
from random import shuffle

app = Flask(__name__)

image_dir = "static/images"
images = [image for image in os.listdir(image_dir) if image.split(".")[-1].lower() in ["jpg", "png", "jpeg", "bmp", "gif"]]

album_dir = "static/albums"
albums = os.listdir(album_dir)
album_dict = {}
for album in albums:
	album_dict[album] = [os.path.join(album_dir, album, image) for image in os.listdir(os.path.join(album_dir, album))]
	#album_dict[album] = os.listdir(os.path.join(album_dir, album))

album_pics = list(album_dict.values())
album_titles = list(album_dict.keys())

print(str(len(images)) + " images loaded")
print(str(len(albums)) + " albums loaded")

######## ROUTES ###########
@app.route("/")
def index():
	return redirect(url_for("carousel"))

@app.route("/carousel")
def carousel():
	shuffle(images)
	return render_template("carousel.html", images=images)

@app.route("/list")
def list():
	shuffle(images)
	return render_template("list.html", images=images)

@app.route("/albums")
def albums():
	return render_template("albums.html", album_pics=album_pics, album_titles=album_titles)

@app.route("/albums/<album>")
def view_album(album):
	album = unquote(album) # to remove those %20 formatting since urls cannot have spaces/etc.
	current_album_path = os.path.join(album_dir, album)
	current_album_pics = os.listdir(current_album_path)
	return render_template("album_viewer.html", current_album_pics=current_album_pics, current_album_title=album)


if __name__ == "__main__":
	app.run(debug=True)