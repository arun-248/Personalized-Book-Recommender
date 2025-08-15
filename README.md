# Personalized Book Recommender 📚

This project is a personalized book recommendation system built with Python, using the **Book-Crossing dataset**. The application uses **collaborative filtering** to provide tailored book suggestions based on a user's reading history and preferences.

---

### Dataset Description

The project utilizes three files from the Book-Crossing dataset:

* **`Users.csv`**: Holds user demographic information, identified by a unique **User-ID**.
* **`Books.csv`**: Our book inventory, with a unique **ISBN** for each book, plus details like **Book-Title**, **Book-Author**, and **Image-URL-M** for displaying book covers.
* **`Book-Ratings.csv`**: The core of the model, linking **User-ID** and **ISBN** with a corresponding **Book-Rating** (0-10).

By combining these files, we build a comprehensive view of user-book interactions, which is the foundation for our collaborative filtering model.

---

### The Importance of Recommender Systems

Recommender systems are essential for modern applications, increasing user engagement and sales across platforms like **Netflix**, **Spotify**, and **Amazon**. By suggesting relevant content, they keep users satisfied and active.

### Types of Recommender Systems

1.  **Popularity-Based**: Recommends items based on their overall popularity.
    * *Example:* YouTube's "Trending" section.
2.  **Content-Based**: Recommends items similar to those a user has liked before, based on item attributes.
3.  **Collaborative Filtering**: Recommends items by leveraging the preferences of a large group of users. This is the core method for this project.
    * **User-Based**: Finds similar users and recommends what they liked.
    * **Item-Based**: Finds similar items and recommends them.
4.  **Hybrid**: Combines multiple techniques to improve accuracy and overcome individual limitations.

---

### How the App Works: A Step-by-Step Guide

This Streamlit application is designed to be intuitive and powerful.

1.  **Initial Display - Popularity-Based Recommendations**:
    Upon launch, the app first displays the **top 50 most popular books**, based on the number of explicit ratings. This provides a quick, general recommendation and showcases a simple **popularity-based recommender system**.

2.  **Getting Personalized Recommendations**:
    The user is then prompted to select their favorite book from a search box. This is where the magic of personalization begins.

3.  **Collaborative Filtering in Action**:
    Once a user selects a book, the app's backend takes over. It uses the pre-trained model to:
    - Identify other users who rated the same book highly.
    - Find other books those "similar" users also rated highly.
    - Generate a list of **five personalized book recommendations** that are highly likely to match the user's taste.

This process is a live demonstration of a **collaborative filtering system**, where the app learns from the collective "wisdom of the crowd" to make intelligent, personalized suggestions.

---

### Technologies Used

- **Streamlit**: For building the interactive, easy-to-use web application.
- **Scikit-learn**: For developing the machine learning model.
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For high-performance numerical operations.
- **Pickle**: To save and load the trained model for quick deployment.

---

### Getting Started

To run the project locally, follow these steps:

1.  **Clone the Repository**:
    ```bash
    git clone <your-repo-link>
    cd <your-repo-name>
    ```

2.  **Install Dependencies**:
    ```bash
    pip install streamlit scikit-learn pandas numpy
    ```

3.  **Run the Application**:
    ```bash
    streamlit run app.py
    ```

This will launch the application in your browser, and you can start exploring your personalized book recommendations.
