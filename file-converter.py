import sys
import markdown

if len(sys.argv) != 4:
    print("Usage: python3 file-converter.py markdown <inputpath> <outputpath>")
    sys.exit(1)
command = sys.argv[1]
inputpath = sys.argv[2]
outputpath = sys.argv[3]

if command != 'markdown':
    print('正しいコマンドを入力してください')
    sys.exit(1)

try:
  with open(inputpath, "r", encoding="utf-8") as input_file:
      text = input_file.read()
  html = markdown.markdown(text)

  with open(outputpath, "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
      output_file.write(html)
  print(f"変換が完了: {outputpath}")

except Exception as e:
  print(f"エラー： {e}")
  sys.exit(1)