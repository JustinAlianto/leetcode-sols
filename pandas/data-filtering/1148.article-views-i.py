import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    view_own = views[views["viewer_id"] == views["author_id"]]["author_id"].unique()

    sorted_id = pd.DataFrame({"id": sorted(view_own)})

    return sorted_id
