from latex import create_pdf_file, create_tex_file


def main():
    moves = [
                (0, 0, 3),
                (0, 1, 4),
                (0, 2, 5),
                (0, 3, 6),
                (0, 4, 7),
                (0, 5, 8),
                (0, 6, 9),
                (0, 7, 10),
                (0, 8, 11),
                (0, 9, 12),
                (0, 10, 13),
                (0, 11, 14),
                (0, 12, 15),
                (0, 13, 0),
                (0, 14, 1),
                (0, 15, 2),

                (1, 0, 13),
                (1, 1, 14),
                (1, 2, 15),
                (1, 3, 0),
                (1, 4, 1),
                (1, 5, 2),
                (1, 6, 3),
                (1, 7, 4),
                (1, 8, 5),
                (1, 9, 6),
                (1, 10, 7),
                (1, 11, 8),
                (1, 12, 9),
                (1, 13, 10),
                (1, 14, 11),
                (1, 15, 12),
            ], 'jk'

    file = 'file.tex'
    create_tex_file(*moves, file)
    print('tex_file')
    create_pdf_file(file)
    print('pdf_file')


if __name__ == '__main__':
    main()
