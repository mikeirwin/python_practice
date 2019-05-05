from projects.A_Sorted_Tale.sorts import bubble_sort
from projects.A_Sorted_Tale.sorts import quicksort
from projects.A_Sorted_Tale.utils import load_books


bookshelf = load_books('books_small.csv')
bookshelf_v1 = bookshelf.copy()
bookshelf_v2 = bookshelf.copy()
long_bookshelf = load_books('books_large.csv')


def by_title_ascending(book_a, book_b):
    return book_a['title_lower'] > book_b['title_lower']


def by_author_ascending(book_a, book_b):
    return book_a['author_lower'] > book_b['author_lower']


def by_total_length(book_a, book_b):
    return len(book_a['author_lower']) + len(book_a['title_lower']) > len(book_b['author_lower']) + len(book_b['title_lower'])


sort_1 = bubble_sort(bookshelf, by_title_ascending)
sort_2 = bubble_sort(bookshelf, by_author_ascending)
#sort_3 = bubble_sort(long_bookshelf, by_total_length)

quicksort(long_bookshelf, 0, len(long_bookshelf) - 1, by_total_length)

for book in long_bookshelf:
    print(book['title'] + ' by ' + book['author'])

