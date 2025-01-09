from langchain_openai import ChatOpenAI
from browser_use import Agent, Controller
from browser_use.browser.browser import Browser, BrowserConfig
from dotenv import load_dotenv
import os
from pathlib import Path
import asyncio
from typing import List
from pydantic import BaseModel

# 環境変数のロード
load_dotenv()

# ブラウザ設定
browser = Browser(
    config=BrowserConfig(
        chrome_instance_path='chromeのpathを記入'
    )
)

# コントローラの初期化
controller = Controller()

# プロンプトを読み込む関数
def load_prompt(file_path):
    with Path(file_path).open('r', encoding='utf-8') as file:
        return file.read()

# 出力を保存するためのモデル定義
class Model(BaseModel):
    title: str
    url: str
    likes: int
    license: str

class Models(BaseModel):
    models: List[Model]

@controller.action('Save models', param_model=Models)
def save_models(params: Models):
    with open('models.txt', 'a') as f:
        for model in params.models:
            f.write(f'{model.title} ({model.url}): {model.likes} likes, {model.license}\n')

# エージェントのメイン処理
async def main():
    # エージェントの初期化
    agent = Agent(
        task="",  # 初期タスクは空で設定
        llm=ChatOpenAI(model="gpt-4o"),
        controller=controller,
        # browser=browser
    )

    # タスク1の実行
    task1_content = load_prompt('C:\Develop\Browser Use\Pronpt\salesforce_operate_pronpt.txt')
    agent.task = task1_content
    result1 = await agent.run()
    print("タスク1の結果:", result1)

    # タスク2の実行
    task2_content = load_prompt('C:\Develop\Browser Use\Pronpt\X_serch_LLMInfo_summary_Pronpt.txt')
    agent.task = task2_content
    result2 = await agent.run()
    print("タスク2の結果:", result2)

# 非同期処理の実行
if __name__ == "__main__":
    asyncio.run(main())
