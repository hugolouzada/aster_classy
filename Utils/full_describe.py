import pandas as pd


def full_describe(series: pd.Series, verbose=True):
    """
    Calculates a pandas describe of series, plus a count of unique and NaN


    :param verbose: printing some other info
    :param series: Pandas Series
    :return: df with stats as cols
    """
    stats_df = pd.DataFrame()

    stats_df['dtype_kind'] = pd.Series([series.dtype.kind])
    stats_df['null_count'] = pd.Series([series.isnull().sum()])

    pandas_des = series.describe()

    if series.dtype.kind != 'o':
        str_des = series.astype(str).describe()
        pandas_des = pandas_des.append(str_des.drop('count'))

    stats_df = pd.concat([pd.DataFrame(pandas_des).transpose(), stats_df], axis=1)

    return stats_df


class TestFullDescribe:

    @classmethod
    def setup_class(cls):
        float_series = pd.Series([2,3,4.0,4.0,5])
        float_integer = pd.Series([2,3,4,4,5,5,5,5,5])
        string_series = pd.Series(['a','b','c','d','d'])

        cls.desc_float = full_describe(float_series)
        cls.desc_int = full_describe(float_integer)
        cls.desc_string = full_describe(string_series)

    def test_dtype_kind(self):
        assert self.desc_float.iloc[0]["dtype_kind"] == "f"
        assert self.desc_string.iloc[0]["dtype_kind"] == "O"
        assert self.desc_int.iloc[0]["dtype_kind"] == "i"