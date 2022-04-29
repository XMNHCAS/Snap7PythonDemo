import snap7
from snap7 import util

# 创建通讯客户端实例
plcObj = snap7.client.Client()

# 连接至PLC
plcObj.connect('192.168.10.230', 0, 1)

# 写入bool
boolData = bytearray(1)
util.set_bool(boolData, 0, 0, True)
plcObj.db_write(10, 0, boolData)

# 写入int
intData = bytearray(2)
util.set_int(intData, 0, 100)
plcObj.db_write(10, 2, intData)

# 写入real
realData = bytearray(4)
util.set_real(realData, 0, 20.5)
plcObj.db_write(10, 4, realData)

# 写入string
str = "hello snap7"
stringData = bytearray(len(str) + 2)
util.set_string(stringData, 0, str, 256)
stringData[0] = 254
plcObj.db_write(10, 8, stringData)

# 写入wstring
str = '中国广州市'
data = int.to_bytes(508, 2, 'big') + int.to_bytes(len(str), 2, 'big') + str.encode(encoding='utf-16be')
plcObj.db_write(10, 264, data)

plcObj.disconnect()
