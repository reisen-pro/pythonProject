"""
Matplotlib 基础练习
===================
Matplotlib = Python 最基础的可视化库，把数据变成图表。

核心概念：
- figure：画布（一整张纸）
- axes：坐标轴（纸上的作图区域，一张纸可以有多个图）
- plot / bar / scatter：折线图 / 柱状图 / 散点图

为什么要学可视化？
→ AI 训练完要看 loss 曲线、要看数据分布、要看模型效果
→ 面试时画图展示你的分析结论，比干巴巴的数字有说服力10倍
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# 设置中文字体（Windows 上显示中文必须设置）
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "KaiTi"]
plt.rcParams["axes.unicode_minus"] = False  # 负号显示正常

# 如果上面字体找不到，用这个兜底方案
try:
    plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
    plt.figure()  # 初始化一次
except:
    pass

# ============================================================
# 数据准备：读取之前的学生成绩数据
# ============================================================
csv_path = os.path.join(os.path.dirname(__file__), "students.csv")
if not os.path.exists(csv_path):
    # 如果没有，去找上节课创建的
    alt_path = os.path.join(os.path.dirname(__file__), "..", "ml", "students.csv")
    if os.path.exists(alt_path):
        csv_path = alt_path

# 确保文件存在
if not os.path.exists(csv_path):
    students_data = {
        "姓名": ["张三", "李四", "王五", "赵六", "陈七", "周八", "吴九", "郑十",
                 "孙一", "钱二", "刘三", "杨四", "朱六", "吴七", "许八"],
        "数学": [85, 92, 78, 90, 88, 73, 95, 81, 77, 84, 91, 68, 79, 86, 93],
        "语文": [88, 76, 95, 82, 90, 85, 78, 92, 83, 79, 88, 74, 96, 81, 77],
        "英语": [90, 83, 88, 85, 92, 80, 91, 87, 79, 85, 90, 72, 88, 84, 89],
        "班级": ["A", "B", "A", "C", "B", "A", "B", "C", "A", "C", "B", "A", "C", "B", "A"],
        "性别": ["男", "女", "男", "女", "男", "女", "男", "女", "男", "女", "男", "女", "男", "女", "男"]
    }
    df = pd.DataFrame(students_data)
    df.to_csv(csv_path, index=False, encoding="utf-8-sig")
else:
    df = pd.read_csv(csv_path)

df["总分"] = df["数学"] + df["语文"] + df["英语"]
print("数据读取成功，共", len(df), "条记录")
print(df.head())


# ============================================================
# 第1题：最简单的折线图
# ============================================================
# 理解 figure（画布）和 plot（画线）的关系

print("\n" + "=" * 50)
print("第1题：最简单的折线图")
print("=" * 50)

x = np.array([1, 2, 3, 4, 5])          # x 轴：第1-5次作业
y = np.array([60, 72, 68, 85, 90])     # y 轴：成绩

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, y, marker="o", color="#1f77b4", linewidth=2, markersize=8)
ax.set_title("成绩进步折线图", fontsize=16, fontweight="bold")
ax.set_xlabel("第几次作业", fontsize=12)
ax.set_ylabel("成绩", fontsize=12)
ax.set_xticks(x)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(os.path.dirname(__file__), "chart_01_line.png"), dpi=150)
print("[已保存] chart_01_line.png")
plt.close()


# ============================================================
# 第2题：柱状图 — 各科目平均分对比
# ============================================================
# bar = 柱子有多高，数据有多直观

print("\n" + "=" * 50)
print("第2题：柱状图")
print("=" * 50)

subjects = ["数学", "语文", "英语"]
class_a = df[df["班级"] == "A"][["数学", "语文", "英语"]].mean()
class_b = df[df["班级"] == "B"][["数学", "语文", "英语"]].mean()
class_c = df[df["班级"] == "C"][["数学", "语文", "英语"]].mean()

x_pos = np.arange(len(subjects))
width = 0.25

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(x_pos - width, class_a, width, label="A班", color="#ff7f0e")
ax.bar(x_pos,       class_b, width, label="B班", color="#1f77b4")
ax.bar(x_pos + width, class_c, width, label="C班", color="#2ca02c")

ax.set_xlabel("科目", fontsize=12)
ax.set_ylabel("平均分", fontsize=12)
ax.set_title("各班级各科目平均分对比", fontsize=16, fontweight="bold")
ax.set_xticks(x_pos)
ax.set_xticklabels(subjects)
ax.legend()
ax.set_ylim(75, 95)  # y 轴范围，让差异更明显
ax.grid(axis="y", alpha=0.3)

# 在柱子上标数值
for bar_group in [ax.bar(x_pos - width, class_a, width),
                  ax.bar(x_pos, class_b, width),
                  ax.bar(x_pos + width, class_c, width)]:
    for bar in bar_group:
        height = bar.get_height()
        ax.annotate(f"{height:.1f}",
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha="center", va="bottom", fontsize=9)

plt.tight_layout()
plt.savefig(os.path.join(os.path.dirname(__file__), "chart_02_bar.png"), dpi=150)
print("[已保存] chart_02_bar.png")
plt.close()


# ============================================================
# 第3题：直方图 — 成绩分布
# ============================================================
# hist = 看数据"扎堆"在哪里，帮你发现规律

print("\n" + "=" * 50)
print("第3题：直方图（成绩分布）")
print("=" * 50)

scores = df["总分"]

fig, ax = plt.subplots(figsize=(10, 6))
n, bins, patches = ax.hist(scores, bins=6, color="#9467bd",
                            edgecolor="white", linewidth=1.2)

# 给不同区间的柱子染不同颜色（低分红色，高分绿色）
for i, patch in enumerate(patches):
    bin_center = (bins[i] + bins[i+1]) / 2
    if bin_center < scores.median() - 20:
        patch.set_facecolor("#e74c3c")
    elif bin_center > scores.median() + 20:
        patch.set_facecolor("#27ae60")
    else:
        patch.set_facecolor("#3498db")

ax.set_xlabel("总分", fontsize=12)
ax.set_ylabel("人数", fontsize=12)
ax.set_title("全班总分分布直方图", fontsize=16, fontweight="bold")
ax.axvline(scores.mean(), color="red", linestyle="--",
           linewidth=2, label=f"平均分: {scores.mean():.1f}")
ax.axvline(scores.median(), color="orange", linestyle="--",
           linewidth=2, label=f"中位数: {scores.median():.1f}")
ax.legend()
ax.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(os.path.dirname(__file__), "chart_03_hist.png"), dpi=150)
print("[已保存] chart_03_hist.png")
plt.close()


# ============================================================
# 第4题：散点图 — 两门成绩的关系
# ============================================================
# scatter = 看两个变量之间有没有关联（相关性）

print("\n" + "=" * 50)
print("第4题：散点图")
print("=" * 50)

math_scores = df["数学"]
chinese_scores = df["语文"]
total_scores = df["总分"]

fig, ax = plt.subplots(figsize=(10, 7))
scatter = ax.scatter(math_scores, chinese_scores,
                     c=total_scores, cmap="RdYlGn",
                     s=120, alpha=0.8, edgecolors="white", linewidth=1)

# 加颜色条
cbar = plt.colorbar(scatter)
cbar.set_label("总分", fontsize=11)

# 给每个点标注姓名
for i, name in enumerate(df["姓名"]):
    ax.annotate(name, (math_scores.iloc[i], chinese_scores.iloc[i]),
                xytext=(5, 5), textcoords="offset points", fontsize=9)

ax.set_xlabel("数学成绩", fontsize=12)
ax.set_ylabel("语文成绩", fontsize=12)
ax.set_title("数学 vs 语文成绩散点图（颜色=总分）", fontsize=16, fontweight="bold")
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(os.path.dirname(__file__), "chart_04_scatter.png"), dpi=150)
print("[已保存] chart_04_scatter.png")
plt.close()


# ============================================================
# 第5题：饼图 — 班级人数占比
# ============================================================
# pie = 看整体中各部分占多少（适合展示比例）

print("\n" + "=" * 50)
print("第5题：饼图")
print("=" * 50)

class_counts = df["班级"].value_counts().sort_index()
labels = [f"{cls}班 ({count}人)" for cls, count in class_counts.items()]
sizes = class_counts.values
colors = ["#ff7f0e", "#1f77b4", "#2ca02c"]
explode = (0.05, 0, 0)  # 把 A班 稍微突出一点

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(sizes, labels=labels, colors=colors, explode=explode,
       autopct="%1.1f%%", startangle=90,
       textprops={"fontsize": 13},
       wedgeprops={"edgecolor": "white", "linewidth": 2})
ax.set_title("班级人数占比", fontsize=16, fontweight="bold", y=1.02)

plt.tight_layout()
plt.savefig(os.path.join(os.path.dirname(__file__), "chart_05_pie.png"), dpi=150)
print("[已保存] chart_05_pie.png")
plt.close()


# ============================================================
# 第6题：综合图 — 一张图放多个子图
# ============================================================
# subplot = 把多张图放进一张大图里，便于对比

print("\n" + "=" * 50)
print("第6题：综合子图")
print("=" * 50)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("学生成绩综合分析", fontsize=18, fontweight="bold", y=1.02)

# 子图1：总分排名 TOP 5
ax1 = axes[0, 0]
top5 = df.sort_values("总分", ascending=False).head(5)
bars = ax1.barh(top5["姓名"], top5["总分"], color="#3498db")
ax1.set_xlabel("总分")
ax1.set_title("总分 TOP 5", fontsize=13)
ax1.invert_yaxis()  # 最高的在顶部
for bar, score in zip(bars, top5["总分"]):
    ax1.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
             str(score), va="center", fontsize=10)

# 子图2：各科目箱线图（看成绩分布范围）
ax2 = axes[0, 1]
bp = ax2.boxplot([df["数学"], df["语文"], df["英语"]],
                  labels=["数学", "语文", "英语"],
                  patch_artist=True)
colors_box = ["#e74c3c", "#27ae60", "#3498db"]
for patch, color in zip(bp["boxes"], colors_box):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)
ax2.set_ylabel("成绩")
ax2.set_title("各科目成绩分布（箱线图）", fontsize=13)
ax2.grid(axis="y", alpha=0.3)

# 子图3：各班总分箱线图
ax3 = axes[1, 0]
class_a_scores = df[df["班级"] == "A"]["总分"]
class_b_scores = df[df["班级"] == "B"]["总分"]
class_c_scores = df[df["班级"] == "C"]["总分"]
bp2 = ax3.boxplot([class_a_scores, class_b_scores, class_c_scores],
                   labels=["A班", "B班", "C班"],
                   patch_artist=True)
colors_box2 = ["#ff7f0e", "#1f77b4", "#2ca02c"]
for patch, color in zip(bp2["boxes"], colors_box2):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)
ax3.set_ylabel("总分")
ax3.set_title("各班总分分布", fontsize=13)
ax3.grid(axis="y", alpha=0.3)

# 子图4：相关性热力图（各科目相关性）
ax4 = axes[1, 1]
corr = df[["数学", "语文", "英语", "总分"]].corr()
im = ax4.imshow(corr, cmap="RdYlBu", aspect="auto", vmin=-1, vmax=1)
ax4.set_xticks(range(4))
ax4.set_yticks(range(4))
ax4.set_xticklabels(["数学", "语文", "英语", "总分"], fontsize=10)
ax4.set_yticklabels(["数学", "语文", "英语", "总分"], fontsize=10)
ax4.set_title("科目相关性热力图", fontsize=13)

# 在格子里填数字
for i in range(4):
    for j in range(4):
        ax4.text(j, i, f"{corr.iloc[i, j]:.2f}",
                 ha="center", va="center", fontsize=11,
                 color="white" if abs(corr.iloc[i, j]) > 0.5 else "black")

plt.colorbar(im, ax=ax4, label="相关系数")
plt.tight_layout()
plt.savefig(os.path.join(os.path.dirname(__file__), "chart_06_combo.png"), dpi=150)
print("[已保存] chart_06_combo.png")
plt.close()

print("\n✅ 全部6张图已生成！去 ml/ 文件夹里看效果吧。")
print("打开方式：在文件管理器里双击打开 png 文件，或者用 VS Code 预览。")


# ============================================================
# 思考题
# ============================================================
"""
1. 对比六种图（折线图、柱状图、直方图、散点图、饼图、箱线图），
   什么场景下用哪种？
   （提示：从"展示什么关系"来分类）
折线图:看趋势,看变化
柱状图:做对比
直方图:看分布
散点图:看关系
饼图:看占比
箱线图:大杂烩。把多张小图拼在一张大图里，显得非常专业。

2. 第4题散点图里，为什么用 c=total_scores 涂颜色？
   不涂颜色的话，散点图还能说明什么？
c=total_scores涂颜色,可以从颜色的深浅程度,来了解这个人的总分是高还是低
不涂颜色的话,散点图可以比较直观的观察到,是偏上,还是偏右,查看偏科
查看总分高/低情况,中间情况,能够直观了解到那些人是综合好,综合成绩差一点,还是居中,还是偏科

3. 第6题热力图中，"相关系数"接近 1 或 -1 是什么意思？
   相关性高的两门课，对学习有什么启示？
越接近1表示两者的关联性越高
越接近-1表示两者几乎没什么关联性
相关性高的两门课,从结果上推断,可以认为学习功课A好,学习功课B也好
也可能说明这个班级的学生逻辑思维/智力水平/学习能力强，或者他们花在理科/文科上的时间普遍较多。

做完发给我看！
"""
