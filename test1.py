import pandas as pd
import numpy as np
 
data = pd.DataFrame({
    "sample_id": [1, 2, 3, 4, 5, 6],
    "group": ["control"]*3 + ["treatment"]*3,
    "activity": [90, 100, 110, 120, np.nan, 140],
})
# data是什么？ 三列六行的数据；

summary1 = data.groupby("group")["activity"].agg(["count", "mean"])  
#这一行在做什么？先对group列根据字段分类,只选中 activity 这一列来操作;
#  再对每一类进行计数和平均值计算(count/mean)；

filled = data.fillna(0)
data2 = filled.groupby("group")["activity"].mean()

print("summary1:"+str(summary1))
print("data2:"+str(data2))