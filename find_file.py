import os

def find_file(filename, search_path):
  """
  在给定路径中查找文件。

  Args:
    filename: 要查找的文件的名称。
    search_path: 开始搜索的目录。

  Returns:
    如果找到文件，则返回文件的绝对路径，否则返回 None。
  """
  for root, dirs, files in os.walk(search_path):
    if filename in files:
      return os.path.abspath(os.path.join(root, filename))
  return None

if __name__ == "__main__":
  filename = input("请输入要查找的文件名: ")
  search_directory = input("请输入要搜索的目录 (留空则为当前目录): ") or "."

  # 处理用户输入的路径中可能存在的波浪号（~）
  search_directory = os.path.expanduser(search_directory)

  if not os.path.isdir(search_directory):
    print(f"错误：目录 '{search_directory}' 不存在。")
  else:
    file_path = find_file(filename, search_directory)

    if file_path:
      print(f"文件找到，路径为: {file_path}")
    else:
      print(f"在 '{search_directory}' 中未找到文件 '{filename}'。")
