import pandas as pd


class Clean_Tweets:
    """
    The PEP8 Standard AMAZING!!!
    """
    def __init__(self, df:pd.DataFrame):
        self.df = df
        print('Automation in Action...!!!')
        
    def drop_unwanted_column(self) -> pd.DataFrame:
        columns = ['created_at', 'source', 'original_text', 'retweet_text', 'sentiment', 'polarity',
                   'subjectivity', 'lang', 'statuses_count', 'favorite_count', 'retweet_count',
                   'screen_name', 'followers_count', 'friends_count', 'possibly_sensitive',
                   'hashtags', 'user_mentions', 'location']
        unwanted_rows = []
        for columnName in columns:
            unwanted_rows = self.df[self.df[columnName] == columnName].index
            self.df.drop(unwanted_rows, inplace=True)
            self.df.reset_index(drop=True, inplace=True)
        return self.df

    def drop_duplicate(self, df:pd.DataFrame)->pd.DataFrame:
        """
        drop duplicate rows
        """
        
        df.drop_duplicates(inplace=True)
        df.reset_index(drop=True, inplace=True)
        
        return df
    def convert_to_datetime(self, df:pd.DataFrame)->pd.DataFrame:
        """
        convert column to datetime
        """
        df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce')
        
        return df
    
    def convert_to_numbers(self, df:pd.DataFrame)->pd.DataFrame:
        """
        convert columns like polarity, subjectivity, retweet_count
        favorite_count etc to numbers
        """

        """
        Here sentiment, Statuses_count, followers_count, 
        and friends_count are added.
        """

        df['polarity'] = pd.to_numeric(df['polarity'])
        df['Subjectivity'] = pd.to_numeric(df['Subjectivity'])
        df['retweet_count'] = pd.to_numeric(df['retweet_count'])
        df['favourite_count'] = pd.to_numeric(df['favourite_count'])
        df['sentiment'] = pd.to_numeric(df['sentiment'])
        df['statuses_count'] = pd.to_numeric(df['statuses_count'])
        df['followers_count'] = pd.to_numeric(df['followers_count'])
        df['friends_count'] = pd.to_numeric(df['friends_count'])

        return df
    
    def remove_non_english_tweets(self, df:pd.DataFrame)->pd.DataFrame:
        """
        remove non english tweets from lang
        """
        
        index_names = self.df[self.df['lang'] != 'en'].index
        self.df.drop(index_names, inplace=True)
        self.df.reset_index(drop=True, inplace=True)
        return self.df