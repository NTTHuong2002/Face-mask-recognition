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
Figure 1: Phases and individual steps for building a COVID-19 face mask detector with computer vision and deep learning using Python, OpenCV, and TensorFlow/Keras.

In order to train a custom face mask detector, we need to break our project into two distinct phases, each with its own respective sub-steps (as shown by Figure 1 above):

Training: Here we’ll focus on loading our face mask detection dataset from disk, training a model (using Keras/TensorFlow) on this dataset, and then serializing the face mask detector to disk
Deployment: Once the face mask detector is trained, we can then move on to loading the mask detector, performing face detection, and then classifying each face as with_mask or without_mask
We’ll review each of these phases and associated subsets in detail in the remainder of this tutorial, but in the meantime, let’s take a look at the dataset we’ll be using to train our COVID-19 face mask detector.
