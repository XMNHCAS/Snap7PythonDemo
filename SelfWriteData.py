import snap7
import struct

# 创建通讯客户端实例
plcObj = snap7.client.Client()

# 连接至PLC
plcObj.connect('192.168.10.230', 0, 1)

# 写入DB10.0 —— bool值
plcObj.write_area(snap7.client.Areas.DB, 10, 0, bool.to_bytes(False, 1, 'big'))

# 写入DB10.2
plcObj.write_area(snap7.client.Areas.DB, 10, 2, int.to_bytes(200, 2, 'big'))
# plcObj.write_area(snap7.client.Areas.DB, 10, 2, struct.pack(">h", 112))

# 写入DB10.4 —— real值
plcObj.write_area(snap7.client.Areas.DB, 10, 4, struct.pack(">f", 10.1))

# 写入DB10.8 —— string值
str = 'hello python'
data = int.to_bytes(254, 1, 'big') + int.to_bytes(len(str), 1, 'big') + str.encode(encoding='ascii')
plcObj.write_area(snap7.client.Areas.DB, 10, 8, data)

# 写入DB10.264 —— wstring值
str = '中国北京市'
data = int.to_bytes(508, 2, 'big') + int.to_bytes(len(str), 2, 'big') + str.encode(encoding='utf-16be')
plcObj.write_area(snap7.client.Areas.DB, 10, 264, data)

# 关闭连接
plcObj.disconnect()
