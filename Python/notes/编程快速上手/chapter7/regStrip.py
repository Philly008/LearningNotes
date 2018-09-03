# strip() 的正则表达式版本
import re
s = "   jj hj  \t\n\r  "
s = re.sub("^[' \t\n\r\x0b\x0c']+|[' \t\n\r\x0b\x0c']+$", '', s)
print(s)