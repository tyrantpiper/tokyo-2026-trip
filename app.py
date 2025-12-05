import streamlit as st
import streamlit.components.v1 as components

# 設定全螢幕與標題
st.set_page_config(page_title="2026 東京返鄉", layout="wide")

# 讀取 HTML
with open("index.html", "r", encoding='utf-8') as f:
    html_data = f.read()

# 顯示 HTML (height=1000 讓手機滑動順暢)
components.html(html_data, height=1000, scrolling=True)
