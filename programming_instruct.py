import json
import openai
from typing import List, Dict

class ProgrammingInstructor:
    def __init__(self, api_key: str):
        self.api_key = api_key
        openai.api_key = api_key
        
        # 初始种子任务
        self.seed_tasks = [
            {
                "instruction": "解释什么是递归函数,并给出一个简单的例子",
                "input": "",
                "output": "递归函数是一个调用自身的函数。例如计算阶乘:\ndef factorial(n):\n    if n <= 1:\n        return 1\n    return n * factorial(n-1)"
            },
            {
                "instruction": "说明如何优化代码性能",
                "input": "",  
                "output": "1. 使用适当的数据结构\n2. 避免重复计算\n3. 使用缓存\n4. 减少循环中的操作"
            }
        ]

    def generate_instruction(self, existing_tasks: List[Dict]) -> Dict:
        """生成新的编程相关指令"""
        prompt = self._create_prompt(existing_tasks)
        
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "你是一个编程教师,负责生成高质量的编程相关指令。"},
                {"role": "user", "content": prompt}
            ]
        )
        
        # 解析响应生成新任务
        new_task = self._parse_response(response.choices[0].message.content)
        return new_task

    def _create_prompt(self, existing_tasks: List[Dict]) -> str:
        """创建提示模板"""
        prompt = """请基于以下已有的编程指令示例,生成一个新的编程相关指令:

现有指令示例:
{examples}

生成的新指令需要:
1. 涉及具体的编程概念或技巧
2. 清晰且实用
3. 与已有指令不重复
4. 包含指令描述、输入(可选)和期望输出

请按以下格式生成:
{
    "instruction": "指令描述",
    "input": "输入(如果需要)",
    "output": "期望输出"
}
"""
        # 格式化示例
        examples = "\n".join([json.dumps(task, indent=2, ensure_ascii=False) 
                            for task in existing_tasks[-2:]])
        return prompt.format(examples=examples)

    def _parse_response(self, response: str) -> Dict:
        """解析API响应"""
        try:
            return json.loads(response)
        except:
            # 简单的错误处理
            return {
                "instruction": "解析失败",
                "input": "",
                "output": ""
            }

    def generate_dataset(self, num_instructions: int) -> List[Dict]:
        """生成指令数据集"""
        dataset = self.seed_tasks.copy()
        
        for _ in range(num_instructions):
            new_task = self.generate_instruction(dataset)
            dataset.append(new_task)
            
        return dataset

    def save_dataset(self, dataset: List[Dict], filename: str):
        """保存数据集到文件"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(dataset, f, indent=2, ensure_ascii=False)

    def interactive_mode(self):
        """交互模式"""
        print("欢迎使用编程指令生成器！")
        while True:
            print("\n请选择操作：")
            print("1. 生成新的指令集")
            print("2. 查看现有种子任务")
            print("3. 退出")
            
            choice = input("请输入选项（1-3）: ")
            
            if choice == "1":
                try:
                    num = int(input("请输入要生成的指令数量: "))
                    filename = input("请输入保存的文件名(如 instructions.json): ")
                    
                    print("\n正在生成指令...")
                    dataset = self.generate_dataset(num)
                    self.save_dataset(dataset, filename)
                    
                    print(f"\n成功生成 {num} 条指令并保存到 {filename}")
                    
                    # 打印生成的指令
                    for i, task in enumerate(dataset, 1):
                        print(f"\n指令 {i}:")
                        print(f"Instruction: {task['instruction']}")
                        print(f"Input: {task['input']}")
                        print(f"Output: {task['output']}")
                        
                except ValueError:
                    print("请输入有效的数字！")
                    
            elif choice == "2":
                print("\n现有种子任务：")
                for i, task in enumerate(self.seed_tasks, 1):
                    print(f"\n种子任务 {i}:")
                    print(f"Instruction: {task['instruction']}")
                    print(f"Input: {task['input']}")
                    print(f"Output: {task['output']}")
                    
            elif choice == "3":
                print("感谢使用！再见！")
                break
            else:
                print("无效的选项，请重新选择！")

if __name__ == "__main__":
    api_key = input("请输入您的 OpenAI API key: ")
    instructor = ProgrammingInstructor(api_key)
    instructor.interactive_mode() 