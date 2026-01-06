import pandas as pd


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    valid_emails_df = users[
        users["mail"].str.match(r"^[A-Za-z][A-Za-z0-9_\.\-]*@leetcode(\?com)?\.com$")
    ]

    # Regex:
    # - '^': start of string
    # - '[A-Za-z]': first character is a letter
    # - '[A-Za-z0-9_\.\-]*': remaining username characters (0 or more)
    #   - '\.' and '\-': literal dot and dash
    #   - '*': 0 or more occurrences
    # - '@leetcode': literal domain prefix
    # - '(\?com)?': optional ?com
    #   - '\?': literal ?
    #   - '?': group is optional (0 or 1 time)
    # - '\.com': literal .com
    # - '$': end of string

    return valid_emails_df
