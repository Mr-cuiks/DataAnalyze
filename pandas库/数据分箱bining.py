# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

score_list = np.random.randint(20, 100, size=50)
binds = [0, 59, 75, 85, 100]
score_cut = pd.cut(score_list, binds)
print(pd.value_counts(score_cut))
df = pd.DataFrame()
df['score'] = score_list
df['student'] = [pd.util.testing.rands(3) for i in range(50)]
df['Categories'] = pd.cut(df['score'], binds,labels=['及格','刚及格','还好','很好'])
print(df)
