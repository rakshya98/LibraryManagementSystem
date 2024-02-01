Setup Instructions 
1.	Clone the repository.
git clone https://github.com/rakshya98/LibraryManagementSystem.git

2.	Navigate to the project directory.
cd LibraryManagementSystem

3.	Create a virtual environment(optional but recommended):
python -m venv venv

4.	Activate the virtual environment
cd venv
cd Scripts
activate

5.	Navigate back to the project directory.

6.	Install the required dependencies.
pip install -r requirements.txt

7.	Apply database migrations:
python manage.py migrate

8.	Run the server:
python manage.py runserver

9.	Access the API at http://127.0.0.1:8000/



API Documentation
1.	User APIs

a.	Create a New User:
Endpoint: http://127.0.0.1:8000/api/users/create/
Method: POST
Request Body: 
{
“Name”: “Emma Watson”,
“Email”:emma@gmail.com,
“MembershipDate”:”2020-12-11”
}


b.	List all users:
Endpoint: http://127.0.0.1:8000/api/users/list/
Method: GET


c.	Get User by ID:
Endpoint: http://127.0.0.1:8000/api/users/1/
Method: GET


2.	Book APIs
a.	Add a New Book: 
Endpoint: http://127.0.0.1:8000/api/books/add/
Method: POST
Request Body:
{
    "Title": 
        "Ramayana",
    "ISBN": 
        "11113A,
    "PublishedDate": 
        "1998-01-10,
    "Genre": 
        "Religion"
}

b.	List All Books:
Endpoint: http://127.0.0.1:8000/api/books/list/
Method: GET

c.	Get Book by ID:
Endpoint: http://127.0.0.1:8000/api/books/1/
Method: GET

d.	Get All Book Details:
Endpoint: http://127.0.0.1:8000/api/books/details/
Method: GET

e.	Assign or Update Book Details
Endpoint: http://127.0.0.1:8000/api/books/1/details/
Method: POST, PATCH


3.	BorrowedBooksAPIs
a.	Borrow a Book:
Endpoint: http://127.0.0.1:8000/api/borrow/
Method: POST
Request Body: 
  {
        "UserID": 1,
        "BookID": 1,
        "BorrowDate": "2024-02-01",
        "ReturnDate": null
    }

b.	Return a book:
Endpoint:  http://127.0.0.1:8000/api/return/1/
Method: PATCH
Request Body:
  {
        "UserID": 1,
        "BookID": 1,
        "BorrowDate": "2024-02-01",
        "ReturnDate": “2024-02-02”
    }
c.	List All Borrowed Books:
Endpoint: http://127.0.0.1:8000/api/list/borrowed/
Method:GET










