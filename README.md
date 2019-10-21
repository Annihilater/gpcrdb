抓取 https://www.gpcrdb.org/structure/ 页面的表格，本项目使用的是 Scrapy 框架，因为 Scrapy Shell 调试起来比较方便。

数据默认储存到本机 MongoDB 数据库中，在运行爬虫前请先在本机开启 MongoDB，不会启动 MongoDB 的同学请自行 Google。

1. 克隆项目

    ```shell
    git clone https://github.com/Annihilater/gpcrdb.git
    ```

2. 安装依赖

    ```shell
    pip install -r requirements.txt
    ```

3. 运行爬虫

    ```shell
    scrapy crawl structure
    ```

4. 连接 MongoDB 数据库查看抓取到的数据，推荐使用 NoSQLBooter for MongoDB（开源免费、[下载地址](https://nosqlbooster.com/downloads)） 软件连接本地 MongoDB 数据库查看数据
    <img src="https://klause-blog-pictures.oss-cn-shanghai.aliyuncs.com/2019-10-21-075241.png" alt="image-20191021155241356" style="zoom:100%;" />

    

    

> 意外：找到了 gpcrdb 的接口 https://gpcrdb.org/services/reference/



另外`requests`模拟请求的代码在 [gpcrdb/test/requests_code.py](https://github.com/Annihilater/gpcrdb/blob/master/test/requests_code.py) 里。

