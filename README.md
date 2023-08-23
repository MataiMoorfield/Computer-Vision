# Computer-Vision
Basic computer vision model with YOLO. 
Made by Matai Moorfield.

# What is Computer Vision?

Computer vision is the work of making sense out of visual, audio, or other data inputs for machines. So far with computer vision, we are able to recognise faces, read licence plates, find objects in a given image, summarise the content of a photo, and a lot more.

At first computer vision started quite manually, with researchers trying to come up with to detect certain patterns and images, but with the surge of deep learning, over the last decade, we now have models that can automatically learn these patterns just by looking at the examples.

> “Computer vision is a field of study which enables computers to replicate the human visual system. It’s a subset of artificial intelligence which collects information from digital images or videos and processes them to define the attributes. The entire process involves image acquiring, screening, analysing, identifying and extracting information. This extensive processing helps computers to understand any visual content and act on it accordingly. You can also take up a computer vision course for free to understand the basics under Artificial intelligence domain.” (M. Chatterjee, Nov. 2022)
> 

Computer vision is a branch of computer science that powers machines to see, recognise, and process images. It is a multi-disciplinary field, and is a subfield of artificial intelligence and machine learning. 


# How does Computer Vision Work?

<aside>
Computer vision primarily uses pattern recognition techniques to self-train and understand data.

</aside>
<br />


Computer vision algorithms are trained by using a lot of visual data. The model process these images and finds patterns. “For example, If we send a million pictures of vegetable images to a model to train, it will analyse them and create an Engine (Computer Vision Model) based on patterns that are similar to all vegetables. As a result, Our Model will be able to accurately detect whether a particular image is a Vegetables every time we send it.” (Dharmaraj, Mar. 2022).

> ”While machine learning algorithms were previously used for computer vision applications, now deep learning methods have evolved as a better solution for this domain. For instance, machine learning techniques require a humongous amount of data and active human monitoring in the initial phase monitoring to ensure that the results are as accurate as possible. Deep learning on the other hand, relies on neural networks, and uses examples for problem solving. It self-learns by using labeled data to recognise common patterns in the examples.” (M. Chatterjee, Nov. 2022)
>

# Computer Vision in Operation
This is the breakdown of this model using YOLO:
1. **Input Image:** The neural network takes an input image as its input. YOLO resizes the input image to a fixed size, often dividing it into a grid.
2. **Neural Network Architecture:** YOLO uses a convolutional neural network (CNN) architecture to process the input image. This CNN processes the entire image in a single forward pass and generates a set of bounding box predictions and class probabilities simultaneously.
3. **Grid and Anchor Boxes:** YOLO divides the input image into a grid of cells. Each cell is responsible for predicting objects that fall within its boundaries. Within each cell, YOLO predicts bounding boxes (usually multiple per cell) and assigns them to anchor boxes. Anchor boxes are predefined shapes that help the model predict a wide range of object shapes and sizes.
4. **Predictions:** For each anchor box in each cell, YOLO predicts:
    - The coordinates of the bounding box relative to the cell's location.
    - The confidence score, indicating how likely the predicted box contains an object.
    - The class probabilities for each class label. This is often represented as a softmax output, where each class gets a probability score.
5. **Non-Maximum Suppression:** After predictions are made, YOLO applies non-maximum suppression to eliminate duplicate or highly overlapping bounding box predictions. This step ensures that only the most confident and non-overlapping predictions are kept.
6. **Output:** The final output of the neural network is a list of bounding box predictions along with their class probabilities. These predictions are generated for all cells in the grid.
7. **Post-Processing and Visualisation:** The bounding box predictions and class probabilities are then used to draw bounding boxes around detected objects on the input image. The class label associated with each box is determined based on the highest class probability.
8. **Thresholding:** YOLO often applies a confidence threshold to the predicted bounding boxes to filter out low-confidence detections. This helps reduce false positives in the final results.
9. **Usage:** The processed image with bounding boxes and class labels is then used for various applications, such as object detection in autonomous vehicles, surveillance systems, robotics, and more.


![Project Screenshot](https://i.ibb.co/gZtHNbg/Screen-Shot-2023-08-20-at-7-17-54-PM.png)
![Project Screenshot](https://i.ibb.co/0cL6x5G/Screen-Shot-2023-08-20-at-7-17-25-PM.png)

