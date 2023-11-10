## 폴더안의 파일 목록 가져오기
import os

def get_files_in_folder(folder_path):
    files = []
    for file_name in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file_name)
        if os.path.isfile(full_path):
            files.append(full_path)
    return files # ['./record/카카오뱅크_거래내역_N6317902420_2023111015494237.xlsx']



# 엑셀 파일 열고 df로 반환
import pandas as pd
import win32com.client
import pythoncom  # 추가된 부분

folder_path = 'C:/PlayData/kakao_USed/record/'
def read_excel_in_folder(idx):
    pythoncom.CoInitialize()
    
    folder_list = get_files_in_folder(folder_path)

    # Excel 앱 열기
    excel_app = win32com.client.Dispatch("Excel.Application")

    # Excel 파일 열기
    workbook = excel_app.Workbooks.Open(folder_list[idx])

    # 원하는 작업 수행
    sheet = workbook.Sheets("카카오뱅크 거래내역")
    df = pd.DataFrame(sheet.UsedRange())

    # df 전처리
    df = df.iloc[:, 1:]
    df.columns = df.iloc[10]
    new_df = df.iloc[11:].reset_index(drop=True)

    # Excel 앱 종료
    workbook.Close(False)  # Close without saving changes
    excel_app.Quit()
    pythoncom.CoUninitialize()

    

    return new_df
    