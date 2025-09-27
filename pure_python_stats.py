# pure_python_stats.py
import csv
import math
from collections import defaultdict, Counter

def is_number(val):
    try:
        float(val)
        return True
    except:
        return False

def compute_stats(values):
    n = len(values)
    if n == 0:
        return {"count": 0}
    nums = [float(v) for v in values if is_number(v)]
    if nums:
        mean = sum(nums) / len(nums)
        var = sum((x - mean) ** 2 for x in nums) / len(nums)
        return {
            "count": n,
            "mean": mean,
            "min": min(nums),
            "max": max(nums),
            "std": math.sqrt(var)
        }
    else:
        freq = Counter(values)
        return {
            "count": n,
            "unique": len(freq),
            "most_common": freq.most_common(1)[0]
        }

def analyze_csv(filepath, group_cols=None):
    with open(filepath, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if group_cols:
        groups = defaultdict(list)
        for row in rows:
            key = tuple(row[c] for c in group_cols)
            groups[key].append(row)
    else:
        groups = {("ALL",): rows}

    results = {}
    for g, subset in groups.items():
        col_data = defaultdict(list)
        for row in subset:
            for col, val in row.items():
                if val.strip() not in ("", "-", "null"):
                    col_data[col].append(val)

        results[g] = {col: compute_stats(vals) for col, vals in col_data.items()}
    return results

if __name__ == "__main__":
    for file in ["C:\Users\Anjaneya Padwal\Downloads\period_03 (1)\2024_fb_ads_president_scored_anon.csv", "C:\Users\Anjaneya Padwal\Downloads\period_03 (1)\2024_fb_posts_president_scored_anon.csv", "C:\Users\Anjaneya Padwal\Downloads\period_03 (1)\2024_tw_posts_president_scored_anon.csv"]:
        print(f"---- Analyzing {file} ----")
        res = analyze_csv(file)
        print(res)
