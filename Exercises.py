①
import pandas as pd

mydataset = {
  'bns': ["第二性", "lud in the mist", "女嫌い"],
  'date':["20200501","20210321","20191222"],
  'jp': [0, 0, 1],
  'en':[0,1,0],
  'non-fic':[1,0,1],
  'feminism':[1,0,1]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

②
import pandas as pd

jp = [0, 0, 1]

myvar = pd.Series(jp, index = ["第二性", "lud in the mist", "女嫌い"])

print(myvar["女嫌い"])


③
import pandas as pd

book_jps = {"第二性": 0, "lud in the mist": 0, "女嫌い": 1}

myvar = pd.Series(book_jps)

print(myvar)


④
import pandas as pd

mydataset = {
  'bns': ["第二性", "lud in the mist", "女嫌い"],
  'date':["20200501","20210321","20191222"],
  'jp': [0, 0, 1],
  'en':[0,1,0],
  'non-fic':[1,0,1],
  'feminism':[1,0,1]
}

myvar = pd.DataFrame(mydataset, index=["第二性","lud","ミソジニー"])

print(myvar.loc[["第二性","lud"]])

⑤
import pandas as pd

data={
	'date':{
    	"第二性":"20200501",
        "lud":"20210321",
        "ミソジニー":"20191222",
    },
    'jp':{
    	"第二性":0,
        "lud":0,
        "ミソジニー":1,
    },
    'en':{
    	"第二性":0,
        "lud":1,
        "ミソジニー":0,
    },
    'non-fic':{
    	"第二性":1,
        "lud":0,
        "ミソジニー":1,
    },
    'feminism':{
    	"第二性":1,
        "lud":0,
        "ミソジニー":1,
    },
}

df = pd.DataFrame(data)

print(df)

⑥
import pandas as pd

data={
	'date':{
    	"第二性":"20200501",
        "lud":"20210321",
        "ミソジニー":"20191222"
    },
    'jp':{
        "ミソジニー":1
    },
    'en':{
        "lud":1
    },
    'non-fic':{
    	"第二性":1,
        "ミソジニー":1
    },
    'feminism':{
    	"第二性":1,
        "ミソジニー":1
    },
}

df = pd.DataFrame(data)

df["jp"].fillna(0, inplace = True)
df["en"].fillna(0, inplace = True)

print(df.to_string())

#Notice in the result: empty cells got the value 0.

⑦
import pandas as pd

data={
	"from":{
    	"0":"b1",
        "1":"b6",
        "2":"b7",
        "3":"b1",
    },
    "to":{
    	"0":"b6",
        "1":"b7",
        "2":"b8",
        "3":"b6",
    },
}

df = pd.DataFrame(data)

df.drop_duplicates(inplace = True)

print(df.to_string())

#Notice that row 3 has been removed from the result

⑧ [from,to] 生成未完成
import pandas as pd
import json

data={
	'date':{
    	"第二性":"20200501",
        "lud":"20210321",
        "ミソジニー":"20191222"
    },
    'jp':{
        "ミソジニー":1
    },
    'en':{
        "lud":1
    },
    'non-fic':{
    	"第二性":1,
        "ミソジニー":1
    },
    'feminism':{
    	"第二性":1,
        "ミソジニー":1
    },
}

node={
	"from":{},
    "to":{}
}

df = pd.DataFrame(data)

df.fillna(0,inplace=True)

en_list=[]
for x in df.index:
	if df.loc[x,"en"] > 0:
		en_list.append(x)

print(en_list)


⑨[from,to] 生成未完成（MOCK DATA）

import pandas as pd

df = pd.read_csv('data.csv')

df.fillna(0,inplace=True)

nodes = {'from':[],'to':[]}

nodesDf = pd.DataFrame(nodes)

#for index, row in df.iterrows():
# print(row[0])

def durationDeal(duration):
 if x>50

# Iterating over one column - `f` is some function that processes your data
result = [durationDeal(x) for x in df['duration']]

print(nodesDf)
