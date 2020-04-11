
def book_image_path(instanse, filename):
    file_type = filename.split('.')[-1]
    return f'books/{instanse.isbn}.{file_type}'