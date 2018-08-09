# 文件拷贝

source_file = '../../copy-test.zip'
dest_file = source_file[source_file.rfind("/") + 1:]

source_f = open(source_file, 'rb')  # rb 读取二进制文件
dest_f = open(dest_file, 'wb')  # 写入二进制文件

content = source_f.read()
dest_f.write(content)

source_f.close()
dest_f.close()