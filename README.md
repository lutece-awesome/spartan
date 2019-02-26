# Spartan

[![Python](https://img.shields.io/badge/python-3.7.2-red.svg?style=flat-square)](https://www.python.org/downloads/release/python-370/)
[![Build Status](https://travis-ci.org/lutece-awesome/spartan.svg?branch=master)](https://travis-ci.org/lutece-awesome/spartan)
[![Coverage Status](https://coveralls.io/repos/github/lutece-awesome/spartan/badge.svg?branch=master)](https://coveralls.io/github/lutece-awesome/spartan?branch=master)

Next generation core.

# 架构图

![image](https://github.com/lutece-awesome/spartan/blob/master/docs/pic/pic1.png)

# 属性

-   更强的安全性 & 性能沙箱
-   更强的扩展性，能够轻松的嵌入到其他 OJ 上，只需要实现基本的 Input / output Adapter 即可
-   支持多线程判题(Test version, beta)
-   测试覆盖率高 > 80%
-   处理所有异常 -> 细分 Error
-   最小化配置，提供一键的 Docker 部署
-   支持 Machine Learning 上传结果文件进行计算

# 输入

|         类型         | 输入类型 | 默认值 |                                                                      说明                                                                       |
| :------------------: | :------: | :----: | :---------------------------------------------------------------------------------------------------------------------------------------------: |
|         data         |   str    |   ""   |                                                                  代码或者文档                                                                   |
|      data_type       |   str    | "file" |               输入种类,可选'c' \| 'cpp' \| 'java' \| 'python2' \| 'python3' \| 'go' \| 'ruby' \| 'rust' \| 'javascript' \| 'file'               |
|      time_limit      |   int    |  1000  |                                                              cpu 时间限制,单位 ms                                                               |
|     memory_limit     |   int    |   64   |                                                                内存限制,单位 mib                                                                |
|   cpu_number_limit   |   int    |   1    |                                                     cpu 核心数量限制,大于 1 则为多线程模式                                                      |
|     output_limit     |   int    |   64   |                                                               输出限制,单位为 mb                                                                |
|  compile_time_limit  |   int    |  2000  |                                                              编译时间限制,单位 ms                                                               |
| compile_memory_limit |   int    |   64   |                                                              编译内存限制,单位 mb                                                               |
|  checker_time_limit  |   int    |  2000  |                                                             检查器时间限制,单位 ms                                                              |
| checker_memory_limit |   int    |   64   |                                                             检查器内存限制,单位 mb                                                              |
|     checker_type     |   str    | "wcmp" | 检查器种类,可选"wcmp" \| "custom",wcmp 是 testlib 自带的 checker,具体参考[这里](https://github.com/MikeMirzayanov/testlib/tree/master/checkers) |
|     checker_data     |   str    |   ""   |                              自定义检查器脚本内容,仅在 checker_type 为"custom"时生效,仅支持 c++语言,模板参考(TODO)                              |

# 过程变量

# 部署说明

pip install -r requirements.txt --upgrade
