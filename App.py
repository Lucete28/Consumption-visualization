import streamlit as st
from fun import *


    
    
def show_data():
    df = st.session_state.df
    with_draw = df.loc[df['구분'] == '출금', '거래금액'].str.replace(',', '').astype(int).sum()
    deposit= df.loc[df['구분'] == '입금', '거래금액'].str.replace(',', '').astype(int).sum()
    Deal_list = df['거래구분'].unique().tolist()
    c1,c2 = st.columns(2)
    c1.write(f'총 출금 금액 : {with_draw}')
    # 전체 선택 상태를 나타내는 변수
    All_select = False
    now_selected = []
    # '전체 선택' 버튼 생성
    
    # All_select = False
    # now_selected = []
    # Deal_list = [1,2,3,4,5]
    c1,c2 = st.columns(2)
    
    All_select = c1.checkbox('전체 선택', key='All_select')
    for deal in Deal_list:
        if not All_select:
            선택 = c1.checkbox(deal)
            if 선택:
                now_selected.append(deal)
        else:   
            # 전체 선택이 활성화되어 있으면 모든 항목을 선택으로 표시
            now_selected.append(deal)
    
    
    c2.write(f'총 입금 금액 : {deposit}')
    st.write(df)
# 초기화
PATH = r'C:\PlayData\kakao_USed\record'
st.title('카카오 거래 보기')
files = get_files_in_folder(PATH)
for file in files:
    if st.sidebar.button(file):
        # st.session_state.now_file = file
        df = read_excel_in_folder(files.index(file))
        st.session_state.df = df
        # show_data()

if not st.session_state.df.empty:
    show_data()
    

