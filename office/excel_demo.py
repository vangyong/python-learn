import xlwt
import os 
import sys



def txt_xls(filename,xlsname):
    try:
        f = open(filename)
        xls = xlwt.Workbook()
        #生成excel的方法，声明excel
        sheet = xls.add_sheet('sheet',cell_overwrite_ok=True)
        x = 1   #在excel开始写的位置（y）
        sheet.write_merge(0, 0,0,2, '【长安盾-全球威胁情报中心发现并预警】通过长安盾关基防护安全大数据分析。发现以下威胁高危攻击源IP：')


        while True:     #循环读取文本里面的内容
            line = f.readline()     #一行一行的读
            if not line:    #如果没有内容，则退出循环
                break
            if x==1:
                sheet.write(x, 0, line)
            elif x== 3:
                sheet.write(x, 0, line)
            elif x== 5:
                sheet.write(x, 0, line)
                x += 1
                sheet.write(x, 0, 'ip')
                sheet.write(x, 1, '地理位置')
                sheet.write(x, 2, '攻击次数')
            elif x== 18:
                sheet.write(x, 0, line)
                x += 1
                sheet.write(x, 0, 'ip')
                sheet.write(x, 1, '地理位置')
                sheet.write(x, 2, '攻击次数')
            elif x==121:
                sheet.write(x, 0, line)
                x += 1
                sheet.write(x, 0, '地理位置')
                sheet.write(x, 1, '攻击次数')
            else:
                for i in range(len(line.split(' '))):   #\t即tab健分隔
                    item = line.split(' ')[i]
                    sheet.write(x,i,item)      #x单元格经度，i单元格纬度
            x += 1  #另起一行
        sheet.write_merge(134, 134, 0, 2, '已接入长安盾云防御平台客户无需操作，攻击IP已通过长安盾安全大数据分析引擎自动识别风险并阻断。未加入请核实是否与该IP有业务交互，如没有建议从互联网出口防火墙或网关对该IP进行阻断。')
        sheet.col(0).width = 4333
        sheet.col(1).width = 4333
        sheet.col(2).width = 4333
        f.close()
        xls.save(xlsname)        #保存为xls文件
    except:
        raise
if __name__ == '__main__':
    filename = './20210609.txt'
    xlsname = './1.xls'
    txt_xls(filename,xlsname)
