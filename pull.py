import pandas as pd
import gspread as gs


class Pull:
    def __init__(self):
        self.sheet_id = "1Duo8OpvQAtJEO7y6_gsfykl77wUpi8IkVNyr1Yt4L1I"
        self.sheet_name = "2021-2022 Robotics Team Signup(responses)"
        self.url = f"https://docs.google.com/spreadsheets/d/1Duo8OpvQAtJEO7y6_gsfykl77wUpi8IkVNyr1Yt4L1I/edit#gid=1524028929"
        



    def return_data(self):
        gc = gs.service_account(filename='robodata-352301-c15537264bd5.json')
        sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1Rps9sAo_nU-AxezrMeutLEoNQF86ktgDB4RT0aWrsM8/edit#gid=0')

        ws = sh.worksheet('Sheet1')

        df = pd.DataFrame(ws.get_all_records())

        print(pd.DataFrame(df, columns=['First Name', 'Last Name', 'Best Email to contact you with.']))