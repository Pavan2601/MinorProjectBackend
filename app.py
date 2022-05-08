import json
import pickle
import pandas as pd

def life(data):
    jsondata = [json.loads(data)]
    filename = './finalized_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    df = pd.DataFrame.from_dict(jsondata)

    df["Introvert"] = df["Introvert"].map({'yes':1,'no':0})
    df["olympiads"] = df["olympiads"].map({'yes':1,'no':0})
    df["can work long time before system?"] = df["can work long time before system?"].map({'yes':1,'no':0})
    df["self-learning capability?"] = df["self-learning capability?"].map({'yes':1,'no':0})
    df["Extra-courses did"] = df["Extra-courses did"].map({'yes':1,'no':0})
    df["talenttests taken?"] = df["talenttests taken?"].map({'yes':1,'no':0})
    df["interested in games"] = df["interested in games"].map({'yes':1,'no':0})
    df["In a Realtionship?"] = df["In a Realtionship?"].map({'yes':1,'no':0})
    df["worked in teams ever?"] = df["worked in teams ever?"].map({'yes':1,'no':0})
    df["Taken inputs from seniors or elders"] = df["Taken inputs from seniors or elders"].map({'yes':1,'no':0})
    df["hard/smart worker"] = df["hard/smart worker"].map({'hard worker':1,'smart worker':0})
    df["Salary/work"]=df["Salary/work"].map({"salary":1,"work":0})
    df["reading and writing skills"]=df["reading and writing skills"].map({"poor":0,"medium":1,"excellent":2})
    df["memory capability score"]=df["memory capability score"].map({"poor":0,"medium":1,"excellent":2})
    df["Gentle or Tuff behaviour?"] =df["Gentle or Tuff behaviour?"].map({"gentle":1,"stubborn":0})
    df["Job/Higher Studies?"] =df["Job/Higher Studies?"].map({"higherstudies":1,"job":0})
    df["Management or Technical"] =df["Management or Technical"].map({"Management":1,"Technical":0})

    certifications=pd.get_dummies(df['certifications'],prefix='certifications')
    workshops=pd.get_dummies(df['workshops'],prefix='workshops')
    subjects=pd.get_dummies(df['Interested subjects'],prefix='subject')
    career=pd.get_dummies(df['interested career area '],prefix='career')
    company=pd.get_dummies(df['Type of company want to settle in?'],prefix='company')
    books=pd.get_dummies(df['Interested Type of Books'],prefix='books')

    data = pd.concat([df,certifications,workshops,subjects,career,company,books],axis=1)
    data.drop(['certifications','workshops','Interested subjects','interested career area ','Type of company want to settle in?','Interested Type of Books'],axis=1,inplace=True)

    for i in loaded_model.allcolumns:
        if i not in data.columns:
            data[i]=0

    data=data[loaded_model.allcolumns] 

    return loaded_model.predict(data)[0]
