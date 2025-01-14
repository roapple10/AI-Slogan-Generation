"""
基礎代理類模塊
定義所有代理的共同接口和基本功能
"""
from abc import ABC, abstractmethod
from typing import Any

class BaseAgent(ABC):
    """基礎代理類，定義所有代理的共同接口"""
    
    def __init__(self, name: str):
        """
        初始化基礎代理
        
        Args:
            name: 代理名稱
        """
        self.name = name
        self.response = None
        
    @abstractmethod
    async def process(self, *args, **kwargs) -> Any:
        """
        處理輸入數據的抽象方法
        """
        pass
    
    def get_response(self) -> str:
        """
        獲取代理響應
        
        Returns:
            代理的響應文本
        """
        return self.response