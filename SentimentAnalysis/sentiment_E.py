import os
from transformers import pipeline

# 忽略符号链接警告（可选）
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

# 显式指定模型和版本
model_name = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"
revision = "714eb0f"

# 初始化管道
classifier = pipeline(
    task="sentiment-analysis",
    model=model_name,
    revision=revision,
    framework="pt"
)

# 测试推理
texts = [
    "Cheng Zhiqiang is extremely capable.",
    "Cheng Zhiqiang doesn't seem as capable as before.",
    "Cheng Zhiqiang is okay."
]
results = classifier(texts)

for text, result in zip(texts, results):
    print(f"文本: {text}")
    print(f"情感: {result['label']} (置信度: {result['score']:.4f})\n")