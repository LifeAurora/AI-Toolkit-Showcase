# 数据分析与报表生成
import pandas as pd
import matplotlib.pyplot as plt

# 模拟数据
data = {
    "学生": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "数学": [88, 92, 79, 85, 90],
    "英语": [95, 85, 88, 90, 92],
    "物理": [80, 87, 85, 88, 91]
}

df = pd.DataFrame(data)

# 生成成绩总分列
df["总分"] = df["数学"] + df["英语"] + df["物理"]

# 导出 Excel
df.to_excel("score_report.xlsx", index=False)

# 绘制柱状图
df.set_index("学生")[["数学", "英语", "物理"]].plot(kind="bar", figsize=(8,6))
plt.title("学生成绩分布")
plt.ylabel("分数")
plt.savefig("../../assets/automation-scripts/data_analysis.png")
plt.show()

print("数据分析完成，Excel 和图表已生成！")
