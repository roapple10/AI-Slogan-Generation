"""
UI 組件模塊
定義用於構建用戶界面的可重用組件
"""
import streamlit as st

def display_header(title: str):
    """顯示應用程序標題"""
    st.title(title)

def display_image(image_bytes: bytes):
    """顯示圖像"""
    st.image(image_bytes)

def display_results(results: dict):
    """顯示分析結果"""
    st.write("## 分析結果")
    for key, value in results.items():
        st.write(f"**{key}:** {value}")

def display_config(config: dict):
    """顯示配置信息"""
    st.write("## 配置信息")
    st.json(config)