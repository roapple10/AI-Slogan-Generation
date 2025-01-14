from phi.agent import Agent
from phi.model.google import Gemini
import os
from dotenv import load_dotenv

class BestSloganAgent:
    def __init__(self):
        try:
            # 確保環境變數已載入
            load_dotenv()
            
            # 從環境變數獲取 API KEY
            api_key = os.getenv("GOOGLE_API_KEY")
            if not api_key:
                raise ValueError("GOOGLE_API_KEY not found in environment variables")
            
            # 初始化 model
            model = Gemini(id="gemini-pro", api_key=api_key)
            
            # 初始化 agent
            self.agent = Agent(
                model=model,
                instructions=[
                    "You are a Traditional Chinese best slogan selector that:",
                    "1. Analyzes multiple slogans and their scores",
                    "2. Considers feedback and improvement suggestions",
                    "3. Provides detailed explanation for selection",
                    "4. Makes recommendations for optimization"
                ],
                markdown=True
            )
        except Exception as e:
            raise Exception(f"Error initializing BestSloganAgent: {str(e)}")

    async def process(self, slogans_data: list) -> dict:
        """分析所有標語並選出最佳標語"""
        prompt = f"""
        請使用繁體中文，從以下標語中選出最佳標語並提供優化建議。

        所有標語及其評分：
        {self._format_slogans_data(slogans_data)}

        請提供：
        1. 最佳標語選擇
        2. 選擇理由
        3. 優化建議（如何讓這個標語更好）
        4. 其他標語的參考價值（可以借鑒的優點）
        """
        
        try:
            response = self.agent.run(message=prompt)
            return {
                "best_slogan": self._find_best_slogan(slogans_data),
                "analysis": response.content.strip()
            }
        except Exception as e:
            raise Exception(f"Error selecting best slogan: {str(e)}")

    def _format_slogans_data(self, slogans_data: list) -> str:
        """格式化標語數據"""
        formatted_data = ""
        for i, result in enumerate(slogans_data, 1):
            formatted_data += f"""
            第{i}個標語：
            標語內容：{result['slogan']}
            得分：{result['score']['score']}/5
            評價：{result['score']['feedback']}
            ---
            """
        return formatted_data

    def _find_best_slogan(self, slogans_data: list) -> dict:
        """找出得分最高的標語"""
        return max(slogans_data, key=lambda x: x['score']['score']) 