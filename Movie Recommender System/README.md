# Movie Recommendation System

## Overview
This project is a **Movie Recommendation System** designed to provide personalized movie suggestions based on various recommendation techniques. It is inspired by the recommendation systems used by popular streaming services such as **Netflix** and **Amazon Prime**.

## Recommendation Types
The system includes three main types of recommendations:
1. **Content-Based Recommendation:** Recommends movies based on the content you enjoy (e.g., genres, keywords).
2. **Popularity-Based Recommendation:** Suggests movies that are widely popular around the world.
3. **Collaborative Filtering:** Uses the viewing patterns of groups (even if they are not personally connected) to offer recommendations, similar to recommendations you might see on a multi-user Netflix account.

## Flow Diagram
The overall process for the system is as follows:
1. **Data** → 2. **Preprocessing** → 3. **Model Building** → 4. **Website Interface** → 5. **Deployment**

## Data Structure
The dataset is structured as a DataFrame with three key columns:
- **movie_id:** Unique identifier for each movie.
- **title:** The title of the movie.
- **tags:** A collection of tags or keywords that describe the movie.

## Data Source
The dataset used in this project is available on Kaggle:
[TMDB Movie Metadata Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

## Data Vectorization & Feature Extraction
1. **Text Vectorization:**
   - All tags are combined using a bag-of-words model to convert textual data into numerical vectors.
   - For example, if "Action", "Future", "Sci-fi", etc., are common tags, each movie is represented by a vector such as:
     - *movie1:* [5, 3, 6, 4, ...]
     - *movie2:* [2, 4, 5, 7, ...]
2. **Preprocessing Techniques:**
   - **Stemming:** Reduces words to their root form (e.g., "replying" becomes "repli").
   - **Lemmatization:** Converts words into their base form (e.g., "replying" becomes "reply").
   - **Stop Words Removal:** Eliminates common words (e.g., "is", "of", "are", "the", etc.) that do not add significant meaning.

## Similarity Measurement
- The dataset contains **4806 movies**, which are converted into high-dimensional vectors (approximately 5000 dimensions).
- **Cosine Similarity** is used to determine the similarity between two movie vectors:
  - A smaller cosine angle indicates higher similarity.
  - **Note:** Euclidean distance is not efficient for high-dimensional data, hence cosine similarity is preferred.

## TMDB API Integration
- The project utilizes the **TMDB API** to fetch movie posters and additional metadata, enhancing the UI experience.
- Ensure that you have a valid TMDB API key and proper API setup in your application.

## Model Saving and Deployment
- **Model Serialization:** The trained recommendation model is saved as a pickle file using Python's `pickle` module.
- **Similarity Matrix:** The computed movie similarity matrix is also stored in a separate pickle file for efficient retrieval.
- **File Naming:** Pickle files are optimized and saved with concise file names for ease of access and minimal storage overhead.
- A **Streamlit** web application is developed to offer a user-friendly interface, making it easy to interact with the recommendation system.
- The system is deployed as a web service, ensuring seamless access for end-users.

## Video Demonstration
Check out the video demonstration of the project:
[Video Link](https://example.com/video-demo)  

## Conclusion
This Movie Recommendation System provides a full pipeline covering data preprocessing, feature extraction, similarity measurement, model building, and deployment through a web interface. It combines content-based, popularity-based, and collaborative filtering approaches to offer personalized movie suggestions. Enhancements, such as integration with the TMDB API for dynamic posters and optimized model storage, further enrich the user experience.
