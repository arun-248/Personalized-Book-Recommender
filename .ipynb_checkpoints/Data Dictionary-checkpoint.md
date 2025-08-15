# Content

- **The Book-Crossing dataset comprises 3 files.**

**Users:**

Contains the users. Note that user IDs (User-ID) have been anonymized and map to integers. Demographic data is provided (Location, Age) if available. Otherwise, these fields contain NULL-values. 

- User ID : Used to Identify User an anonymized number
- Location : Location of the User
- Age : Age of the User

**Books:**

Books are identified by their respective ISBN. Invalid ISBNs have already been removed from the dataset. Moreover, some content-based information is given (Book-Title, Book-Author, Year-Of-Publication, Publisher), obtained from Amazon Web Services. Note that in case of several authors, only the first is provided. URLs linking to cover images are also given, appearing in three different flavours (Image-URL-S, Image-URL-M, Image-URL-L), i.e., small, medium, large. These URLs point to the Amazon web site.

- ISBN : Unique Number to Identify the Book 
- Book-Title : Book title 
- Book-Author : Author of the Book
- Year-Of-Publication : The year when the book was published
- Publisher : Name of the publisher who published the book
- Image-URL-S : Amazon Image URL for the book in small size 
- Image-URL-M : Amazon Image URL for the book in medium size
- Image-URL-L : Amazon Image URL for the book in large size

**Ratings:**

Contains the book rating information. Ratings (Book-Rating) are either explicit, expressed on a scale from 1-10 (higher values denoting higher appreciation), or implicit, expressed by 0. 

- User-ID : 
- ISBN : 
- Book-Rating : Rating given by the user for a book. 

---