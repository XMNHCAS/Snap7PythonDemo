import snap7
from snap7 import util
# import struct

# 创建通讯客户端实例
plcObj = snap7.client.Client()

# 连接至PLC
plcObj.connect('192.168.10.230', 0, 1)

# 读取DB10.0开始的1个字节
# data = plcObj.read_area(snap7.client.Areas.DB, 10, 0, 1)
data = plcObj.db_read(10, 0, 1)

data = plcObj.db_read(10, 0, 776)
# print(plcObj.get_connected())

print(data)
util.set_bool(data, 0, 0, False)
print(data)
print(util.get_bool(data, 0, 0))
print(util.get_int(data, 2))
print(util.get_real(data, 4))
print(util.get_string(data, 8, 256))
# print(bool.from_bytes(data, byteorder='big'))

# 读取DB10.2开始的2个字节
# data = plcObj.read_area(snap7.client.Areas.DB, 10, 2, 2)
# print(int.from_bytes(data, byteorder='big'))

# 读取DB10.4开始的4个字节
# data = plcObj.read_area(snap7.client.Areas.DB, 10, 4, 4)
# data.reverse()
# print(struct.unpack('f', data)[0])

# 读取DB10.10开始的254个字节
# data = plcObj.read_area(snap7.client.Areas.DB, 10, 10, 254)
# print(data.decode(encoding="ascii"))

# 读取DB10.268开始的508个字节
# data = plcObj.read_area(snap7.client.Areas.DB, 10, 268, 508)
# print(data.decode(encoding="utf-16be"))

# # 写入DB10.0 —— bool值
# plcObj.write_area(snap7.client.Areas.DB, 10, 0, bool.to_bytes(True, 1, 'big'))

# # 写入DB10.2
# plcObj.write_area(snap7.client.Areas.DB, 10, 2, int.to_bytes(233, 2, 'big'))
# # plcObj.write_area(snap7.client.Areas.DB, 10, 2, struct.pack(">h", 112))

# # 写入DB10.4 —— real值
# plcObj.write_area(snap7.client.Areas.DB, 10, 4, struct.pack(">f", 10.1))

# # 写入DB10.8 —— string值
# str = 'hello python'
# data = int.to_bytes(254, 1, 'big') + int.to_bytes(
#     len(str), 1, 'big') + str.encode(encoding='ascii')
# plcObj.write_area(snap7.client.Areas.DB, 10, 8, data)

# # 写入DB10.264 —— wstring值
# str = '中国北京市'
# data = int.to_bytes(508, 2, 'big') + int.to_bytes(
#     len(str), 2, 'big') + str.encode(encoding='utf-16be')
# plcObj.write_area(snap7.client.Areas.DB, 10, 264, data)

# 关闭与PLC的连接
plcObj.disconnect()

# areas = ADict({
#   'PE': 0x81,  #input 输入区
#   'PA': 0x82,  #output 输出区
#   'MK': 0x83,  #bit memory 中间存储区（M区）
#   'DB': 0x84,  #DB区
#   'CT': 0x1C,  #counters
#   'TM': 0x1D,  #Timers
# })
