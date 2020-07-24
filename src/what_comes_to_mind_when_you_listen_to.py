import argparse
import lyricsgenius
import matplotlib.pyplot as plt
import pandas as pd

class Lyrics:
    
    def __init__(self, token, title, artist, vanilla):
        self.token = token
        self.title = title
        self.artist = artist
        self.vanilla = vanilla
        genius = lyricsgenius.Genius("my_client_access_token_here")
        
    def song(self):
        genius = lyricsgenius.Genius(self.token)
        
        return genius.search_song(self.title, self.artist).lyrics
    
    def transform(self):
        lyrics = self.song()
        lyrics = lyrics.split("\n")
        lyrics = [x.replace(",", "") for x in lyrics]
        lyrics = [x.lower() for x in lyrics if "[" not in x]        
        lyrics = " ".join(lyrics).split(" ")
        if self.vanilla == False:
            remove = ["the", "and", "or", "it", "i", "a", "you", "to", "oh", "yeah", "by", "this", "that"]
            lyrics = [x for x in lyrics if x not in remove]
        unique = list(set(lyrics))
        unique = [x for x in unique if x != ""]
        df = pd.DataFrame([[x, lyrics.count(x)] for x in unique], columns=["words", "count"])
        df = df.sort_values(by = "count", ascending=False)
        top = df.iloc[:4]
        top = top.append(pd.DataFrame([{"words": "others", "count": sum(df.iloc[4:,1])}]))
        top = top.reset_index(drop=True)
        
        return top

    def visualize(self, top):
        labels = top.iloc[:,0] 
        sizes = top.iloc[:,1]
        colors = ['black', 'grey', 'darkgrey', 'lightgrey', 'whitesmoke']
        patches, texts = plt.pie(sizes, colors=colors, startangle=90)
        plt.legend(patches, labels, loc="best")
        plt.axis('equal')
        plt.tight_layout()
        plt.show()
        
if __name__ == "__main__":
    TOKEN = open("token.txt", "r").readline()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-t',
        '--title',
        type=str,
        help='Song title that you would like to get',
        metavar=''
    )
    parser.add_argument(
        '-a',
        '--artist',
        type=str,
        help='The artist name from the corresponding song title',
        metavar=''
    )
    args = parser.parse_args()
    title = args.title
    artist = args.artist
    lyrics = Lyrics(TOKEN, title, artist)
    top = lyrics.transform()
    lyrics.visualize(top)