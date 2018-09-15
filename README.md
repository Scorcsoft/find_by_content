# find_by_content
通过文件内容查找文件的工具

# 用法
python findbc.py path [OPTIONS]

## 查找路径
第一个参数必须为路径

## -k
必选参数，指定关键字，例如在当前目录查找内容中包含字符串scorcsoft的文件:
```
python findbc.py ./ -k scorcsoft
```

## -t
可选参数，指定多种文件类型，例如在当前目录查找内容中包含字符串scorcsoft的txt和php文件:
```
python findbc.py ./ -k scorcsoft -t php,txt
```

## -o
可选参数，将结果写入到指定文件，例如在当前目录查找内容中包含字符串scorcsoft文件，并且把结果保存在result.txt中:
```
python findbc.py ./ -k scorcsoft -o result.txt
```

## 长参数
可选参数，指定单一文件类型，例如在当前目录查找内容中包含字符串scorcsoft的php文件:
```
python findbc.py ./ -k scorcsoft --php
```

在当前目录查找内容中包含字符串scorcsoft的html文件:
```
python findbc.py ./ -k scorcsoft --html
```

## 注意事项：
如果目录、参数值中存在空格，那么应该用引号括起来，例如：
```
python findbc.py "./te st" -k "scorc soft" -o "res ult.txt"
```
