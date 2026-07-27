# Movie Recommendation System

## Overview

This project implements a **Content-Based Movie Recommendation System** using Machine Learning and Natural Language Processing (NLP). The system recommends movies similar to a user's favorite title by analyzing movie metadata such as genres, keywords, taglines, cast members, and directors. Recommendations are generated based on textual similarity rather than user ratings.

---

## Dataset

**Dataset:** Movies CSV Dataset

**Dataset Link:** https://www.kaggle.com/datasets/harshshinde8/movies-csv

The dataset contains information about thousands of movies, including their genres, cast, directors, keywords, and other descriptive metadata used for generating recommendations.

---

## Technologies Used

- Python
- Pandas
- Scikit-learn
- NumPy
- KaggleHub
- Difflib

---

## Project Workflow

### 1. Data Preprocessing

- Load the movie dataset.
- Handle missing values by replacing them with empty strings.
- Select important textual features such as genres, keywords, tagline, cast, and director.
- Combine selected features into a single text representation for each movie.

### 2. Feature Extraction

- Convert the combined text into numerical feature vectors using **TF-IDF Vectorization**.
- Represent each movie based on the importance of its descriptive words.

### 3. Model Development

- Train a **Nearest Neighbors (KNN)** model using cosine similarity.
- Store feature vectors for efficient similarity-based retrieval.

### 4. Recommendation Generation

- Accept a movie title from the user.
- Correct minor spelling mistakes using **Difflib**.
- Identify the closest matching movie.
- Retrieve and display the top similar movies based on cosine similarity.

---

## Features

- Content-based movie recommendation
- TF-IDF feature extraction
- Cosine similarity-based recommendations
- Typo-tolerant movie search
- Fast nearest-neighbor retrieval
- Personalized movie suggestions

---

## Results

The recommendation system successfully identifies movies with similar themes, genres, cast members, directors, and plot-related keywords. Given a movie title as input, the model returns a list of closely related movies, providing accurate and meaningful recommendations without requiring user ratings or viewing history.

---

## Repository Structure

```text
Movie-Recommendation-System/
│
├── movie_recommendation.ipynb
├── movies.csv
├── README.md
└── results/
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Movie-Recommendation-System.git
```

Install the required libraries:

```bash
pip install pandas numpy scikit-learn kagglehub
```

Run the Jupyter Notebook:

```bash
jupyter notebook movie_recommendation.ipynb
```

---

## Future Improvements

- Hybrid recommendation system combining content-based and collaborative filtering
- Deep learning-based recommendation models
- Interactive web application using Streamlit or Flask
- Personalized recommendations based on user preferences
- Integration with live movie databases and APIs

---

## Conclusion

This project demonstrates how Natural Language Processing and Machine Learning can be combined to build an effective content-based movie recommendation system. By leveraging TF-IDF vectorization and K-Nearest Neighbors with cosine similarity, the system generates relevant movie recommendations based solely on movie metadata, providing a strong foundation for more advanced recommender systems.
