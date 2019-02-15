class Libro():
    def __init__(self, nombre, genero, autor, book_id):
        self.nombre = nombre
        self.genero = genero
        self.autor = autor
        self.book_id = book_id

    def dame_info(self):
        return 'Book({}, {}, {},{})'.format(self.nombre, self.genero, self.autor, self.book_id)

    def prestamo(self):
        prestamo = 'Usted tiene 15 días para disfrutar del libro '
        return prestamo
