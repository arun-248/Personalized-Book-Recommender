# 📚 Personalized Book Recommender

<div align="center">

[![Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-FF4B4B?logo=streamlit&logoColor=white&style=for-the-badge)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white&style=for-the-badge)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/ML-scikit--learn-F7931E?logo=scikit-learn&logoColor=white&style=for-the-badge)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white&style=for-the-badge)](https://pandas.pydata.org/)

**🎯 An intelligent ML-powered book recommendation system using collaborative filtering**

</div>

---

## 🌟 Project Highlights

> **Personalized Reading Experience**: Leveraging collaborative filtering and the Book-Crossing dataset to provide tailored book suggestions based on user reading history and preferences, enhancing discovery of new literature.

**🎯 What makes this special:**
- **Dual recommendation approach** combining popularity-based and collaborative filtering
- **Interactive web application** with real-time suggestions
- **Comprehensive dataset integration** from Book-Crossing
- **User-friendly interface** with book cover displays
- **Scalable ML model** ready for deployment

---

## 🚀 Key Features

**🔮 Intelligent Recommendation Engine**
* Collaborative filtering for personalized suggestions
* Top 50 popularity-based recommendations on launch
* User-item interaction analysis
* Real-time book matching based on similar user preferences
* Five tailored recommendations per query

**📊 Interactive Dashboard**
* Clean, intuitive Streamlit interface
* Book search functionality with autocomplete
* Visual book cover displays
* Live recommendation updates
* User-friendly book selection

**🧠 Advanced ML Pipeline**
* Pre-trained collaborative filtering model
* User-based and item-based filtering
* Model serialization with Pickle for fast deployment
* Efficient similarity calculations
* Data preprocessing and normalization

**📖 Comprehensive Book Database**
* Book-Crossing dataset integration
* Book metadata including titles, authors, ISBNs
* User rating history (0-10 scale)
* Book cover image URLs
* Demographic user information

---

## 🖼️ Application Preview

<div align="center">

### 🏠 **Main Dashboard**
*Top 50 most popular books displayed on launch*

<img src="https://github.com/arun-248/Personalized-Book-Recommender/blob/main/Main_Dashboard%20(2).png" alt="Personalized Book Recommender" width="800"/>

### 📚 **Personalized Recommendations**
*Five tailored book suggestions based on user selection*
<img src="https://github.com/arun-248/Personalized-Book-Recommender/blob/main/Personalized_Recommendations.png" alt="Personalized Book Recommender" width="800"/>
</div>

---

## 📊 Dataset Description

### **Data Sources**
The project utilizes three core files from the Book-Crossing dataset:

| File | Description | Key Fields |
|------|-------------|------------|
| **Users.csv** | User demographic information | User-ID, Location, Age |
| **Books.csv** | Complete book inventory | ISBN, Book-Title, Book-Author, Image-URL-M |
| **Book-Ratings.csv** | User-book interaction data | User-ID, ISBN, Book-Rating (0-10) |

### **Data Integration**
By combining these files, we build a comprehensive view of user-book interactions, which forms the foundation for our collaborative filtering model. The system analyzes patterns across thousands of users and books to generate intelligent recommendations.

---

## 🔬 Recommender Systems Overview

### **The Importance of Recommender Systems**
Recommender systems are essential for modern applications, increasing user engagement and sales across platforms like **Netflix**, **Spotify**, and **Amazon**. By suggesting relevant content, they keep users satisfied and active.

### **Types of Recommender Systems**

**1. 📈 Popularity-Based**
* Recommends items based on overall popularity
* Example: YouTube's "Trending" section
* Used for initial display in our app

**2. 📝 Content-Based**
* Recommends items similar to those a user has liked
* Based on item attributes and features
* Analyzes content characteristics

**3. 🤝 Collaborative Filtering** *(Our Primary Method)*
* Leverages preferences of a large group of users
* **User-Based**: Finds similar users and recommends what they liked
* **Item-Based**: Finds similar items and recommends them
* Powers personalized recommendations in our app

**4. 🔄 Hybrid**
* Combines multiple techniques
* Improves accuracy and overcomes individual limitations
* Future enhancement opportunity

---

## 🎯 How the App Works

### **Step-by-Step User Journey**

**1. 🌟 Initial Display - Popularity-Based Recommendations**
* Upon launch, displays **top 50 most popular books**
* Based on number of explicit ratings
* Provides quick, general recommendations
* Showcases popularity-based recommender system

**2. 🔍 Getting Personalized Recommendations**
* User selects their favorite book from search box
* Autocomplete feature for easy book discovery
* Intuitive search interface

**3. 🤖 Collaborative Filtering in Action**
Once a user selects a book, the app's backend:
* Identifies other users who rated the same book highly
* Finds other books those "similar" users also rated highly
* Generates a list of **five personalized book recommendations**
* Matches user's taste based on collective wisdom

**4. 📚 Display Results**
* Shows recommended books with cover images
* Includes book titles and authors
* Instant results for seamless experience

---

## 🛠️ Technologies Used

### **Core Technologies**
- **Streamlit** – Interactive web application framework
- **Scikit-learn** – Machine learning model development
- **Pandas** – Data manipulation and analysis
- **NumPy** – High-performance numerical operations
- **Pickle** – Model serialization for quick deployment

### **Data Processing**
- Data cleaning and preprocessing
- Feature engineering for collaborative filtering
- User-item matrix construction
- Similarity calculations

### **Deployment**
- Streamlit Cloud integration
- Pre-trained model loading
- Fast inference pipeline

---



## 📈 Model Performance

### **Key Metrics**
* Trained on thousands of user-book interactions
* Utilizes Book-Crossing dataset with 200K+ ratings
* Fast recommendation generation (<1 second)
* High-quality suggestions based on collaborative patterns

### **Algorithm Details**
* **Method**: Collaborative Filtering (User-Based)
* **Similarity Metric**: Cosine Similarity
* **Data Processing**: Sparse matrix optimization
* **Model Format**: Serialized with Pickle for deployment

---

## 🚀 Future Enhancements

<details>
<summary><strong>🎯 Short-term Goals</strong></summary>

- [ ] Add content-based filtering for cold-start users
- [ ] Implement user rating feature
- [ ] Enhanced book search with filters
- [ ] Mobile-responsive design improvements
- [ ] Performance optimization for larger datasets

</details>

<details>
<summary><strong>🌟 Long-term Vision</strong></summary>

- [ ] **Hybrid Recommender System**: Combine collaborative and content-based filtering
- [ ] **Deep Learning Models**: Neural collaborative filtering
- [ ] **Real-time Updates**: Dynamic model retraining
- [ ] **User Profiles**: Save preferences and reading history
- [ ] **API Development**: Enable third-party integrations
- [ ] **Multi-language Support**: Expand to international books

</details>

---

## 🙏 Acknowledgments

- **Book-Crossing Community**: For providing the comprehensive dataset
- **Open Source Community**: For amazing tools and libraries
- **Streamlit Team**: For the fantastic deployment platform
- **scikit-learn**: For robust machine learning algorithms

---

## 🤝 Contributing

We welcome contributions! Feel free to:

### 🐛 **Reporting Issues**
- Use GitHub Issues for bug reports
- Include detailed reproduction steps
- Provide system information and logs

### 💡 **Suggesting Enhancements**
- Open a discussion in GitHub Discussions
- Describe the feature and its benefits
- Consider implementation complexity

---

<div align="center">

## 📄 License

This project is open source and available for educational purposes.

```
Feel free to use, modify, and distribute
Open source and ready for collaboration
```

**📚 Built with passion for reading | 🤖 Powered by Machine Learning**

*Made with ❤️ by [Arun Chinthalapally](https://github.com/arun-248)*

</div>
