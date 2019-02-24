# spartan

Next generation core.

# 属性

- 更强的安全性 & 性能沙箱
- 更强的扩展性，能够轻松的嵌入到其他OJ上，只需要实现基本的Input / output Adapter即可
- 支持多线程判题(Test version, beta)
- 测试覆盖率高 > 80%
- 处理所有异常 -> 细分Error
- 最小化配置，提供一键的Docker部署
- 支持Machine Learning上传结果文件进行计算

# 输入
| 类型 | 输入类型 | 默认值 | 说明
| :------: | :------: | :------: | :------: |
| data | str | "" | 代码或者文档
| data_type | str | "file" | 输入种类,可选'c' \| 'cpp' \| 'java' \| 'python2' \| 'python3' \| 'go' \| 'ruby' \| 'rust' \| 'javascript' \| 'file'
| time_limit | int | 1000 | cpu时间限制,单位ms
| memory_limit | int | 64 | 内存限制,单位mib
| cpu_number_limit | int | 1 | cpu核心数量限制,大于1则为多线程模式
| output_limit | int | 64 | 输出限制,单位为mib
| compile_time_limit | int | 2000 | 编译时间限制,单位ms
| compile_memory_limit | int | 64 | 编译内存限制,单位mb
| checker_time_limit | int | 2000 | 检查器时间限制,单位ms
| checker_memory_limit | int | 64 | 检查器内存限制,单位mb
| checker_type | str | "wcmp" | 检查器种类,可选'wcmp' \| 'custom',wcmp是testlib自带的checker,具体参考[这里](https://github.com/MikeMirzayanov/testlib/tree/master/checkers)
| checker_data | str | "" | 自定义检查器脚本内容,仅支持c++语言,模板参考(TODO)

# 部署说明

pip install -r requirements.txt --upgrade

