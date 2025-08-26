import pandas as pd

# Create a comprehensive music artist genre dataset with around 200 entries
music_data = [
    # Pop Artists
    ("Taylor Swift", "Pop"),
    ("Taylor Swift", "Country"),
    ("Taylor Swift", "Folk"),
    ("Taylor Swift", "Alternative"),
    ("Ariana Grande", "Pop"),
    ("Ariana Grande", "R&B"),
    ("Ed Sheeran", "Pop"),
    ("Ed Sheeran", "Folk"),
    ("Ed Sheeran", "Acoustic"),
    ("Billie Eilish", "Pop"),
    ("Billie Eilish", "Alternative"),
    ("Billie Eilish", "Electropop"),
    ("Dua Lipa", "Pop"),
    ("Dua Lipa", "Dance"),
    ("Dua Lipa", "Disco"),
    
    # Rock Artists
    ("The Beatles", "Rock"),
    ("The Beatles", "Pop"),
    ("The Beatles", "Psychedelic"),
    ("Led Zeppelin", "Rock"),
    ("Led Zeppelin", "Hard Rock"),
    ("Led Zeppelin", "Blues"),
    ("Queen", "Rock"),
    ("Queen", "Arena Rock"),
    ("Queen", "Progressive Rock"),
    ("Pink Floyd", "Progressive Rock"),
    ("Pink Floyd", "Psychedelic"),
    ("Pink Floyd", "Art Rock"),
    ("The Rolling Stones", "Rock"),
    ("The Rolling Stones", "Blues Rock"),
    ("AC/DC", "Hard Rock"),
    ("AC/DC", "Heavy Metal"),
    
    # Hip Hop/Rap Artists
    ("Drake", "Hip Hop"),
    ("Drake", "R&B"),
    ("Drake", "Rap"),
    ("Kendrick Lamar", "Hip Hop"),
    ("Kendrick Lamar", "Conscious Rap"),
    ("Kendrick Lamar", "Jazz Rap"),
    ("Eminem", "Hip Hop"),
    ("Eminem", "Rap"),
    ("Jay-Z", "Hip Hop"),
    ("Jay-Z", "East Coast Hip Hop"),
    ("Kanye West", "Hip Hop"),
    ("Kanye West", "Production"),
    ("Kanye West", "Experimental"),
    ("Cardi B", "Hip Hop"),
    ("Cardi B", "Trap"),
    ("Travis Scott", "Hip Hop"),
    ("Travis Scott", "Trap"),
    ("Travis Scott", "Psychedelic Rap"),
    
    # R&B/Soul Artists
    ("Adele", "Pop"),
    ("Adele", "Soul"),
    ("Adele", "Ballad"),
    ("Beyoncé", "Pop"),
    ("Beyoncé", "R&B"),
    ("Beyoncé", "Soul"),
    ("John Legend", "R&B"),
    ("John Legend", "Soul"),
    ("John Legend", "Pop"),
    ("Alicia Keys", "R&B"),
    ("Alicia Keys", "Soul"),
    ("Alicia Keys", "Neo Soul"),
    ("The Weeknd", "R&B"),
    ("The Weeknd", "Pop"),
    ("The Weeknd", "Alternative R&B"),
    
    # Electronic/Dance Artists
    ("Calvin Harris", "Electronic"),
    ("Calvin Harris", "House"),
    ("Calvin Harris", "Dance"),
    ("Daft Punk", "Electronic"),
    ("Daft Punk", "House"),
    ("Daft Punk", "Disco"),
    ("Skrillex", "Electronic"),
    ("Skrillex", "Dubstep"),
    ("Skrillex", "EDM"),
    ("Deadmau5", "Electronic"),
    ("Deadmau5", "Progressive House"),
    ("Avicii", "Electronic"),
    ("Avicii", "House"),
    ("Avicii", "EDM"),
    
    # Country Artists
    ("Johnny Cash", "Country"),
    ("Johnny Cash", "Folk"),
    ("Johnny Cash", "Rockabilly"),
    ("Dolly Parton", "Country"),
    ("Dolly Parton", "Pop"),
    ("Carrie Underwood", "Country"),
    ("Carrie Underwood", "Pop"),
    ("Keith Urban", "Country"),
    ("Keith Urban", "Country Rock"),
    ("Blake Shelton", "Country"),
    ("Blake Shelton", "Country Pop"),
    
    # Jazz Artists
    ("Miles Davis", "Jazz"),
    ("Miles Davis", "Bebop"),
    ("Miles Davis", "Cool Jazz"),
    ("John Coltrane", "Jazz"),
    ("John Coltrane", "Bebop"),
    ("John Coltrane", "Free Jazz"),
    ("Ella Fitzgerald", "Jazz"),
    ("Ella Fitzgerald", "Vocal Jazz"),
    ("Louis Armstrong", "Jazz"),
    ("Louis Armstrong", "Traditional Jazz"),
    ("Duke Ellington", "Jazz"),
    ("Duke Ellington", "Big Band"),
    
    # Alternative/Indie Artists
    ("Radiohead", "Alternative Rock"),
    ("Radiohead", "Experimental"),
    ("Radiohead", "Art Rock"),
    ("Arctic Monkeys", "Indie Rock"),
    ("Arctic Monkeys", "Alternative Rock"),
    ("The Strokes", "Indie Rock"),
    ("The Strokes", "Garage Rock"),
    ("Coldplay", "Alternative Rock"),
    ("Coldplay", "Pop Rock"),
    ("Imagine Dragons", "Alternative Rock"),
    ("Imagine Dragons", "Pop Rock"),
    ("Imagine Dragons", "Electronic Rock"),
    
    # Metal Artists
    ("Metallica", "Heavy Metal"),
    ("Metallica", "Thrash Metal"),
    ("Iron Maiden", "Heavy Metal"),
    ("Iron Maiden", "Power Metal"),
    ("Black Sabbath", "Heavy Metal"),
    ("Black Sabbath", "Doom Metal"),
    ("Slayer", "Thrash Metal"),
    ("Slayer", "Speed Metal"),
    
    # Reggae Artists
    ("Bob Marley", "Reggae"),
    ("Bob Marley", "Ska"),
    ("Bob Marley", "Rocksteady"),
    ("Jimmy Buffett", "Tropical Rock"),
    ("Jimmy Buffett", "Country"),
    
    # Folk Artists
    ("Bob Dylan", "Folk"),
    ("Bob Dylan", "Rock"),
    ("Bob Dylan", "Country"),
    ("Joni Mitchell", "Folk"),
    ("Joni Mitchell", "Jazz"),
    ("Neil Young", "Folk Rock"),
    ("Neil Young", "Country Rock"),
    ("Neil Young", "Grunge"),
    
    # Classical/Orchestral
    ("Ludwig van Beethoven", "Classical"),
    ("Ludwig van Beethoven", "Romantic"),
    ("Wolfgang Amadeus Mozart", "Classical"),
    ("Johann Sebastian Bach", "Baroque"),
    ("Johann Sebastian Bach", "Classical"),
    
    # Latin Artists
    ("Shakira", "Latin Pop"),
    ("Shakira", "Pop"),
    ("Shakira", "Rock"),
    ("Ricky Martin", "Latin Pop"),
    ("Ricky Martin", "Pop"),
    ("Bad Bunny", "Reggaeton"),
    ("Bad Bunny", "Latin Trap"),
    ("J Balvin", "Reggaeton"),
    ("J Balvin", "Latin Pop"),
    
    # Punk Artists
    ("Green Day", "Punk Rock"),
    ("Green Day", "Pop Punk"),
    ("The Ramones", "Punk Rock"),
    ("The Ramones", "Garage Rock"),
    ("Sex Pistols", "Punk Rock"),
    ("The Clash", "Punk Rock"),
    ("The Clash", "Ska"),
    ("The Clash", "Reggae"),
    
    # Blues Artists
    ("B.B. King", "Blues"),
    ("B.B. King", "Electric Blues"),
    ("Muddy Waters", "Blues"),
    ("Muddy Waters", "Chicago Blues"),
    ("Eric Clapton", "Blues"),
    ("Eric Clapton", "Rock"),
    ("Stevie Ray Vaughan", "Blues"),
    ("Stevie Ray Vaughan", "Blues Rock"),
    
    # Funk Artists
    ("James Brown", "Funk"),
    ("James Brown", "Soul"),
    ("Parliament-Funkadelic", "Funk"),
    ("Parliament-Funkadelic", "Psychedelic"),
    ("Prince", "Funk"),
    ("Prince", "Pop"),
    ("Prince", "R&B"),
    ("Prince", "Rock"),
    
    # World Music
    ("Yo-Yo Ma", "Classical"),
    ("Yo-Yo Ma", "World Music"),
    ("Ravi Shankar", "Indian Classical"),
    ("Ravi Shankar", "World Music"),
    ("Buena Vista Social Club", "Cuban"),
    ("Buena Vista Social Club", "World Music"),
    
    # Modern Artists
    ("Billie Holiday", "Jazz"),
    ("Billie Holiday", "Blues"),
    ("Frank Sinatra", "Traditional Pop"),
    ("Frank Sinatra", "Jazz"),
    ("Frank Sinatra", "Swing"),
    ("Elvis Presley", "Rock and Roll"),
    ("Elvis Presley", "Pop"),
    ("Elvis Presley", "Country"),
    ("Michael Jackson", "Pop"),
    ("Michael Jackson", "R&B"),
    ("Michael Jackson", "Dance"),
    ("Michael Jackson", "Soul"),
    ("Whitney Houston", "Pop"),
    ("Whitney Houston", "R&B"),
    ("Whitney Houston", "Soul"),
    ("Madonna", "Pop"),
    ("Madonna", "Dance"),
    ("Madonna", "Electronic")
]

# Create DataFrame
music_genre_df = pd.DataFrame(music_data, columns=['name', 'genre_list'])

# Save to CSV file
csv_filename = 'music_dataset.csv'
music_genre_df.to_csv(csv_filename, index=False)
print(f"Dataset saved to '{csv_filename}'")

# Display the dataset
print("\nMusic Artist Genre Dataset")
print("=" * 50)
print(f"Total entries: {len(music_genre_df)}")
print(f"Unique artists: {music_genre_df['name'].nunique()}")
print(f"Unique genres: {music_genre_df['genre_list'].nunique()}")
print("\nFirst 20 entries:")
print(music_genre_df.head(20))

print("\nAll unique artists:")
print(sorted(music_genre_df['name'].unique()))

print("\nAll unique genres:")
print(sorted(music_genre_df['genre_list'].unique()))

# Show artist with most genres
artist_genre_count = music_genre_df.groupby('name').size().sort_values(ascending=False)
print(f"\nArtist with most genres: {artist_genre_count.index[0]} ({artist_genre_count.iloc[0]} genres)")

# Show most common genres
genre_count = music_genre_df['genre_list'].value_counts()
print(f"\nMost common genres:")
print(genre_count.head(10))
