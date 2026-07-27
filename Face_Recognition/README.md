# Face Recognition using CNN

A deep learning project that performs face recognition using a Convolutional Neural Network (CNN) trained on the **Labeled Faces in the Wild (LFW)** dataset. The project demonstrates facial image preprocessing, feature extraction, model training, and evaluation to recognize individuals from real-world face images captured under varying conditions.

## Dataset

**Dataset:** Labeled Faces in the Wild (LFW)

**Dataset Link:** https://vis-www.cs.umass.edu/lfw/

The LFW dataset contains face images collected from the web, featuring variations in pose, lighting, facial expressions, and backgrounds. It is widely used as a benchmark dataset for face recognition and facial verification tasks.

## Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Matplotlib
- Scikit-learn
- Seaborn

## Project Workflow

1. Load and preprocess the LFW dataset.
2. Resize and normalize facial images.
3. Build a Convolutional Neural Network (CNN).
4. Train the model to learn facial features.
5. Evaluate the model on unseen test images.
6. Generate predictions for face recognition.
7. Visualize model performance using accuracy and loss graphs.
8. Analyze predictions with a confusion matrix and classification report.

## CNN Architecture

The model consists of:

- Convolutional Layers
- Max Pooling Layers
- Flatten Layer
- Fully Connected Dense Layer
- Dropout Layer for regularization
- Softmax Output Layer for multi-class face classification

## Features

- Face image preprocessing
- CNN-based facial feature extraction
- Face recognition using deep learning
- Model training and evaluation
- Accuracy and loss visualization
- Confusion Matrix
- Classification Report
- Model saving and loading

## Results

The CNN model successfully learns discriminative facial features from the LFW dataset and accurately recognizes different individuals. The model demonstrates strong performance on unseen test images while maintaining good generalization across varying lighting conditions, facial expressions, and viewing angles.

## Repository Structure

```
Face-Recognition/
│
├── face_recognition.ipynb
├── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Face-Recognition.git
```

Install the required libraries:

```bash
pip install tensorflow numpy matplotlib seaborn scikit-learn
```

Run the Jupyter Notebook:

```bash
jupyter notebook face_recognition.ipynb
```

## Conclusion

This project demonstrates the application of Convolutional Neural Networks for face recognition using the LFW dataset. It provides practical experience in facial image preprocessing, deep learning-based feature extraction, model training, evaluation, and performance visualization, serving as a foundation for more advanced computer vision and biometric recognition systems.
