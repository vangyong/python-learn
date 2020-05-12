
## 环境安装
1.pip 导出、安装
pip freeze > requirements
pip install -r requirements
2.anaconda 导出、安装
conda list -e > requirements
conda install --yes --file requirements    

## ICE 服务
ice 生成代码(需先安装ice)
slice2py Printer.ice
    
## PCAP包解析    