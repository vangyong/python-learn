
## 环境安装
1.安装依赖包
conda install Flask
conda install requests

## 
python blockchain.py

## 单节点生成区块
* 
http://localhost:5000/mine

http://localhost:5000/transactions/new

http://localhost:5000/chain

http://localhost:5000/nodes/register

http://localhost:5000/nodes/resolve

## 多节点
pipenv run python blockchain.py
pipenv run python blockchain.py -p 5001
    
## 引用
https://cloud.tencent.com/developer/article/1100975    