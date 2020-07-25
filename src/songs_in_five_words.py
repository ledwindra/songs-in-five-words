import argparse
import lyricsgenius
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import pandas as pd
import re

class Lyrics:
    
    def __init__(self, token):
        self.token = token
        self.title = args.title
        self.artist = args.artist
        self.vanilla = args.vanilla
        
    def song(self):
        genius = lyricsgenius.Genius(self.token)
        
        return genius.search_song(self.title, self.artist).lyrics
    
    def transform(self):
        lyrics = self.song()
        lyrics = lyrics.split("\n")
        lyrics = [x.replace(",", "") for x in lyrics]
        lyrics = " ".join(lyrics).split(" ")
        lyrics = [re.sub(r'[^\w]', '', x.lower()) for x in lyrics]
        if not self.vanilla:
            remove = [
                'a',
                'as',
                'and',
                'by',
                'dont',
                'i',
                'it',
                'its',
                'me',
                'my',
                'of',
                'oh',
                'or',
                'some',
                'that',
                'the',
                'this',
                'to',
                'we',
                'with',
                'yeah',
                'you'
            ]
            lyrics = [x for x in lyrics if x not in remove]
        unique = list(set(lyrics))
        unique = [x for x in unique if x != '']
        df = pd.DataFrame([[x, lyrics.count(x)] for x in unique], columns=['words', 'count'])
        df = df.sort_values(by = 'count', ascending=False)
        top = df.iloc[:5]
        top = top.append(pd.DataFrame([{'words': 'others', 'count': sum(df.iloc[5:,1])}]))
        top = top.reset_index(drop=True)
        
        return top

    def visualize(self, top):
        font = {
            'fontname':'Comic Sans MS',
            'size': 22
        }
        legend_font = font_manager.FontProperties(
            family='Comic Sans MS',
            weight='bold',
            style='normal',
            size=16
        )
        plt.xkcd()
        labels = top.iloc[:,0] 
        sizes = top.iloc[:,1]
        colors = ['black', 'grey', 'darkgrey', 'lightgrey', 'gainsboro', 'whitesmoke']
        patches, texts = plt.pie(
            sizes,
            colors=colors,
            startangle=90,
            wedgeprops={
                'edgecolor':'k',
                'linewidth': 1,
                'linestyle': 'solid'
            }
        )
        plt.title(self.title,  **font)
        plt.legend(patches, labels, loc='best', prop=legend_font)
        plt.axis('equal')
        plt.tight_layout()
        plt.xkcd()
        plt.show()
        
if __name__ == '__main__':
    TOKEN = open('./util/token.txt', 'r').readline()
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
    parser.add_argument(
        '-v',
        '--vanilla',
        type=bool,
        default=False,
        help='If set True, the program will include stop words',
        metavar=''
    )
    args = parser.parse_args()
    lyrics = Lyrics(TOKEN)
    top = lyrics.transform()
    lyrics.visualize(top)