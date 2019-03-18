import pandas as pd

groups = ["Modern Web", "DevOps", "Cloud", "Big Data", "Security", "自我挑戰組"]
ironmen = [59, 9, 19, 14, 6, 77]

ironmen_dict = {
                "groups": groups,
                "ironmen": ironmen
}

# 建立 data frame
ironmen_df = pd.DataFrame(ironmen_dict)

# 選擇欄位
print(ironmen_df.ix[:, "groups"])
print("---") # 分隔線

# 選擇觀測值
print(ironmen_df.ix[0])
print("---") # 分隔線

# 同時選擇欄位與觀測值
print(ironmen_df.ix[0, "groups"])