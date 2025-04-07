"""
配置設置模塊
定義應用程序的全局配置
"""
import os

class Settings:
    """應用程序配置"""
    
    def __init__(self):
        """初始化配置"""
        self.api_key = os.getenv("API_KEY")
        self.model_name = os.getenv("MODEL_NAME", "gemini-2.0-flash-exp")
        # 可以添加更多配置項
        
settings = Settings()