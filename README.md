DATASET
========
The dataset include all the songs that have been on the Top 200 Weekly (Global) charts of Spotify in 2020 & 2021. The dataset include the following features:

* Highest Charting Position: The highest position that the song has been on in the Spotify Top 200 Weekly Global Charts in 2020 & 2021.
* Number of Times Charted: The number of times that the song has been on in the Spotify Top 200 Weekly Global Charts in 2020 & 2021.
* Week of Highest Charting: The week when the song had the Highest Position in the Spotify Top 200 Weekly Global Charts in 2020 & 2021.
* Song Name: Name of the song that has been on in the Spotify Top 200 Weekly Global Charts in 2020 & 2021.
* Song iD: The song ID provided by Spotify (unique to each song).
* Streams: Approximate number of streams the song has.
* Artist: The main artist/ artists involved in making the song.
* Artist Followers: The number of followers the main artist has on Spotify.
* Genre: The genres the song belongs to.
* Release Date: The initial date that the song was released.
* Weeks Charted: The weeks that the song has been on in the Spotify Top 200 Weekly Global Charts in 2020 & 2021.
* Popularity:The popularity of the track. The value will be between 0 and 100, with 100 being the most popular.
* Danceability: Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.
* Acousticness: A measure from 0.0 to 1.0 of whether the track is acoustic.
* Energy: Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy.
* Instrumentalness: Predicts whether a track contains no vocals. The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content.
* Liveness: Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live.
* Loudness: The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track. Values typical range between -60 and 0 db.
* Speechiness: Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value.
* Tempo: The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration.
* Valence: A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while * tracks with low valence sound more negative (e.g. sad, depressed, angry).
* Chord: The main chord of the song instrumental.

Acknowledgements-
This dataset would not be possible without the help of spotifycharts.com and Spotipy Python Library

Resultado esperado
------------------
* 1 - Quais são os 5 Artistas que mais tiveram Números de vezes mapeado? Colunas esperada (Artist, Number of Times Charted)
* 2 - Quais são as 5 músicas com maior popularidade? Colunas esperada (Song Name, Popularity)
* 3 - Quais são os 5 gêneros que contém mais seguidores? Colunas esperada (Genre, Followers)

Observações
------------
* Seja criativo;
* A linguagem de desenvolviemnto deve ser Python;
* É opcional a utilização de bibliotecas do Python;
* Deve se enviar o resultado e o código realizado;

ENTREGA
=======
* Caso prefira pode adicionar os códigos em um repositório e nos enviar o link do repositório, lembre-se de deixar o repositório público ou compartilhar com o email thiago@jumper.inf.br;
* Caso tenha baixado o arquivo zip, nos envie este mesmo projeto em formato compactado, com os seus fontes para o email thiago@jumper.inf.br;
* Para Adicionar algum comentário/observação que achar importante, adicione como comentário no código;