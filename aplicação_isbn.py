def binary_search_isbn(records, isbn):
    """
    Busca binária para localizar livro por ISBN em registros ordenados.
    """
    low, high = 0, len(records) - 1
    while low <= high:
        mid = (low + high) // 2
        if records[mid]["isbn"] == isbn:
            return records[mid]
        elif records[mid]["isbn"] < isbn:
            low = mid + 1
        else:
            high = mid - 1
    return None

# Exemplo de uso
library = [
    {"isbn": "0001", "title": "Book A"},
    {"isbn": "0002", "title": "Book B"},
    {"isbn": "0003", "title": "Book C"},
]
print(binary_search_isbn(library, "0002"))  # Saída: {'isbn': '0002', 'title': 'Book B'}
