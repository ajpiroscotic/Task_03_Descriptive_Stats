# pandas_stats.py
import pandas as pd

def analyze_with_pandas(filepath, group_cols=None):
    df = pd.read_csv(filepath)

    results = {}
    if group_cols:
        grouped = df.groupby(group_cols)
        for g, sub in grouped:
            results[g] = {
                "describe": sub.describe(include="all"),
                "nunique": sub.nunique(),
                "value_counts": {col: sub[col].value_counts().head(1).to_dict() for col in sub.columns}
            }
    else:
        results["ALL"] = {
            "describe": df.describe(include="all"),
            "nunique": df.nunique(),
            "value_counts": {col: df[col].value_counts().head(1).to_dict() for col in df.columns}
        }
    return results

if __name__ == "__main__":
    for file in ["C:\Users\Anjaneya Padwal\Downloads\period_03 (1)\2024_fb_ads_president_scored_anon.csv", "C:\Users\Anjaneya Padwal\Downloads\period_03 (1)\2024_fb_posts_president_scored_anon.csv", "C:\Users\Anjaneya Padwal\Downloads\period_03 (1)\2024_tw_posts_president_scored_anon.csv"]:
        print(f"---- Analyzing {file} ----")
        res = analyze_with_pandas(file)
        for k,v in res.items():
            print(f"Group: {k}")
            print(v["describe"])
