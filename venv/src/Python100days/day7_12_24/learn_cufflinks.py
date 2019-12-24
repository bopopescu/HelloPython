import pandas as pd
import cufflinks as cf
import numpy as np
import plotly as py


cf.set_config_file(world_readable=True,theme='pearl')
# cf.datagen.lines().iplot(kind='scatter',xTitle='Dates',yTitle='Returns',title='Cufflinks - Line Chart')
cf.datagen.lines().plot([1,2,3],[1,2,3])
# cf.help()
# df=cf.datagen.ohlc()
# qf=cf.QuantFig(df,title='First Quant Figure',legend='top',name='GS')
# qf.add_bollinger_bands()
# qf.iplot()
# cf.set_config_file(offline=True)
# cf.datagen.box(20).iplot(kind='box',legend=False)
# cf.set_config_file(world_readable=True,theme='pearl')
# df=pd.DataFrame(np.random.randn(100,5),index=pd.date_range('1/1/15',periods=100),
#                 columns=['IBM','MSFT','GOOG','VERZ','APPL'])
# df=df.cumsum()