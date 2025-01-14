import asyncio
import streamlit as st
from src.ui.layout import create_ui
from dotenv import load_dotenv
import os

# 載入環境變數
load_dotenv()

if __name__ == "__main__":
    create_ui() 