# Sree-Parvathy-P-Nair_AI-ML-Projects

A collection of Artificial Intelligence and Machine Learning projects developed using Python, TensorFlow, LangChain, FAISS, and Google Gemini. The repository demonstrates applications of deep learning, computer vision, and Retrieval-Augmented Generation (RAG) across different domains.

---

# Projects

## 1. AI PDF RAG Chatbot

**Technologies:** Python, LangChain, FAISS, Sentence Transformers, Google Gemini, Streamlit

A Retrieval-Augmented Generation (RAG) chatbot that answers questions from uploaded PDF documents. The system extracts text from PDFs, splits it into chunks, generates embeddings using Sentence Transformers, stores them in a FAISS vector database, retrieves the most relevant information through semantic search, and uses Google's Gemini model to generate accurate, context-aware responses.

**Key Features**
- PDF document loading and preprocessing
- Text chunking and embedding generation
- FAISS vector database
- Semantic similarity search
- Gemini-powered question answering
- Interactive Streamlit interface
- Chat history and source document retrieval

---

## 2. Breast Cancer Detection

**Dataset:** BreastMNIST

**Technologies:** Python, TensorFlow, Keras, MedMNIST

A Convolutional Neural Network (CNN) model developed to classify breast medical images as part of a computer-aided diagnosis system. The project focuses on medical image classification using deep learning techniques to distinguish between different image classes.

**Key Features**
- CNN-based medical image classification
- Data preprocessing and normalization
- Model training and evaluation
- Performance visualization using accuracy and loss graphs

---

## 3. Face Recognition

**Dataset:** Labeled Faces in the Wild (LFW)

**Technologies:** Python, TensorFlow, Keras

A CNN-based face recognition system that learns facial features from images and identifies individuals. The project demonstrates image preprocessing, feature extraction, and deep learning techniques for facial recognition.

**Key Features**
- Face image preprocessing
- CNN architecture for feature learning
- Model training and prediction
- Performance evaluation and visualization

---

## 4. Image Classification

**Dataset:** Fashion-MNIST

**Technologies:** Python, TensorFlow, Keras

A deep learning model designed to classify grayscale clothing images into one of ten Fashion-MNIST categories using Convolutional Neural Networks. The project demonstrates the complete workflow of image preprocessing, CNN model development, training, and evaluation.

**Key Features**
- Fashion-MNIST image classification
- CNN model implementation
- Training and validation
- Accuracy and loss analysis
- Prediction on test images

---

# Technologies Used

- Python
- TensorFlow
- Keras
- LangChain
- FAISS
- Sentence Transformers
- Google Gemini API
- Streamlit
- NumPy
- Matplotlib
- Scikit-learn
- MedMNIST

---

# Repository Structure

```
AI-ML-Projects/
│
├── README.md
├── requirements.txt
│
├── CHATBOT/
│   ├── app.py
│   ├── vector_store.py
│   ├── rag.py
│   ├── loader.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── similarity_search.py
│   ├── utils.py
│   ├── data/
│   ├── vectorstore/
│   └── results/
│
├── Breast-Cancer-Detection/
│   ├── breast_cancer_detection.ipynb
│   ├── README.md
│   └── screenshots/
│
├── Face-Recognition/
│   ├── face_recognition.ipynb
│   ├── README.md
│   └── screenshots/
│
└── Image-Classification/
    ├── image_classification.ipynb
    ├── README.md
    └── screenshots/
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/Sparvathy-23/Sree-Parvathy-P-Nair_CNN-Projects.git
```

Navigate to the repository:

```bash
cd Sparvathy-23
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

For the RAG Chatbot project, create a `.env` file inside the `CHATBOT` folder and add your Google Gemini API key:

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

---

# Repository Highlights

- Deep Learning using Convolutional Neural Networks
- Medical Image Classification
- Face Recognition
- Fashion Image Classification
- Retrieval-Augmented Generation (RAG)
- Semantic Search with FAISS
- Google Gemini LLM Integration
- Interactive Streamlit Web Application

---

# Author

**Sree Parvathy**

B.Tech Computer Science and Engineering (Artificial Intelligence & Machine Learning)
