import unittest
import pandas as pd
import sys, os

sys.path.append(os.path.abspath(os.path.join('scripts')))

from extract_dataframe import read_json
from extract_dataframe import TweetDfExtractor

# For unit testing the data reading and processing codes, 
# we will need about 5 tweet samples. 
# Create a sample not more than 10 tweets and place it in a json file.
# Provide the path to the samples tweets file you created below
#sampletweetsjsonfile = "./sampletweets.json"   #put here the path to where you placed the file e.g. ./sampletweets.json. 
_, tweet_list = read_json("../data/sampletweets.json" )

columns = [
    "created_at",
    "source",
    "original_text",
    "clean_text",
    "sentiment",
    "polarity",
    "subjectivity",
    "lang",
    "favorite_count",
    "retweet_count",
    "original_author",
    "screen_count",
    "followers_count",
    "friends_count",
    "possibly_sensitive",
    "hashtags",
    "user_mentions",
    "place"
]


class TestTweetDfExtractor(unittest.TestCase):
    """
		A class for unit-testing function in the fix_clean_tweets_dataframe.py file

		Args:
        -----
			unittest.TestCase this allows the new class to inherit
			from the unittest module
	"""

    def setUp(self) -> pd.DataFrame:
        self.df = TweetDfExtractor(tweet_list[:5])
        # tweet_df = self.df.get_tweet_df()

    def test_find_statuses_count(self):
        self.assertEqual(
            self.df.find_statuses_count(), [8097,5831,1627,1627,18958]
        )

    def test_find_full_text(self):
        text = ["""RT @i_ameztoy: Extra random image (I):\n\nLets focus in one very specific zone of the western coast -&gt; Longjing District, Taichung #City, #Ta\u2026""",
        """Extra random image (I):\n\nLets focus in one very specific zone of the western coast -&gt; Longjing District, Taichung #City, #Taiwan \n \n#Copernicus #Sentinel2 \ud83d\udef0\ufe0f 2022-08-03 \nFull Size -&gt; https://t.co/39IOoqJZR9 \ud83e\uddd0 https://t.co/rdf21paD5P""",
        """RT @IndoPac_Info: #China's media explains the military reasons for each area of the drills in the #Taiwan Strait\n\nRead the labels in the pi\u2026""",
        """#China's media explains the military reasons for each area of the drills in the #Taiwan Strait\n\nRead the labels in the pictures \u2b07\ufe0f Via CGTN https://t.co/0J4ilou4iv""",
        """China even cut off communication, they don't anwer phonecalls from the US. But here clown @ZelenskyyUa enters the stage to ask #XiJinping to change Putin's mind."""]

        self.assertEqual(self.df.find_full_text(), text)

    """
    def test_find_sentiments(self):
        self.assertEqual(
            self.df.find_sentiments(self.df.find_full_text()),
            (
                [],
                [],
            ),
        )

    """
    def test_find_screen_name(self):
        name = ['i_ameztoy','IndoPac_Info','ZIisq','ZelenskyyUa','Fin21Free']
        self.assertEqual(self.df.find_screen_name(), name)

    def test_find_followers_count(self):
        f_count = [20497,65,85,85,207]
        self.assertEqual(self.df.find_followers_count(), f_count)

    def test_find_friends_count(self):
        friends_count = [2621,272,392,2608,54]
        self.assertEqual(self.df.find_friends_count(), friends_count)

    """ def test_find_is_sensitive(self):
        self.assertEqual(self.df.is_sensitive(), [None,None,None,None,None])
    """

    # def test_find_hashtags(self):
    #     self.assertEqual(self.df.find_hashtags(), )

    # def test_find_mentions(self):
    #     self.assertEqual(self.df.find_mentions(), )



if __name__ == "__main__":
    unittest.main()

