Project Overview
This project comprises three components, each targeting a unique problem in analyzing and predicting song attributes on Spotify:

Genre Prediction Notebook: Classifies songs into genres using audio features.
Popularity Prediction Notebook: Predicts the popularity of songs using regression models.
Music Recommendation System (Streamlit Application): A web-based app recommending similar tracks based on cosine similarity of audio features.
The project demonstrates end-to-end machine learning workflows and incorporates interactive elements for user engagement.

File Descriptions
1. spotify_finalproject_genreprediction.ipynb
Focus: Classifying songs into genres.
Approach:
Uses machine learning classification models like Logistic Regression, Random Forest, and SVM.
Dimensionality reduction with PCA.
Key Features:
Preprocessing pipelines for cleaning and scaling.
Model evaluation using accuracy scores.
Output: Classification accuracy for various models.
2. spotify_finalproject_popularityprediction.ipynb
Focus: Predicting song popularity scores.
Approach:
Employs regression models, including Linear Regression and Gradient Boosting.
Hyperparameter tuning with GridSearchCV.
Key Features:
Feature engineering to improve model predictions.
Mean Absolute Error (MAE) as the evaluation metric.
Output: Prediction accuracy and model performance metrics.
3. Music Recommendation System (Streamlit App)
Focus: Interactive music recommendation system.
Approach:
Calculates track similarity using cosine similarity.
Provides real-time recommendations based on selected tracks.
Features:
User-friendly interface built with Streamlit.
Dropdown search and dynamic track recommendations.
Output: A table displaying recommended tracks with their genre and artist details.
Data Overview
The dataset consists of Spotify audio features and metadata, such as:

Audio Features: Popularity, Danceability, Energy, Key, Tempo, and more.
Track Metadata: Track ID, Track Name, Artist Name, Album Name, Genre, and Duration.
Preprocessing Highlights:
Removed duplicates and handled missing values.
Engineered new features, such as track_avg_artist_popularity.
Normalized numerical features for optimal model performance.
Methodology
Genre and Popularity Prediction
Data Cleaning and Preprocessing:
Removed unnecessary columns, handled null values, and normalized features.
Feature Selection:
Dimensionality reduction for Genre Prediction.
Selecting features with high correlation to popularity.
Model Training:
Classification and regression models trained using cross-validation.
Evaluation:
Accuracy for Genre Prediction.
MAE for Popularity Prediction.
Recommendation System
Similarity Calculation:
Computed cosine similarity for numerical features to find similar tracks.
Interactive Application:
Designed a Streamlit app with a search-and-recommendation interface.
How to Run
Prerequisites
Python 3.7+
Libraries: numpy, pandas, matplotlib, seaborn, sklearn, streamlit, scipy.
Steps:
Clone the repository.
Install dependencies:
pip install -r requirements.txt
Run the Notebooks:
Open spotify_finalproject_genreprediction.ipynb or spotify_finalproject_popularityprediction.ipynb in Jupyter Notebook or JupyterLab.

Problem Statement:
The project addresses three key challenges in music data analysis:

Genre Classification: Predicting song genres from audio features.
Popularity Prediction: Estimating a song's popularity based on its attributes.
Personalized Recommendations: Providing users with song recommendations similar to their preferences.
Results and Insights
Genre Prediction:
Achieved competitive accuracy using Random Forest and SVM.
Popularity Prediction:
Gradient Boosting and Decision Tree models outperformed simpler regressors in terms of MAE.
Recommendation System:
Successfully identified and displayed similar tracks in real time using cosine similarity.
