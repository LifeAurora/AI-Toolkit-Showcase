#AI 辅助生成代码示例
import openai

# 配置你的 OpenAI API Key
openai.api_key = "YOUR_API_KEY"

# 提示词示例：生成 Python 处理 CSV 的函数
prompt = """
请生成一个 Python 函数，能够读取 CSV 文件，计算每列的平均值，并返回字典结果。
"""

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}]
)

# 输出生成的代码
generated_code = response['choices'][0]['message']['content']
print("=== AI 生成的代码 ===\n")
print(generated_code)

# 保存为本地文件
with open("../../assets/automation-scripts/ai_script.py", "w", encoding="utf-8") as f:
    f.write(generated_code)

print("\nAI 生成代码已保存！")
