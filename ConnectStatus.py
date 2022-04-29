import snap7

# 创建通讯客户端实例
plcObj = snap7.client.Client()

# 连接至PLC
plcObj.connect('192.168.10.230', 0, 1)

# 打印连接状态
print(f"连接状态：{plcObj.get_connected()}")

# 关闭连接
plcObj.disconnect()

# 打印连接状态
print(f"连接状态：{plcObj.get_connected()}")
