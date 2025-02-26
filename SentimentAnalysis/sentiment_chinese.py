from transformers import pipeline
import os

# 忽略符号链接警告
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

# 中文情感分析模型（推荐以下任选其一）
models = [
    "IDEA-CCNL/Erlangshen-Roberta-110M-Sentiment",  # 深度求索中文情感模型
    "uer/roberta-base-finetuned-jd-binary-chinese",  # 京东评论二分类
    "nlptown/bert-base-multilingual-uncased-sentiment"  # 多语言通用模型
]

# 初始化中文情感分析管道
classifier = pipeline(
    task="sentiment-analysis",
    model=models[0],  # 优先使用Erlangshen中文模型
    framework="pt"
)

# 测试中文文本
texts = [
    "小猫抓老鼠非常厉害",
    "小猫抓老鼠非常厉害不像过去厉害了",
    "小猫最近表现一般般"
]

results = classifier(texts)

for text, result in zip(texts, results):
    print(f"文本: {text}")
    print(f"情感: {result['label']} (置信度: {result['score']:.4f})\n")