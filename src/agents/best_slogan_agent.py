from google import genai
import os
from dotenv import load_dotenv

class BestSloganAgent:
    def __init__(self):
        try:
            # 確保環境變數已載入
            load_dotenv()
            
            # 從環境變數獲取 API KEY 和 MODEL NAME
            api_key = os.getenv("GOOGLE_API_KEY")
            model_name = os.getenv("MODEL_NAME")
            
            if not api_key:
                raise ValueError("GOOGLE_API_KEY not found in environment variables")
            if not model_name:
                raise ValueError("MODEL_NAME not found in environment variables")
                
            # 初始化 client
            self.client = genai.Client(api_key=api_key)
            self.model_name = model_name
            
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
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt
            )
            return {
                "best_slogan": self._find_best_slogan(slogans_data),
                "analysis": response.text.strip()
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