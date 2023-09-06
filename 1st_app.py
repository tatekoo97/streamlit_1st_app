import streamlit as st 

st.title("郵便番号・住所検索（東京都）")

csv_path = './13tokyo/13TOKYO.CSV'

with st.form(key='postCode_form', clear_on_submit=True):

    def GetAddress():
        postal_code = st.text_input("郵便番号を入力：")
        with open(csv_path, "r", encoding="shift_jis") as f:
            for line in f:
                line = line.replace(' ', '') # スペースカット
                line = line.replace('"', '') # ダブルクォーテーションカット
                cells = line.split(",")      # カンマ区切り
                code = cells[2]  # 郵便番名
                pref = cells[6]  # 都道府県名
                city = cells[7]  # 市区町村名
                ad = cells[8]    # 番地
                title = pref + city + ad
                if code.find(postal_code) != -1:
                    if postal_code:
                        st.sidebar.text(title)
    GetAddress()


    def GetPostCode():
        
        addr = st.text_input("住所を入力：")
        with open(csv_path, "r", encoding="shift_jis") as f:
            for line in f:
                line = line.replace(' ', '') # cut space
                line = line.replace('"', '') # cut double quatation
                cells = line.split(",")      # split by comma
                code = cells[2]  # Postal Code
                pref = cells[6]  # Prefucture
                city = cells[7]  # City name
                ad = cells[8]    # Address name
                title = pref + city + ad
                if title.find(addr) != -1:
                    if addr:
                        st.sidebar.text(code + ":" + title)  
    GetPostCode()
    submit_btn = st.form_submit_button("送信")
    cancel_btn = st.form_submit_button("キャンセル")
