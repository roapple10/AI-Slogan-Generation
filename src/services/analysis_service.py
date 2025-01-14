"""
分析服務模塊
定義用於執行多模態數據分析的服務
"""
from typing import Any
from src.agents import VisionAgent, UXAgent, MarketAgent
from src.config.settings import settings

class AnalysisService:
    """分析服務，協調多個代理執行分析"""
    
    def __init__(self, model: Any):
        """初始化分析服務"""
        self.vision_agent = VisionAgent(model=model, instructions=["Analyze the image."])
        self.ux_agent = UXAgent(model=model, instructions=["Analyze the user interface data."])
        self.market_agent = MarketAgent(model=model, instructions=["Analyze the market data."])
    
    def analyze(self, data: dict) -> dict:
        """
        執行多模態數據分析
        
        Args:
            data: 包含不同模態數據的字典
            
        Returns:
            包含各代理分析結果的字典
        """
        vision_result = self.vision_agent.process(data.get("image"))
        ux_result = self.ux_agent.process(data.get("ui"))
        market_result = self.market_agent.process(data.get("market"))
        
        return {
            "vision_analysis": vision_result,
            "ux_analysis": ux_result,
            "market_analysis": market_result,
        }