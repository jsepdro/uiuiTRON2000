from random import randint

def voltaArtista():
    vetor_de_artistas = [
        "Frank Sinatra",
        "Lobo",
        "BlakkStar",
        "Arctic Monkeys",
        "John Legend",
        "George Ezra",
        "Céline Dion",
        "Skank",
        "Roberto Carlos",
        "Frank Ocean",
        "Bob Dylan",
        "Lord Huron"
    ]

    gerador = randint(0, 11)
    artista = vetor_de_artistas[gerador]
    str(artista)
    return artista