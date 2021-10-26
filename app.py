from flask import Flask, render_template, request
import pickle
import re
from nltk.tokenize import TreebankWordTokenizer
import pandas as pd


app=Flask(__name__)

def clean_text(data):
        
        rem1=r'#[A-Za-z0-9]+'
        rem2=r'@[A-Za-z0-9]+'
        rem3=r'https?://[A-Za-z0-9./]+'
        pair=r'|'.join((rem1,rem2,rem3))
        strip=re.sub(pair,'', data)
        letters_only=re.sub('[^a-zA-Z]', ' ',strip)
        lower_case=letters_only.lower()
        token = TreebankWordTokenizer()
        word=token.tokenize(lower_case)  
        return (' '.join(word))
        

@app.route('/', methods=('GET' , 'POST'))

def home():
    
    if request.method=='POST':
        if request.form.get('text')=="":
            final=2
        else:
            model = pickle.load(open('forest_text.pkl','rb'))
            model1 = pickle.load(open('vect_text.pkl','rb'))
            user_input=request.form.get('text')
            clean=clean_text(user_input)
            cleaned=model1.transform(pd.Series(clean))
            final=model.predict(cleaned)
    else:
        final=''
    
    return render_template('fakeNews.html', prediction=final)

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    


