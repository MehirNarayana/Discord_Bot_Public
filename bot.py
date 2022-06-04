import pandas as pd

sheet_id = "1Duo8OpvQAtJEO7y6_gsfykl77wUpi8IkVNyr1Yt4L1I"
sheet_name = "2021-2022 Robotics Team Signup(responses)"
url = f"https://docs.google.com/spreadsheets/d/1Duo8OpvQAtJEO7y6_gsfykl77wUpi8IkVNyr1Yt4L1I/edit#gid=1524028929"

dataframe = pd.read_csv(url, on_bad_lines='skip')

print(dataframe)