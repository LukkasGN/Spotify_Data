import pandas as pd

dataFrame = pd.read_csv('spotify_dataset.csv', delimiter= ',')
print(dataFrame.columns)

# 1 - Quais são os 5 Artistas que mais tiveram Números de vezes mapeado?

valorMapMax = dataFrame.nlargest(5, 'Number of Times Charted')[['Artist','Number of Times Charted']]
print("Melhores 5 artistas e suas respectivas vezes mapeados: ")
print(valorMapMax)

# 2 - Quais são as 5 músicas com maior popularidade?

print("Melhores 5 musicas com maior popularidade: ")
dataMusic = dataFrame.sort_values(['Popularity'], ascending = False)
print(dataMusic[['Song Name', 'Popularity']].iloc[0:5])

#3 - Quais são os 5 gêneros que contém mais seguidores?

print("Melhores 5 gêneros com mais seguidores: ")
dataGen = dataFrame.sort_values(['Artist Followers'], ascending = False)
print(dataGen[['Genre', 'Artist Followers']].iloc[0:5])