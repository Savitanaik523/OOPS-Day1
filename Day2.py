class Book:
    def __init__(self,title,auther):
        self.title=title
        self.auther=auther
        
    def diplay_book_details(self):
        print("Title: ",self.title)
        print("Auther: ",self.auther)
        
class LibraryBook(Book):
    def __init__(self,title,auther,book_id):
        super().__init__(title,auther)
        self.book_id=book_id
        
    def diplay_book_details(self):
        self.display_book_details()
        print("Book ID:",self.book_id)
        
obj=LibraryBook("Python Programming","Guido van Rossum",101)
obj.display_book_details()
        