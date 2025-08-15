# importing required libraries.
import streamlit as st
import pickle
import numpy as np
import pandas as pd 

st.set_page_config(layout="wide")

st.header("Book Recommender System")
st.markdown('''
            ##### This site has the book recomentation system where you can select a book from our catlog and it will suggest books accordingly. 
            ##### Based on our data we have the top 50 books based on the user feedback.
            ##### The Recomender system is based on Colloborative filtering. 
            ''')
# Importing models and dataframe. 
popular = pickle.load(open('popular.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
similarity_score = pickle.load(open('similarity_scores.pkl','rb'))
      
# Streamlit sidebar header
st.sidebar.title("Top 50 Books")

# Display books in a grid layout if the 'SHOW' button is clicked
if st.sidebar.button("SHOW"):
    cols_per_row = 5  # Number of columns per row

    # Calculate number of rows needed
    num_rows = (len(popular) + cols_per_row - 1) // cols_per_row

    # Loop through each row
    for row in range(num_rows):
        cols = st.columns(cols_per_row)  # Create columns for the current row
        
        # Loop through each column in the current row
        for col in range(cols_per_row):
            book_idx = row * cols_per_row + col
            
            if book_idx < len(popular):
                with cols[col]:
                    st.image(popular.iloc[book_idx]['Image-URL-M'])  # Display book cover image directly from DataFrame
                    st.text(popular.iloc[book_idx]['Book-Title'])  # Display book title
                    st.text(popular.iloc[book_idx]['Book-Author'])  # Display book author
                    st.text(f"Ratings: {popular.iloc[book_idx]['num_ratings']}")  # Display total ratings
                    st.text(f"Avg. Rating: {round(popular.iloc[book_idx]['avg_rating'], 2)}")  # Display average rating
  
# Code for recommender system :     

def recommend(book_name):
    # Fetch the index of the given book name in the pivot table (pt)
    index = np.where(pt.index == book_name)[0][0]

    # Get the similarity scores for the given book and sort them in descending order
    # We use enumerate to get the index and similarity score
    # We skip the first item ([1:5]) since it's the book itself (highest similarity score)
    similar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:6]

    # Initialize an empty list to store the data of similar books
    data = []
    for i in similar_items:
        item = []
        # Get the DataFrame rows for the book corresponding to the current index
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]

        # Add the book title to the item list, ensuring no duplicates
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        
        # Add the book author to the item list, ensuring no duplicates
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        
        # Uncomment the following line to add the book image URL to the item list, if needed
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        
        # Append the item (containing book title and author) to the data list
        data.append(item)
    
    # Return the list of similar books with their titles and authors
    return data

# this is the valus in our dropdown list. 
book_list = pt.index.values  # Extracting the index (assumed to be 'Book-Title') as a list of book titles
         
# Streamlit sidebar for recommending books
st.sidebar.title("Recommend Books")
selected_book = st.sidebar.selectbox("Type or select a book from the dropdown", book_list)  # Dropdown to select a book

if st.sidebar.button("Recommend Me"):  # Button to trigger recommendation
    book_recommended = recommend(selected_book)  # Get recommended books based on selected book
    
    # Display recommended books in 5 columns
    cols = st.columns(5)  # Create 5 columns using Streamlit
    
    # Loop through each column
    for col_idx in range(5):
        with cols[col_idx]:
            if col_idx < len(book_recommended):
                st.image(book_recommended[col_idx][2])  # Display book cover image
                st.text(book_recommended[col_idx][0])  # Display book title
                st.text(book_recommended[col_idx][1])  # Display book author

# Importing the data
books_df = pd.read_csv("Data/Books.csv")
ratings_df = pd.read_csv("Data/Ratings.csv")
users_df = pd.read_csv("Data/Users.csv")

# Streamlit header
st.sidebar.title("Data Used")

if st.sidebar.button("Show Data"): 
    st.subheader('This is the Books data we used in our model')
    st.dataframe(books_df)
    st.subheader('This is the Books Ratings data we used in our model')
    st.dataframe(ratings_df)
    st.subheader('This is the Users data we used in our model')
    st.dataframe(users_df)