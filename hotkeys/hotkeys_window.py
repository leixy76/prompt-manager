import tkinter as tk
from tkinter import ttk, messagebox
import os

class HotkeysWindow:
    def __init__(self, parent, data_manager):
        self.window = tk.Toplevel(parent)
        self.window.title("独立专属快捷键配置")
        self.data_manager = data_manager
        
        self.setup_ui()
        self.load_data()
        
    def setup_ui(self):
        """设置UI界面"""
        # 提示词列表框架
        frame = ttk.Frame(self.window)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 提示词列表标签
        label = ttk.Label(frame, text="带快捷键的提示词列表")
        label.pack(pady=5)
        
        # 提示词列表
        self.prompt_list = tk.Listbox(frame, width=80, height=20)
        self.prompt_list.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # 添加滚动条
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.prompt_list.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.prompt_list.config(yscrollcommand=scrollbar.set)
        
        # 添加“清空hotkey”按钮
        clear_button = ttk.Button(frame, text="清空hotkey", command=self.clear_hotkeys)
        clear_button.pack(pady=10)
        
    def load_data(self):
        """加载数据"""
        hotkeys_prompts = self.data_manager.get_hotkeys_prompts()
        for prompt in hotkeys_prompts:
            # 排除带有“ctrl+*”的快捷键
            if prompt.get('shortcut', '') != "ctrl+*":
                self.prompt_list.insert(tk.END, f"{prompt['name']} ({prompt['shortcut']})")
                
    def clear_hotkeys(self):
        """清空所有 JSON 数据的 shortcut 字段"""
        if messagebox.askyesno("确认清空", "确定要清空所有快捷键吗？此操作不可恢复！"):
            self.data_manager.clear_all_hotkeys()
            self.prompt_list.delete(0, tk.END)  # 清空列表
            messagebox.showinfo("清空完成", "所有快捷键已清空。")