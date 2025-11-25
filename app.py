from flask import Flask, render_template, request, redirect, url_for, make_response


# instantiate the app
app = Flask(__name__)
categories = [
    {"id":1, "name": "Biographies"},
    {"id":2, "name": "Psychology"},
    {"id":3, "name": "Politics"},
    {"id":4, "name": "History"}
]

books =[
    {
        "id":1,
        "categoryId":1,
        "title": "Petty: The Biography",
        "author": "Warren Zanes",
        "isbn": "13-9780304936588",
        "price": 10.00,
        "image": "new petty.gif"
        "readNow":0
    },
    {
        "id":2,
        "categoryId":1,
        "title": "Paul: The Biography",
        "author": "N.T.Wright",
        "isbn": "13-9780312287863",
        "price": 100.00,
        "image": "paul.gif"
        "readNow":1
    },
    {
        "id":3,
        "categoryId":1,
        "title": "Jerusalem: The Biography",
        "author": "Simon Sebag Montefiore",
        "isbn": "13-9780767925365",
        "price": 112.00,
        "image": "jerusalem.gif"
        "readNow":1
    },
    {
        "id":4,
        "categoryId":1,
        "title": "Anna: The Biography",
        "author": "Amy Odell",
        "isbn": "13-9780303608037",
        "price": 99.00,
        "image": "anaa.gif"
        "readNow":0
    },
    


    {
        "id":5,
        "categoryId":2,
        "title": "The Let Them Theory: A Life-Changing Tool That Millions of People Can't Stop Talking About",
        "author": "Mel Robbins, Sawyer Robbins",
        "isbn": "13-9780634069321",
        "price": 199.00,
        "image": "The Let Them Theory A Life-Changing Tool That Millions of People Can't Stop Talking About.gif"
        "readNow":1
    },
    {
        "id":6,
        "categoryId":2,
        "title": "The Anxious Generation: How the Great Rewiring of Childhood Is Causing an Epidemic of Mental Illness",
        "author": "Jonathan Haidt",
        "isbn": "13-9780571538163",
        "price": 2000.00,
        "image": "The Anxious Generation How the Great Rewiring of Childhood Is Causing an Epidemic of Mental Illness.gif"
        "readNow":0
    },
    {
        "id":7,
        "categoryId":2,
        "title": "Don't Believe Everything You Think (Expanded Edition): Why Your Thinking Is The Beginning & End Of Suffering",
        "author": "Joseph Nguyen",
        "isbn": "13-9781423481780",
        "price": 2000.00,
        "image": "Don't Believe Everything You Think (Expanded Edition) Why Your Thinking Is The Beginning & End Of Suffering.gif"
        "readNow":0
    },
    {
        "id":8,
        "categoryId":2,
        "title": "The Body Keeps the Score: Brain, Mind, and Body in the Healing of Trauma",
        "author": "Bessel Van Der Kolk",
        "isbn": "13-9780634069329",
        "price": 1999.00,
        "image": "The Body Keeps the Score Brain, Mind, and Body in the Healing of Trauma.gif"
        "readNow":0
    },

    {
        "id":9,
        "categoryId":3,
        "title": "The U.S. Constitution: A Reader",
        "author": "Hillsdale College Politics Faculty",
        "isbn": "13-9781423492724",
        "price": 999.99,
        "image": "The U.S. Constitution A Reader.gif"
        "readNow":1
    },
    {
        "id":10,
        "categoryId":3,
        "title": "Politics",
        "author": "Aristotle",
        "isbn": "13-9780131832020",
        "price": 62.88,
        "image": "Politics.gif"
        "readNow":0
    },
    {
        "id":11,
        "categoryId":3,
        "title": "The Boy Who Cried Race: The White Guilt Messiah Complex, Democrats And Black Victims",
        "author": "Unpopular Politics",
        "isbn": "13-9780131832021",
        "price": 77.77,
        "image": "The Boy Who Cried Race The White Guilt Messiah Complex, Democrats And Black Victims.gif"
        "readNow":1
    },
    {
        "id":12,
        "categoryId":3,
        "title": "How Fascism Works: The Politics of Us and Them",
        "author": "Jason Stanley",
        "isbn": "13-9780634086786",
        "price": 15.99,
        "image": "How Fascism Works The Politics of Us and Them.gif"
        "readNow":1
    },

        {
        "id":13,
        "categoryId":4,
        "title": "The Secret History",
        "author": "Donna Tartt",
        "isbn": "13-9780793512737",
        "price": 17.99,
        "image": "The Secret History.gif"
        "readNow":1
    },
    {
        "id":14,
        "categoryId":4,
        "title": "American History for Kids: A Captivating Guide to Major Events in US History",
        "author": "Captivating History",
        "isbn": "13-9780634069321",
        "price": 18.99,
        "image": "American History for Kids A Captivating Guide to Major Events in US History.gif"
        "readNow":1
    },
    {
        "id":15,
        "categoryId":4,
        "title": "The Histories",
        "author": "Herodotus",
        "isbn": "13-9780793512598",
        "price": 20.00,
        "image": "The Histories.gif"
        "readNow":1
    },
    {
        "id": 16,
        "categoryId": 4,
        "title": "The Creation of the American Republic, 1776-1787",
        "author": "Gordon S. Wood",
        "isbn": "13-9780634012327",
        "price": 29.99,
        "image": "The Creation of the American Republic, 1776-1787.gif",
        "readNow": 1
    }
]
# Create a list called categories. The elements in the list should be lists that contain the following information in this order:
#   categoryId
#   categoryName
#   An example of a single category list is: [1, "Biographies"]

# Create a list called books. The elements in the list should be lists that contain the following information in this order:
#   bookId     (you can assign the bookId - preferably a number from 1-16)
#   categoryId (this should be one of the categories in the category dictionary)
#   title
#   author
#   isbn
#   price      (the value should be a float)
#   image      (this is the filename of the book image.  If all the images, have the same extension, you can omit the extension)
#   readNow    (This should be either 1 or 0.  For each category, some of the books (but not all) should have this set to 1.
#   An example of a single category list is: [1, 1, "Madonna", "Andrew Morton", "13-9780312287863", 39.99, "madonna.png", 1]

#books = [
    # Biographies
#   [1, 1, "Beethoven", "David Jacobs", "13-9780304936588", 9.99, "beethoven.gif", 0],
#   [2, 1, "Madonna", "Andrew Morton", "13-9780312287863", 12.99, "madonna.jpg", 1],
#   [3, 1, "Clapton: The Autobiography", "Eric Clapton", "13-9780767925365", 10.99, "clapton.jpg", 1],
#   [4, 1, "Music is My Mistress", "Edward Kennedy Ellington", "13-9780303608037", 68.99, "ellington.jpg", 0],

    # Learn to Play placeholders
#   [5, 2, "Play Piano Today!", "Hal Leonard", "13-9780634069321", 19.99, "piano.jpg", 1],
#   [6, 2, "Guitar Basics", "James Longworth", "13-9780571538163", 14.99, "guitar.jpg", 0],

    # Music Theory placeholders
#   [7, 3, "Music Theory Essentials", "Jason W. Solomon", "13-9781423492724", 21.95, "theory.jpg", 1],

    # Scores and Charts placeholders
#   [8, 4, "Classical Favorites", "Various", "13-9780793512737", 15.99, "scores.jpg", 0],
#]


# set up routes
@app.route('/')
def home():
    #Link to the index page.  Pass the categories as a parameter
    return render_template("index.html", categories=categories)
    #return render_template("index.html", categories=categories)

@app.route('/category/<int:category_id>')
def category(category_id):
    # Store the categoryId passed as a URL parameter into a variable
    #category_id = request.args.get("categoryId", type=int)

    # Create a new list called selected_books containing a list of books that have the selected category
    selected_books = [b for b in books if b["categoryId"] == category_id]

    # Link to the category page.  Pass the selectedCategory, categories and books as parameters

    return render_template(
   "category.html",
    selectedCategory=category_id,
    categories=categories,
    books=selected_books
    )

# we'll link this for project 2 to an sqlite3 database using flask's get_db() function
@app.route('/search')
def search():
    #Link to the search results page.
    return render_template()

@app.errorhandler(Exception)
def handle_error(e):
    """
    Output any errors - good for debugging.
    """
    return render_template('error.html', error=e) # render the edit template


if __name__ == "__main__":
    app.run(debug = True)
