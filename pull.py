import pandas as pd
import gspread as gs


class Pull:
    def __init__(self):
        self.sheet_name = "Sheet1"
        self.url = 'https://docs.google.com/spreadsheets/d/1Rps9sAo_nU-AxezrMeutLEoNQF86ktgDB4RT0aWrsM8/edit#gid=0'
        
        


    def return_data(self):
        gc = gs.service_account(filename='robodata-352301-c15537264bd5.json')
        sh = gc.open_by_url(self.url)

        ws = sh.worksheet(self.sheet_name)

        df = pd.DataFrame(ws.get_all_records())

        data = pd.DataFrame(df, columns=['First Name', 'Discord Account Information (username#****)(optional)'])

        rows = data.values.tolist()

        return rows