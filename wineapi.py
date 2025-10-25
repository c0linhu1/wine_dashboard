"""
WineAPI for loading and querying combined red and white
wine quality data based on chemical properties, quality
ratings, and wine type.
Extracting data from the 'winequality-red.csv' and
'winequality-white.csv' files

Author: Colin Hui
"""

import pandas as pd
REDWINE_FILE = 'winequality-red.csv'
WHITEWINE_FILE = 'winequality-white.csv'

class WineAPI:

    # DataFrame to hold combined wine data
    wine_df = None

    def load_wine(self, red_file, white_file):
        """Load and combine red and white wine data with type labels."""
        # The columns in the csv files are separated by a semicolon instead
        # of a comma so we need to do 'sep = ";"'
        red = pd.read_csv(red_file, sep = ';')
        red['type'] = 'Red'

        white = pd.read_csv(white_file, sep = ';')
        white['type'] = 'White'

        # reset row index in the new 'wind_df'
        self.wine_df = pd.concat([red, white],
                                 ignore_index = True)

    def get_wine_types(self):
        """Return an alphabetically sorted list of unique wine types."""
        return sorted(self.wine_df['type'].
                      dropna().unique())

    def get_quality_levels(self):
        """Return sorted list of unique quality scores."""
        return sorted(self.wine_df['quality'].
                      dropna().unique())

    def filter_data(self, wine_type = None, min_quality = None,
                    max_quality = None, alcohol_range = None):
        """
        Filter wine data by type, quality, and alcohol content.
        Arguments:
        - wine_type: 'Red' or 'White'
        - min_quality, max_quality: range of quality to filter
        - alcohol_range: tuple (min, max) alcohol level
        Returns filtered DataFrame
        """
        df = self.wine_df.copy()

        if wine_type:
            df = df[df['type'] == wine_type]

        if min_quality is not None:
            df = df[df['quality'] >= min_quality]

        if max_quality is not None:
            df = df[df['quality'] <= max_quality]

        if alcohol_range:
            df = df[(df['alcohol'] >= alcohol_range[0]) & (df['alcohol'] <= alcohol_range[1])]

        return df


def main():
    """Basic test of WineAPI functionality."""
    api = WineAPI()
    api.load_wine(REDWINE_FILE, WHITEWINE_FILE)
    print("Types:", api.get_wine_types())
    print("Quality Levels:", api.get_quality_levels())
    filtered = api.filter_data(wine_type = "Red",
                               min_quality = 5,
                               alcohol_range = (9.5, 12.5))
    print(filtered.head())


if __name__ == '__main__':
    main()
