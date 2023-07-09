# Face-mask-recognition
                                       👉 𝗙𝗮𝗰𝗲 𝗠𝗮𝘀𝗸 𝗗𝗲𝘁𝗲𝗰𝘁𝗼𝗿 𝘄𝗶𝘁𝗵 𝗢𝗽𝗲𝗻𝗖𝗩, 𝗞𝗲𝗿𝗮𝘀/𝗧𝗲𝗻𝘀𝗼𝗿𝗙𝗹𝗼𝘄, 𝗮𝗻𝗱 𝗗𝗲𝗲𝗽 𝗟𝗲𝗮𝗿𝗻𝗶𝗻𝗴 👈

In this tutorial, we’ll discuss how we can use computer vision in our two-phase face mask detector, detailing how our computer vision and deep learning pipeline will be implemented.

From there, we’ll review the dataset we’ll be using to train our custom face mask detector.

I’ll then show you how to implement a Python script to train a face mask detector on our dataset using Keras and TensorFlow.

We’ll use this Python script to train a face mask detector and review the results.

Given the trained face mask detector, we’ll proceed to implement two more additional Python scripts used to:

Detect  face masks in images
Detect face masks in real-time video streams

                                        📜 📃 📄Ｔｗｏ－ｐｈａｓｅ░ｆａｃｅ░ｍａｓｋ░ｄｅｔｅｃｔｏｒ 📜 📃 📄
<img width="382" alt="image" src="https://github.com/NTTHuong2002/Face-mask-recognition/assets/130816726/9b8f430c-a6ff-440f-9a6e-3c17e584b069">

░F░i░g░u░r░e░ ░1░:░ Phases and individual steps for building a COVID-19 face mask detector with computer vision and deep learning using Python, OpenCV, and TensorFlow/Keras.

In order to train a custom face mask detector, we need to break our project into two distinct phases, each with its own respective sub-steps (as shown by Figure 1 above):

1️⃣ Training: Here we’ll focus on loading our face mask detection dataset from disk, training a model (using Keras/TensorFlow) on this dataset, and then serializing the face mask detector to disk

2️⃣ Deployment: Once the face mask detector is trained, we can then move on to loading the mask detector, performing face detection, and then classifying each face as with_mask or without_mask

❌ We’ll review each of these phases and associated subsets in detail in the remainder of this tutorial, but in the meantime, let’s take a look at the dataset we’ll be using to train our COVID-19 face mask detector.

<img width="398" alt="image" src="https://github.com/NTTHuong2002/Face-mask-recognition/assets/130816726/d28927da-450e-4280-adce-7242a3fc4d74">

░F░i░g░u░r░e░ ░2░:░ COVID-19 face mask detector training accuracy/loss curves demonstrate high accuracy and little signs of overfitting on the data. We’re now ready to apply our knowledge of computer vision and deep learning using Python, OpenCV, and TensorFlow/Keras to perform face mask detection.

<img width="374" alt="image" src="https://github.com/NTTHuong2002/Face-mask-recognition/assets/130816726/45ef5dea-3145-4468-9791-73505667cc91">
<img width="354" alt="image" src="https://github.com/NTTHuong2002/Face-mask-recognition/assets/130816726/d230b142-a051-4469-92ed-77250dc32713">

                                                                🔔【﻿ＳU M M A R Y】🔔
In this tutorial, you learned how to create a COVID-19 face mask detector using OpenCV, Keras/TensorFlow, and Deep Learning.

To create our face mask detector, we trained a two-class model of people wearing masks and people not wearing masks.

We fine-tuned MobileNetV2 on our mask/no mask dataset and obtained a classifier that is ~99% accurate.

We then took this face mask classifier and applied it to both images and real-time video streams by:

1️⃣ Detecting faces in images/video
2️⃣ Extracting each individual face
3️⃣ Applying our face mask classifier

Our face mask detector is accurate, and since we used the MobileNetV2 architecture, it’s also computationally efficient, making it easier to deploy the model to embedded systems (Raspberry Pi, Google Coral, Nvidia, etc.).
