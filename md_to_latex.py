import pypandoc
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

def convert_md_to_latex(md_content):
    """
    Converts a Markdown string to a LaTeX string.
    """
    try:
        # Check if pandoc is installed
        pypandoc.get_pandoc_version()
    except OSError:
        messagebox.showerror("错误", "Pandoc 未安装。请先安装 Pandoc。")
        return None

    try:
        # Add extra pandoc arguments to handle Chinese characters with xeCJK
        extra_args = ['--pdf-engine=xelatex', '-V', 'mainfont=SimSun']
        output = pypandoc.convert_text(md_content, 'latex', format='md', extra_args=extra_args)
        return output
    except Exception as e:
        messagebox.showerror("转换错误", f"转换过程中发生错误: {e}")
        return None

class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Markdown 到 LaTeX 转换器")
        self.root.geometry("800x600")

        # Main frame
        main_frame = tk.Frame(root)
        main_frame.pack(pady=10, padx=10, fill="both", expand=True)

        # Input text area
        input_label = tk.Label(main_frame, text="Markdown 输入:")
        input_label.pack(anchor="w")
        self.input_text = scrolledtext.ScrolledText(main_frame, height=10, wrap=tk.WORD)
        self.input_text.pack(fill="both", expand=True)

        # Output text area
        output_label = tk.Label(main_frame, text="LaTeX 输出:")
        output_label.pack(anchor="w", pady=(10, 0))
        self.output_text = scrolledtext.ScrolledText(main_frame, height=10, wrap=tk.WORD)
        self.output_text.pack(fill="both", expand=True)

        # Buttons frame
        buttons_frame = tk.Frame(root)
        buttons_frame.pack(pady=10)

        self.open_button = tk.Button(buttons_frame, text="打开文件", command=self.open_file)
        self.open_button.pack(side="left", padx=5)

        self.convert_button = tk.Button(buttons_frame, text="转换", command=self.convert)
        self.convert_button.pack(side="left", padx=5)

        self.save_button = tk.Button(buttons_frame, text="导出为...", command=self.save_file)
        self.save_button.pack(side="left", padx=5)

    def open_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Markdown 文件", "*.md"), ("所有文件", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                self.input_text.delete('1.0', tk.END)
                self.input_text.insert('1.0', content)
            except Exception as e:
                messagebox.showerror("文件读取错误", f"无法读取文件: {e}")

    def convert(self):
        md_content = self.input_text.get("1.0", tk.END)
        if not md_content.strip():
            messagebox.showwarning("警告", "输入内容为空。")
            return
        
        latex_output = convert_md_to_latex(md_content)
        
        if latex_output:
            self.output_text.delete('1.0', tk.END)
            self.output_text.insert('1.0', latex_output)

    def save_file(self):
        latex_content = self.output_text.get("1.0", tk.END)
        if not latex_content.strip():
            messagebox.showwarning("警告", "没有可导出的内容。")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".tex",
            filetypes=[("LaTeX 文件", "*.tex"), ("所有文件", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(latex_content)
                messagebox.showinfo("成功", f"文件已成功保存到:\n{file_path}")
            except Exception as e:
                messagebox.showerror("保存错误", f"无法保存文件: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ConverterApp(root)
    root.mainloop()
