from logging import exception
from flask import Flask, config, render_template, request
import detect_mask_image_ngu
import os
import cv2
from flask_assets import Environment, Bundle

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static\\img"
app.config["RESULT_FOLDER"] = "static\\rs"
assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('styles/main.scss', filters='pyscss', output='all.css')
assets.register('scss_all', scss)


@app.route("/", methods=["GET", "POST"])
def HomePage():
    if request.method == "GET":
        return render_template("index.html")
    else:
        try:
            image = request.files["image"]
            if image:
                print(image.filename)
                imgpath = os.path.join(app.config["UPLOAD_FOLDER"], image.filename)
                image.save(imgpath)
                print(imgpath)
                d_image = detect_mask_image_ngu.Detect(imgpath)
                result = detect_mask_image_ngu.ResizeImg(d_image)
                outputpath = f'{app.config["RESULT_FOLDER"]}/{image.filename}'
                cv2.imwrite(outputpath, result)

            return render_template("index.html", msg="Found", img=outputpath)
        except Exception as e:
            print(e)
            return render_template("index.html", msg="NotFound")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)