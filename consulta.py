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
        "Lord Huron",
        "Marisa Monte",
        "Nick Jonas",
        "Joji",
        "Trevor Daniel",
        "Chase Atlantic"

    ]

    gerador = randint(0, 12)
    artista = vetor_de_artistas[gerador]
    str(artista)
    return artista
