import io,os,re
import csv
import argparse
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

def extract_text_by_page(pdf_path):
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh, caching=True,check_extractable=False):
            resource_manager = PDFResourceManager()
            fake_file_handle = io.StringIO()
            converter = TextConverter(resource_manager, fake_file_handle)
            page_interpreter = PDFPageInterpreter(resource_manager, converter)
            page_interpreter.process_page(page)
            text = fake_file_handle.getvalue()
            yield text
            # close open handles
            converter.close()
            fake_file_handle.close()
            
def extract_text(pdf_path,keyword):
    page_num = 1
    # keyword = ['国际化','智能化',"服务化","数字化"]
    output = dict()
    for kw in keyword:
        output[kw] = {"num":0,"content":list()}
         
    for page in extract_text_by_page(pdf_path):
        rough = page.split(" ")
        for kw in keyword:
            if True in [kw in i for i in rough]:
                lists = re.split(' |，|。|；',page)
                for element in lists:
                    if kw in element:
                        print(pdf_path,kw,page_num,element)
                        output[kw]['num'] += 1 
                        output[kw]['content'].append("第" + str(page_num)+"页 " + element)
                
        page_num = page_num + 1
    print(output)
    return output
    

                    

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("-p","--path",type=str,help="请输入你要转换的父文件夹路径，默认为获取当前运行路径")
    args.add_argument("-o","--output",type=str,help="输入输出的csv文件名，默认为<current_dir_path>.csv")
    args.add_argument("-k","--keyword",type=str,help="输入关键词以','分割，默认为[国际化,智能化,服务化,数字化]")
    my_args = args.parse_args()
    if my_args.path == None:
        path = os.getcwd()
    else:
        path = my_args.path
        
    if my_args.output == None:
        table_name = os.path.join(path,os.path.split(path)[1] + ".csv")
    else:
        table_name = os.path.join(path,my_args.output + ".csv")
    if my_args.keyword == None:
        keyword = ['国际化','智能化',"服务化","数字化"]
    else:
        my_args.keyword = my_args.keyword.replace("，",",")
        keyword = my_args.keyword.split(",")
    print("源文件夹位置：%s\n输出表格路径及名称：%s\n关键词：%s\n" %(path,table_name,keyword))
    
    with open(table_name, 'a+', newline='') as f:
        writer = csv.writer(f)
        header = ["company","year"]
        for e in keyword:
            header.append("num")
            header.append(e)
        writer.writerow(header)
        
    # linux path sample: "/Users/Niko/PythonProjects/pdfConverter/report_1"
    # windows path sample: "C:/soft/python"
    
    for parent, dirs, files in os.walk(path):   
        for filename in files:
            try:
                print("========= %s 开始解析 =========" %filename)
                file_label = str(os.path.split(parent)[1])
                year_label = re.findall(r'[1-9]+\.?[0-9]*',filename.split("_")[1])[0]
                absolute = os.path.join(parent,filename)
                output = extract_text(absolute,keyword)
                result = [file_label,year_label]
                for key in output:
                    result.append(output[key]['num'])
                    result.append("\r".join(output[key]['content']))
                with open(table_name, 'a+', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(result)
            except:
                pass
                print("error")



