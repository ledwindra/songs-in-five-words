# About
There are of course many ways to describe a song. Some have emotional attachments
towards certain songs. This is not an attempt to say that's right or wrong. It's
just a no brainer way to describe a song in just a five words. Would this be a
futile effort? Well, let's just see!

# Clone
In any case you're interested, just do the following:

```
cd ~
git clone https://github.com/songs-in-five-words.git
cd songs-in-five-words.git
```

# Virtual environment
If you don't want to mess up with the existing modules installed in your machine,
use the virtual environment by doing the following:

```
python3 -m venv .venv
source .venv/bin/activate
```

When you want exit, just type `deactivate` and you're not out ⛔️.

# Modules
To get the lyrics, I use [LyricsGenius](https://github.com/johnwmillr/lyricsgenius) API. 
Other modules are needed such as [pandas](https://github.com/pandas-dev/pandas) to 
manipulate the DataFrame and [matplotlib](https://github.com/matplotlib/matplotlib) 
to make the nice visualization. Run the following to install them. Please note that
you may need to activate the virtual environment if you don't want to mess up with
the existing modules inside your machine 😄:

```
source .venv/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt
```

You're all set!

# Run
We only need to run one program, which is located inside `/src/songs_in_five_words.py`. 
It takes three arguments, where the two of them are very crucial since you will 
have to pick one song from one artist 😎! If you're still unsure, do the following: 

```
python3 src/songs_in_five_words.py --help

usage: songs_in_five_words.py [-h] [-t] [-a] [-v]

optional arguments:
  -h, --help       show this help message and exit
  -t , --title     Song title that you would like to get
  -a , --artist    The artist name from the corresponding song title
  -v , --vanilla   If set True, the program will include stop words
```

Let's break them down! `-t` or `--title` is needed to get the song title. `a` or
`--artist` is needed to get the song artist. Both of them are case <strong>INSENSTIVE</strong>,
so you don't have to worry if you're unsure or make a typo 😬. Lastly, `v` or
`--vanilla` will determine whether or not the stopwords are dropped (e.g. `and`,
`or`, `the`, etc). By default, it's set as `False`. Otherwise, you can set as
`True` (yes, it's capitalized in the respective first letters). For example:

```
# no capitalization
python3 src/songs_in_five_words.py -t "cocaine" -a "eric clapton" -v False

# liberal capitalization
python3 src/songs_in_five_words.py -t "cOcainE" -a "eRic cLapTon" -v False

# not vanilla
python3 src/songs_in_five_words.py -t "cocaine" -a "eric clapton" -v True
```

# Contribute or complain?

You can contribute by making pull request. Note that you need to create your own
branch. I don't know what would be the incentives for you, though 🤣. Conversely,
if you want to file a complain, just make an issue. Hopefully I could make it through.

# End
I hope you enjoy this. And thank you! 🙏🏽