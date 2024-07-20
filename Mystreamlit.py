import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('火星隕石のスペクトルデータの可視化')

uploaded_file = st.file_uploader("CSVファイルをアップロードしてください")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file) 
    st.write(df)
    
    options = st.multiselect(
        '表示するスペクトルを選択してください',
        df.columns[1:],
        default=df.columns[1]
    )
    
    if options:                
        # グラフの作成
        fig, ax = plt.subplots()
        for column in options:
            ax.plot(df[df.columns[0]], df[column], label=column)
        
        ax.set_xlabel(df.columns[0])
        ax.set_ylabel('Reflectance')  # Reflectance は文字列として指定
        ax.legend()
        st.pyplot(fig)
else:
    st.write("少なくとも一つの列を選択してください。")

