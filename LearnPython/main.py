import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import akshare as ak

# 获取小米科技公司（1810.HK）的股票数据
df = ak.stock_hk_hist(symbol="01810", period="daily", start_date="20150101", end_date="20250101")
# 对数据进行简单处理，调整列名和索引
df = df.rename(columns={'日期': 'Date', '收盘': 'Close', '开盘': 'Open', '最高': 'High', '最低': 'Low', '成交量': 'Volume'})
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

# 查看数据前5行
print(df.head())

# 用Pandas描述性统计
print(df.describe())

# 检查缺失值
print(df.isnull().sum())

# 删除缺失值（如果有）
df = df.dropna()

# 提取关键列：收盘价（Close）
close_prices = df['Close'].values  # 转为NumPy数组

# 计算30日和60日移动平均线
df['MA30'] = df['Close'].rolling(window=30).mean()
df['MA60'] = df['Close'].rolling(window=60).mean()

# 计算每日收益率
df['Daily Return'] = df['Close'].pct_change()

# 计算年化波动性
volatility = np.std(df['Daily Return'].dropna()) * np.sqrt(252)  # 年化波动率
print(f"Annualized Volatility: {volatility:.2%}")

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 可以根据系统情况替换为其他支持中文的字体
# 解决负号显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False

# 第一个图形：价格走势与技术指标
plt.figure(figsize=(14, 6))
plt.plot(df.index, df['Close'], label='收盘价', alpha=0.5)
plt.plot(df.index, df['MA30'], label='30日移动平均线', color='orange')
plt.plot(df.index, df['MA60'], label='60日移动平均线', color='red')
plt.title('小米股票10年价格与移动平均线（2015 - 2025）')
plt.xlabel('日期')
plt.ylabel('价格（港元）')
plt.legend()
plt.grid(True)

# 创建新的图形窗口
plt.figure(figsize=(10, 6))

# 第二个图形：收益率的分布
plt.hist(df['Daily Return'].dropna(), bins=50, color='blue', alpha=0.7)
plt.title('每日收益率分布')
plt.xlabel('每日收益率')
plt.ylabel('频次')

# 显示所有图形
plt.show()

# 保存处理后的数据
df.to_csv('1810_HK.csv')