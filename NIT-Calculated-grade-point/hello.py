# -*- coding: UTF-8 -*-

from flask import Flask,render_template
from flask_wtf import Form
from wtforms import StringField, SubmitField,PasswordField
from wtforms.validators import Required

import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
class NameForm(Form):
	name = StringField('学号', validators=[Required()])
	password = PasswordField('密码', validators=[Required()])
	xq = StringField('学期', validators=[Required()])
	submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
	name = None
	password = None
	jd = 0 
	zd={}
	form = NameForm()
	if form.validate_on_submit():
		name = form.name.data
		password = form.password.data
		#输入你的学号+密码+想要查询的学期(2014-2015-2)
		xh=name
		mm=password
		xq=form.xq.data

		#登陆
		s = requests.Session()
		r = s.get('http://117.40.44.25/zzxk_index.htm')
		payload = {'ls_xh':xh,
		           'ls_mm':mm,
		           'B1':'%B5%C7%C2%BC'}
		login = s.post('http://117.40.44.25/zzxk_login_sfcg.asp',data=payload)

		#获取成绩
		cxcj= s.get('http://117.40.44.25/zzxk_fxksbm_cxcj.asp')
		bs = BeautifulSoup(cxcj.content,'lxml')
		data_list = []
		for idx,tr in enumerate(bs.find_all('tr')):
		    if idx>=2:
		        tds = tr.find_all('td')
		        data_list.append({
		            '学期':tds[0].text,
		            '课程':tds[1].text,
		            '学分':tds[3].text,
		            '课程性质':tds[4].text,
		            '成绩':tds[7].text
		            })
		        
		#计算绩点
		def calc(scores):
		    if int(scores)>=90:
		        return 4
		    else:
		        if int(scores)>=85:
		            return 3.7
		        else:
		            if int(scores)>=82:
		                return 3.3
		            else:
		                if int(scores)>=78:
		                    return 3
		                else:
		                    if int(scores)>=75:
		                        return 2.7
		                    else:
		                        if int(scores)>=72:
		                            return 2.3
		                        else:
		                            if int(scores)>=68:
		                                return 2
		                            else:
		                                if int(scores)>=64:
		                                    return 1.5
		                                else:
		                                    if int(scores)>=60:
		                                        return 1
		                                    else:
		                                        return 0
		zxf=0 #zxf总学分
		zjd=0 #zjd总绩点
		for kc in data_list:
		    if kc['学期']==xq:
		        if kc['课程性质']!='通识任选课':
		            zjd+=float(calc(kc['成绩']))*float(kc['学分'])
		            zxf+=float(kc['学分'])
		            zd[kc['课程']]=kc['成绩']
		        #print('课程名:',kc['课程'],'成绩:',kc['成绩'])
		if(zjd==0 or zxf==0):
			jd = '你是不是哪里写错了，密码或者学期或者帐号，要不然就是你这个学期就没成绩'
		else:
			jd=zjd/zxf
	return render_template('index.html', form=form, name=jd,kcm1=zd)

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000,debug=False)