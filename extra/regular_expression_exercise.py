import re

match_str1 = "aeeee apple ape agree age amaze animate advertise a\ne a&e a@e a6e a9e a,e aAe Aae"

''' 通配符 . '''
# . 通配符 - 匹配1个除了换行符\n以外的任何符号
# res = re.findall(r"a.e", match_str1)  # ['aee', 'ape', 'age', 'aze', 'ate', 'a&e', 'a@e', 'a6e', 'a9e', 'a,e', 'aAe']

# res = re.findall(r"a...e", match_str1)  # ['aeeee', 'apple', 'agree', 'amaze']

''' 字符集 [] '''
# [] 字符集 - 匹配1个在字符集限定范围内的符号
# res = re.findall(r"a[0-9]e", match_str1)  # ['a6e', 'a9e']

# ^ 在字符集中 - 取反
# res = re.findall(r"a[^0-9]e", match_str1)  # ['aee', 'ape', 'age', 'aze', 'ate', 'a&e', 'a@e', 'a6e', 'a9e', 'a,e', 'aAe']

# res = re.findall(r"a[a-z]e", match_str1)  # ['aee', 'ape', 'age', 'aze', 'ate']

# res = re.findall(r"a[a-zA-Z]e", match_str1)  # ['aee', 'ape', 'age', 'aze', 'ate', 'aAe']

# p , g
# res = re.findall(r"a[p,g]e", match_str1)  # ['ape', 'age', 'a,e']

''' 重复元字符 {} * + ? '''
# {} 数量范围贪婪符 - 指定左边原子的可以重复的数量范围
# res = re.findall(r"a.{3}e", match_str1)  # ['aeeee', 'apple', 'agree', 'amaze']

# 默认贪婪匹配: 优先按照最大匹配数进行匹配 - aeeee出现三种方式 aee 、 aeee 和 aeeee ,后者先进行匹配
# 1-3
# res = re.findall(r"a.{1,3}e", match_str)1  # ['aeeee', 'apple', 'ape', 'agree', 'age', 'amaze', 'ate', 'adve', 'a&e', 'a@e', 'a6e', 'a9e', 'a,e', 'aAe']

# 取消贪婪匹配:（优先按照最小匹配数进行匹配） 重复符号后面跟一个 ? - aeeee出现三种方式 aee 、 aeee 和 aeeee , 前者先进行匹配
# res = re.findall(r"a.{1,3}?e", match_str1)  # ['aee', 'apple', 'ape', 'agre', 'age', 'amaze', 'ate', 'adve', 'a&e', 'a@e', 'a6e', 'a9e', 'a,e', 'aAe']

# 2-无穷大
# res = re.findall(r"a.{2,}e", match_str1)  # ['aeeee apple ape agree age amaze animate advertise', 'a&e a@e a6e a9e a,e aAe Aae']

# 更改re模式 S - . 可匹配任意符号
# res = re.findall(r"a.{2,}e", match_str1, re.S)  # ['aeeee apple ape agree age amaze animate advertise a\ne a&e a@e a6e a9e a,e aAe Aae']

# res = re.findall(r"a[a-z]{1,3}e", match_str1)  # ['aeeee', 'apple', 'ape', 'agree', 'age', 'amaze', 'ate', 'adve']

# res = re.findall(r"a[^a-zA-Z\n]{1,3}e", match_str1)  # ['a&e', 'a@e', 'a6e', 'a9e', 'a,e']

# * 等同于{0,} - 指定左边原子出现0次或多次
# res = re.findall(r"a.*e", match_str1)  # ['aeeee apple ape agree age amaze animate advertise', 'a&e a@e a6e a9e a,e aAe Aae']

# res = re.findall(r"a.*?e", match_str1)  # ['ae', 'apple', 'ape', 'agre', 'age', 'amaze', 'animate', 'adve', 'a&e', 'a@e', 'a6e', 'a9e', 'a,e', 'aAe', 'ae']

# + 等同于{1,} - 指定左边原子出现1次或多次
# res = re.findall(r"a.+e", match_str1)  # ['aeeee apple ape agree age amaze animate advertise', 'a&e a@e a6e a9e a,e aAe Aae']

# res = re.findall(r"a.+?e", match_str1)  # ['aee', 'apple', 'ape', 'agre', 'age', 'amaze', 'animate', 'adve', 'a&e', 'a@e', 'a6e', 'a9e', 'a,e', 'aAe']

# ? 等同于{0,1} - 指定左边原子出现0次或1次
# res = re.findall(r"a.?e", match_str1)  # ['aee', 'ape', 'age', 'aze', 'ate', 'a&e', 'a@e', 'a6e', 'a9e', 'a,e', 'aAe', 'ae']

# 第一个 ? - 等同于{0,1} 先 1 后 0  第二个 ? - 取消贪婪 先 0 后 1
# res = re.findall(r"a.??e", match_str1)  # ['ae', 'ape', 'age', 'aze', 'ate', 'a&e', 'a@e', 'a6e', 'a9e', 'a,e', 'aAe', 'ae']

''' 边界符（锚点符） ^ $ '''
match_str2 = "23 yuan 56 dollar 71 Pound 9999 \n 999 \t 99 \n 9 cat cater lcat "
# ^ 开始边界符 - 匹配一行的开始位置
# $ 结束边界符 - 匹配一行的结束位置
path1 = "http://aaa/bbbb/cccc/yuan/blog/1990/12/xxx/yyy, https://www.baidu.com/, https://www.blog-Kk.com, https://www.jd.com, http://www.abc.com"
# path1 = "/yuan/blog/1990/12/"
# res = re.findall(r"^/yuan/blog/[0-9]{4}/[0-9]{1,2}/$", path1)  # [] | ['/yuan/blog/1990/12/']

''' 转义符 '''
# \d 匹配一个数字原子 - 等价于[0-9]
# res = re.findall(r"\d+", match_str2)  # ['23', '56', '71', '9999', '999']
# res = re.findall("\\d+", match_str2)  # ['23', '56', '71', '9999', '999']

# \D 匹配一个非数字原子 - 等价于[^0-9]
# res = re.findall(r"\D+", match_str2)  # [' yuan ', ' dollar ', ' Pound ', ' \n ', ' \t ', ' \n ', ' cat cater lcat ']

# \w 匹配一个包括下划线的单词原子 - 等价于[A-Za-z0-9_]
# res = re.findall(r"\w+", match_str2)  # ['23', 'yuan', '56', 'dollar', '71', 'Pound', '9999', '999', '99', '9', 'cat', 'cater', 'lcat']

# \W 匹配一个非单词原子 - 等价于[^A-Za-z0-9_]
# res = re.findall(r"\W+", match_str2)  # [' ', ' ', ' ', ' ', ' ', ' ', ' \n ', ' \t ', ' \n ', ' ', ' ', ' ', ' ']

# \n 匹配一个换行符
# res = re.findall(r"\n", match_str2)  # ['\n', '\n']

# \t 匹配一个制表符
# res = re.findall(r"\t", match_str2)  # ['\t']

# \s 匹配一个任意空白字符原子 - 空格符、制表符、换页符等
# res = re.findall(r"cat\s", match_str2)  # ['cat ', 'cat ']

# \S 匹配一个任意非空白字符原子
# res = re.findall(r"\S+", match_str2)  # ['23', 'yuan', '56', 'dollar', '71', 'Pound', '9999', '999', '99', '9', 'cat', 'cater', 'lcat']

# \b 匹配一个单词边界原子 - 单词和非单词原子间的位置
# res = re.findall(r".cat\b", match_str2)  # [' cat', 'lcat']

# \B 匹配一个非单词边界
# res = re.findall(r"\Bcat.\B", match_str2)  # ['cat ']

# 取消特殊功能符号以普通化 - 添加一个 \
# res = re.findall(r"https?://www\.[a-zA-Z0-9.%+-_]*?\.com", path1)  # ['https://www.baidu.com', 'https://www.blog-Kk.com', 'https://www.jd.com', 'http://www.abc.com']

''' 分组与优先提取 ()  - 整个 正则表达式 是规则, 不加 () 提取完整项, 提取文本加 () 符合规则进行优先提取 '''
# 分组
match_str3 = "apple banana peach orange aaa appleapple appleappleapple"
# res = re.findall("(apple){2,3}", match_str3)  # ['apple', 'apple']
# res = re.findall("(?:apple){2,3}", match_str3)  # ['appleapple', 'appleappleapple']

# 优先提取
path2 = "hahaha abc@163.com oho info@my163.com 666 info@163.cn yo xyz@163.cn"
# res = re.findall(r"\b[\w.-]+@\w*163\.com\b", path2)  # ['abc@163.com', 'info@my163.com']
# res = re.findall(r"\b([\w.-]+)@\w*163\.com\b", path2)  # ['abc', 'info']

''' 逻辑或 | '''
# 逻辑或
# res = re.findall(r"\b(apple|banana|peach)\b", match_str3)  # ['apple', 'banana', 'peach']
# 取消优先提取 (?: )
# res = re.findall(r"\b[\w.-]+@\w*163\.(?:com|cn)\b", path2)  # ['abc@163.com', 'info@my163.com', 'info@163.cn', 'xyz@163.cn']
# res = re.findall(r"\b([\w.-]+)@\w*163\.(?:com|cn)\b", path2)  # ['abc', 'info', 'info', 'xyz']

''' 常用函数 '''
match_str4 = "服务器 IP 地址如下:   \n主服务器: 192.168.1.1\n备用服务器:  10.0.0.5\n外部服务器: 172.16.254.1\n无效IP:256.100.50.25 和 192.168.1.256"
# re.findall(pattern, string, flags=0) - 查询文本中所有符合正则模式的匹配项, 以列表格式返回
# res = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
#                  match_str4)  # ['192.168.1.1', '10.0.0.5', '172.16.254.1', '256.100.50.25', '192.168.1.256']

# re.search(pattern, string, flags=0) - 查找任何位置首个符合正则模式的匹配项, 存在返回re.match对象, 不存在返回None
# res = re.search(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", match_str4)  # <re.Match object; span=(20, 31), match='192.168.1.1'>
# print(res.span())  # (20, 31)
# print(res.start())  # 20
# print(res.end())  # 31
# print(res.group())  # 192.168.1.1

# 有名分组
# res = re.search(r"外部服务器: \b(?P<outer_ip>(?:\d{1,3}\.){3}\d{1,3})\b",
#                 match_str4)  # <re.Match object; span=(48, 67), match='外部服务器: 172.16.254.1'>
# print(res.group("outer_ip"))  # 172.16.254.1

# re.compile(pattern, flags=0) - 编译正则表达式, 生成一个正则表达式对象, 可重用 - 封装规则
re_compile = re.compile(r"\b(?P<outer_ip>(?:\d{1,3}\.){3}\d{1,3})\b")
res = re_compile.findall(match_str4)  # ['192.168.1.1', '10.0.0.5', '172.16.254.1', '256.100.50.25', '192.168.1.256']
# for match in re_compile.finditer(match_str4):
#     print(match.group("outer_ip"))  # 192.168.1.1\n10.0.0.5\n172.16.254.1\n256.100.50.25\n192.168.1.256

# re.match(pattern,string,flags=0) - 判定字符串开始位置是否匹配正则模式的规则，成功返回re.Match对象, 不匹配返回None - 等同于search("^……")
# res = re.match(r"外部服务器: \b(?P<outer_ip>(?:\d{1,3}\.){3}\d{1,3})\b", match_str4)  # None

# re.split(pattern, string, maxsplit=0, flags=0) - 按指定的正则模式分割字符串, 返回一个分割后的列表
# res = re.split(r": ",
#                match_str4)  # ['服务器 IP 地址如下', '  \n主服务器', '192.168.1.1\n备用服务器', ' 10.0.0.5\n外部服务器', '172.16.254.1\n无效IP:256.100.50.25 和 192.168.1.256']

# re.sub(pattern, repl, string, count=0, flags=0) - 查找符合正则模式的匹配项, 并可以替换一个或多个匹配项成其他内容
# res = re.sub(r"\s+", " ",
#              match_str4,
#              count=6)  # 服务器 IP 地址如下: 主服务器: 192.168.1.1 备用服务器: 10.0.0.5\n外部服务器: 172.16.254.1\n无效IP:256.100.50.25 和 192.168.1.256

print(res)
