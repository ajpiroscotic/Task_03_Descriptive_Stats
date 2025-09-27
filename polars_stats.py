# polars_stats.py
import polars as pl

def analyze_with_polars(filepath, group_cols=None):
    df = pl.read_csv(filepath)

    results = {}
    if group_cols:
        grouped = df.groupby(group_cols)
        for g, sub in grouped:
            results[g] = {
                "describe": sub.describe(),
                "nunique": sub.n_unique(),
            }
    else:
        results["ALL"] = {
            "describe": df.describe(),
            "nunique": df.n_unique(),
        }
    return results

if __name__ == "__main__":
    for file in ["C:\Users\Anjaneya Padwal\Downloads\period_03 (1)\2024_fb_ads_president_scored_anon.csv", "C:\Users\Anjaneya Padwal\Downloads\period_03 (1)\2024_fb_posts_president_scored_anon.csv", "C:\Users\Anjaneya Padwal\Downloads\period_03 (1)\2024_tw_posts_president_scored_anon.csv"]:
        print(f"---- Analyzing {file} ----")
        res = analyze_with_polars(file)
        print(res)
