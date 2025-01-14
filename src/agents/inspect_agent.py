from phi.agent import Agent
from phi.model.google import Gemini
import os
from dotenv import load_dotenv

class InspectAgent:
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
                    "You are a slogan quality inspector that:",
                    "1. Analyzes if slogans effectively reference user input",
                    "2. Checks for clarity and relevance",
                    "3. Provides detailed analysis",
                    "4. Ensures key product features are included"
                ],
                markdown=True
            )
        except Exception as e:
            raise Exception(f"Error initializing InspectAgent: {str(e)}")

    async def process(self, user_input: str, slogan: str) -> dict:
        """檢查標語是否有效參考使用者輸入"""
        prompt = f"""
        請使用繁體中文，分析以下廣告標語是否有效參考了產品資訊：

        產品資訊：
        {user_input}

        廣告標語：
        {slogan}

        分析要求：
        1. 必須使用繁體中文回答
        2. 檢查標語是否包含產品關鍵特點
        3. 評估標語與產品的相關性
        4. 判斷是否有效傳達產品價值
        
        請提供分析結果，包含：
        1. 是否有效參考（請回答「是」或「否」）
        2. 詳細分析說明（使用繁體中文）
        """
        
        try:
            # 使用同步方式調用
            response = self.agent.run(message=prompt)
            analysis = response.content.strip()
            
            # 解析回應，判斷是否有效參考
            referenced = "true" in analysis.lower()
            
            return {
                "analysis": analysis,
                "referenced": referenced
            }
        except Exception as e:
            raise Exception(f"Error analyzing slogan: {str(e)}")

    def get_response(self) -> str:
        return self.response 