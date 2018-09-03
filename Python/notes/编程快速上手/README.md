正则表达式：
```python
1、用 import re 导入正则表达式模块
2、用 re.compile() 函数创建一个 Regex 对象（记得使用原始字符串）
3、向 Regex 对象的 search() 方法传入想查找的字符串。它返回一个 Match 对象。
4、调用 Match 对象的 group() 方法，返回实际匹配文本的字符串
```
```python
?匹配零次或一次前面的分组
*匹配零次或多次前面的分组
+匹配一次或多次前面的分组
{n}匹配n次前面的分组
{n,}匹配n次或更多前面的分组
{,m}匹配零次到m次前面的分组
{n,m}匹配至少n次、至多m次前面的分组
{n,m}?或*?或+?对前面的分组进行非贪心匹配
^spam意味着字符串必须以spam开始
spam$意味着字符串必须以spam结束
.匹配所有字符，换行符除外
\d、\w和\s分别匹配数字、单词和空格
\D、\W和\S分别匹配出数字、单词和空格外的所有字符
[abc]匹配方括号内的任意字符
[^abc]匹配不在方括号内的任意字符
```

在Python 中，读写文件有3个步骤：
```python
1、调用 open() 函数，返回一个 File 对象；
2、调用 File 对象的 read() 或 write() 方法；
3、调用 File 对象的 close() 方法，关闭该文件
```
.pyw 扩展名意味着 Python 运行该程序时，不会显示终端窗口。

断言，在代码中，assert 语句包含以下部分：
```python
assert 关键字；
条件（即求值为 True 或 False 的表达式）；
逗号；
当条件为 False 时显示的字符串。
```

要启用 logging 模块，在程序运行时将日志信息显示在屏幕上，请将下面的代码复制到程序顶部（但在Python 的 #! 行之下）：
```python
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
```

下载并保存到文件的完整过程如下：
```python
1.调用 requests.get() 下载该文件；
2.用 'wb' 调用 open()，以写二进制的方式打开一个新文件；
3.利用 Response 对象的 iter_content() 方法做循环；
4.在每次迭代中调用 write()，将内容写入该文件；
5.调用 close() 关闭该文件。
```

CSS 选择器的例子
``` python
传递给 select() 方法的选择器         将匹配...
soup.select('div')                所有名为 <div> 的元素
soup.select('#author')            带有 id 属性为 author 的元素
soup.select('.notice')            所有使用 CSS class 属性名为 notice 的元素
soup.select('div span')           所有在 <div> 元素之内的 <span> 元素
soup.select('div > span')         所有在 <div> 元素之内的 <span> 元素，中间没有其他元素
soup.select('input[name]')        所有名为 <input> ，并有一个 name 属性，其值无所谓的元素
soup.select('input[type="button"]') 所有名为 <input> ，并有一个 type 属性，其值为 button 的元素
```
selenium 的 WebDriver 方法，用于寻找元素
```python
方法名                                     返回的 WebElement 对象/列表
browser.find_element_by_class_name(name)    使用 CSS 类 name 的元素
browser.find_elements_by_class_name(name)
browser.find_element_by_css_selector(selector)  匹配 CSS selector 的元素
browser.find_elements_by_css_selector(selector)
browser.find_element_by_id(id)              匹配 id 属性值的元素
browser.find_elements_by_id(id)
browser.find_element_by_link_text(text)    完全匹配提供的 text 的 <a> 元素
browser.find_elements_by_link_text(text)
browser.find_element_by_partial_link_text(text)     包含提供的 text 的 <a> 元素
browser.find_elements_by_partial_link_text(text)
browser.find_element_by_name(name)              匹配 name 属性值的元素
browser.find_elements_by_name(name)
browser.find_element_by_tag_name(name)          匹配标签 name 的元素（大小写无关，<a> 元素匹配'a' 和 'A'）
browser.find_elements_by_tag_name(name)
```

WebElement 的属性和方法
```python
属性或方法           描述
tag_name            标签名，例如 'a' 表示 <a> 元素
get_attribute(name) 该元素 name 属性的值
text                该元素内的文本
clear()             对于文本字段或文本区域元素，清除其中输入的文本
is_displayed()      如果该元素可见，返回 True，否则返回 False
is_enabled()        对于输入元素，如果该元素启用，返回 True，否则返回 False
is_selected()       对于复选框或单选框元素，如果该元素被选中，返回 True，否则返回 False
location            一个字典，包含键 'x' 和 'y'，表示该元素在页面上的位置
```

selenium.webdriver.common.Keys 模块中常用的变量
```python
属性                                          含义
Keys.DOWN, Keys.UP, Keys.LEFT, Keys.RIGHT       键盘箭头键
Keys.ENTER, Keys.RETURN                         回车和换行键
Keys.HOME, Keys.END,                            Home 键、End 键、PageUp 键和 PageDown 键
Keys.PAGE_DOWN, Keys.PAGE_UP
Keys.ESCAPE, Keys.BACK_SPACE, Keys.DELETE       Esc, Backspace 和 Delete 键
Keys.F1, Keys.F2, ..., Keys.F12                 键盘顶部的 F1 到 F12 键
Keys.TAB                                        Tab 键

browser.back()  点击“返回”按钮
browser.forward()   点击“前进”按钮
browser.refresh()   点击“刷新”按钮
browser.quit()      点击“关闭窗口”按钮
```

下面是从电子表格文件中读取单元格涉及的所有函数、方法和数据类型：
```python
1.导入 openpyxl 模块；
2.调用 openpyxl.load_workbook() 函数；
3.取得 Workbook 对象；
4.调用 get_active_sheet() 或 get_sheet_by_name() 工作簿方法；
5.取得 Worksheet 对象；
6.使用索引或工作表的 cell() 方法，带上 row 和 column 关键字参数；
7.取得 Cell 对象；
8.读取 Cell 对象的 value 属性。
```













