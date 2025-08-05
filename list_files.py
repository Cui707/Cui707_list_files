import os
import msvcrt

def list_files_in_directory():
    """
    遍历脚本所在目录中除脚本本身之外的全部文件名称。
    """
    # 获取当前脚本的绝对路径
    script_path = os.path.abspath(__file__)
    # 获取当前脚本所在的目录
    directory = os.path.dirname(script_path)
    # 获取脚本自身的名称
    script_name = os.path.basename(script_path)

    print(f"当前目录: {directory}")
    print("--------------------")
    print("该目录下的文件（不包含脚本本身）:")
    print("--------------------")

    # 遍历目录中的所有文件和文件夹
    for filename in os.listdir(directory):
        # 排除脚本本身
        if filename != script_name:
            print(filename)

# 执行函数
if __name__ == "__main__":
    list_files_in_directory()
    
    # 这一部分是新添加的，用于在Windows上保持窗口打开
    print("\n按任意键退出...")
    msvcrt.getch()