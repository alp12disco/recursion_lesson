import sys

# file読み込み処理
def read_file(path):
  try:
    with open(path, "r") as f:
      return f.read()
  except FileNotFoundError:
    print(f'ファイルが存在しません: {path}')
    sys.exit(1)

# file書き込み処理
def write_file(path, content, mode="w"):
  with open(path, mode) as f:
    f.write(content)

# 以下、各コマンドについての処理
def reverse_command(args):
  if len(args) != 2:
    print("使用法: reverse <inputpath> <outputpath>")
    # エラーとして終了
    sys.exit(1)
  inputpath, outputpath = args
  original_str = read_file(inputpath)
  reversed_str = original_str[::-1]
  write_file(outputpath, reversed_str)
  print(f'内容を逆順にして {outputpath} に保存しました')
  
def copy_command(args):
  if len(args) != 2:
    print("使用法: copy <inputpath> <outputpath>")
    sys.exit(1)
  inputpath, outputpath = args
  original_str = read_file(inputpath)
  write_file(outputpath, original_str)
  print(f'{inputpath} の内容を {outputpath} にコピーしました')
  
def duplicate_contents_command(args):
  if len(args) != 2:
    print('使用法: deuplicate-contents <inputpath> <n>')
    sys.exit(1)
  inputpath, n_str = args
  try:
    n = int(n_str)
  except ValueError:
    print('n には数値を入力してください')
    sys.exit(1)
  original_str = read_file(inputpath)
  # appendモードで書き込み
  write_file(inputpath, original_str * n, mode="a")
  print(f'{inputpath} の内容を {n} 回複製しました')
  
def replace_string_command(args):
  if len(args) != 3:
    print("使用法: replace-string <inputpath> <needle> <newstring>")
    sys.exit(1)
  inputpath, needle, newstring = args
  original_str = read_file(inputpath)
  replaced_str = original_str.replace(needle, newstring)
  write_file(inputpath, replaced_str)
  print(f'{inputpath} 内の {needle} を {newstring} に置換しました')
  
def main():
  if len(sys.argv) < 2:
    print("コマンドを指定してください")
    sys.exit(1)
  command = sys.argv[1]
  args = sys.argv[2:]
	
  commands = {
    'reverse': reverse_command,
    'copy': copy_command,
    'duplicate-contents': duplicate_contents_command,
    'replace-string': replace_string_command,
	}
  
  if command in commands:
    commands[command](args)
  else:
    print('正しいコマンドを入力してください')
    
if __name__ == '__main__':
  main()

    
	
