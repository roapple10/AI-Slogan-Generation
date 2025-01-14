import os
import sys

# 將專案根目錄加入到 Python 路徑
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from src.agents.slogan_agent import SloganAgent
from src.agents.inspect_agent import InspectAgent
from src.agents.score_agent import ScoreAgent

class AgentTeam:
    def __init__(self):
        self.slogan_agent = SloganAgent()
        self.inspect_agent = InspectAgent()
        self.score_agent = ScoreAgent()
        
    async def process_request(self, user_input: str) -> dict:
        # 步驟 1: 生成標語
        slogan = await self.slogan_agent.process(user_input)
        
        # 步驟 2: 檢查標語
        inspection_result = await self.inspect_agent.process(user_input, slogan)
        
        # 步驟 3: 評分
        score_result = await self.score_agent.process(slogan, inspection_result)
        
        return {
            "slogan": slogan,
            "inspection": inspection_result,
            "score": score_result,
            "final_score": score_result["score"]
        } 