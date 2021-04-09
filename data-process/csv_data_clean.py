import pandas as pd

# The absolute path of the csv file.
PATH = r"C:/Users/hzb/Desktop/毕业设计/热塑性材料信息.xlsx"

if __name__ == "__main__":
    df = pd.read_excel(PATH, engine='openpyxl')

    # 1. Remove all empty columns.
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    # 2. Fill empty values in TEXT fields.
    df.iloc[:, list(range(13))].fillna("未获得", inplace=True)    

    # 3. Convert nemerical field to float and fill empty values as NaN.
    for num_field_idx in range(13, 59):
        # Use type transform and catch the errors with blank values.
        df.iloc[:, num_field_idx] = pd.to_numeric(df.iloc[:, num_field_idx], errors="coerce")
    
    df.insert(0, "id", range(0, len(df)))
    
    # 4. Remove duplicate field values and reserve the column.
    df.链接 = pd.Series([df.链接 == df.制造商]).replace(True, None, inplace=True)
    df.测试日期 = pd.Series([df.测试日期 == df.上次修改日期]).replace(True, None, inplace=True)
    
    # 5. Detect data exceptions.
    mis_arr = [False] * 20 + list(df[20:].热膨胀数据横向各向同性系数alpha2.isna())
    df["列错乱"] = mis_arr

    df.to_csv(r"D:/test.csv", index=None)
