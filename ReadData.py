import snap7
import struct
from snap7 import util


# 创建通讯客户端实例
plcObj = snap7.client.Client()

# 连接至PLC
plcObj.connect('192.168.10.230', 0, 1)

# 读取数据
data = plcObj.db_read(10, 0, 776)

# 关闭连接
plcObj.disconnect()

# python解析
selfBool = bool.from_bytes(data[0:1], byteorder='big')
selfInt = int.from_bytes(data[2:4], byteorder='big')
selfReal = struct.unpack('>f', data[4:8])[0]
selfString = data[10:264].decode(encoding="ascii")
selfWString = data[268:].decode(encoding="utf-16be")
print("python自身函数解析：")
print(
    f"bool:{selfBool}; int:{selfInt}; real:{selfReal}; string:{selfString}; wstring:{selfWString}"
)

# snap7解析
snap7Bool = util.get_bool(data, 0, 0)
snap7Int = util.get_int(data, 2)
snap7Real = util.get_real(data, 4)
snap7String = util.get_string(data, 8, 256)
snap7WString = util.get_string(data, 264, 508)
print("snap7函数解析：")
print(
    f"bool:{snap7Bool}; int:{selfInt}; real:{snap7Real}; string:{snap7String}; wstring:{snap7WString}"
)
