# import sys
# print(sys.platform)

# 建立geometry模組，並載入使用
# import geometry
# print(geometry.dis(1,1,2,2,))
# print(geometry.slope(1,1,2,2,))

# 調整搜尋模組的路徑
import sys
sys.path.append("modules")    # 在模組的搜尋列表中，新增路徑
print(sys.path)     # 印出模組的搜尋路徑列表
import geometry
print(geometry.dis(1,1,2,2,))