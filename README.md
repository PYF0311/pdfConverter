# pdfConverter
A tool for extracting keywords and sentences from pdf in batches / Support to export csv / Based on pdfminer
## 1.准备工作
### 0. 确保已安装以下软件和Library
```
pycharm latest
python version >= 3.6
pyminer six
```
### 1. 安装python
新电脑建议直接安装anaconda，其中包含python和其他重要组件。并选中「路径添加到环境变量」
### 2. 安装pyminer

```
- 请于cmd中打开，并输入：
pip install pdfminer.six 

- 测试安装成功：在新的文件中输入import和print两行，并观察是否返回'<installed version>' 安装的版本信息。
>>> import pdfminer
>>> print(pdfminer.__version__)  
```
### 3. pycharm
pycharm是python的执行器和文本编辑器，请于官网或百度等渠道下载，学生提供edu邮箱可免费使用，也可直接下载社区版。

## 2.工作原理
1. 程序执行后会遍历该目录下的所有子文件夹和子文件，并保存对应特征
2. 循环读取保存目录所对应的文件，对每一页进行转义文字，并粗略搜索是否存在关键词
3. 若存在，则将该页的文档通过正则匹配分割成每一个语义句，进行精确匹配。并将页码，匹配到的关键词，语义句输出到屏幕
4. 若不存在，不执行精确匹配，跳过该页
5. 整篇文档执行完毕，将结果写入csv表格中
6. 再次执行步骤2

## 3.项目执行
在pycharm的``terminal``中执行``python pdfConverter_v1.0.py`` + 参数。参数均可选填，建议填写``-p``

- ``-p/ --path``：指定执行目录，若不指定，获取当前目录
- ``-o/ --output``：指定输出文件名，若不指定，截取当前目录的子目录名为 输出的文件名（指表格的名称）
- ``-k/ --keyword``：指定关键字，用逗号分开（比如：``国际化，标准化``）。若不指定，默认为 国际化,智能化,服务化,数字化



0. **分离模式（推荐模式）**：脚本位置和执行目录分离。**即你可以把脚本``pdfConverter_v1.0.py``放在桌面等任意位置，然后通过指定path的值选定执行目录**

	```
	python pdfConverter_v1.0.py -p C:/soft/python/report_0 -o output 
	```
	> Linux path sample: "/Users/Niko/PythonProjects/pdfConverter/report_0" <br>
    	Windows path sample: "C:/soft/python/report_0"
1. **集中模式**：脚本放在执行目录中，读取当前目录。若当前目录不符合脚本执行的要求，会报错。（即如果桌面没有 公司代码/pdf 这样的目录结构，执行脚本会报错）

	```
	python pdfConverter_v1.0.py
	```
3. **全参数模式**：指定目录，指定关键字，指定输出文件名

	```
	python pdfConverter_v1.0.py -p C:/soft/python/report_0 -o output_1 -k 国际化
	```

1. **查看使用说明**：

	```
	python pdfConverter_v1.0.py -h 忘记的话可以-h直接查看使用说明）
	```
	```
	====== 脚本使用方法 ========
	
	optional arguments:
	  -h, --help            show this help message and exit
	  -p PATH, --path PATH  请输入你要转换的父文件夹路径，默认为获取当前运行路径
	  -o OUTPUT, --output OUTPUT
	                        输入输出的csv文件名，默认为<current_dir_path>.csv
	  -k KEYWORD, --keyword KEYWORD
	                        输入关键词以','分割，默认为 国际化,智能化,服务化,数字化
	```
	
