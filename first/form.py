from django import forms
from django .forms import widgets


import re

from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
# from django.core.exceptions import D
from first .models import User   #把数据库导进来
class U_ser(forms.Form):
    wid = widgets.TextInput(attrs={'class':'form-control'})
    name = forms.CharField(
        min_length = 1,label='姓名',
        error_messages={  #报错信息
            'required':'用户名不能为空'
        },
        widget=wid,
        validators=[

        ]
                           )


    pwd = forms.CharField(
        widget=widgets.PasswordInput(attrs = {'class':'form-control'}),
        error_messages = {'required':'密码不能为空'}

    )
    r_pwd = forms.CharField(
        widget =widgets.PasswordInput(attrs={'class': 'form-control'}),
        error_messages = {
            'required':'密码不能为空'
        }
    )


    date = forms.DateTimeField(
        widget= widgets.DateInput(
            attrs = {'class':'form-control'}
        ),
    )

    email = forms.EmailField(
        error_messages = {'invalid':'格式错误'},
        widget =  widgets.EmailInput(attrs = {'class':'form-control'})
    )


 #定义钩子
    def clean_name(self):
        val = self.cleaned_data.get('name')
        if val :
            user_obj = User.objects.filter(name = val).first()
            if user_obj:
                raise ValidationError('用户名相同')

            elif val.isdigit():
                raise ValidationError('用户名不能是数字')
            else:
                return val
        else:
            return val
            # raise  ValidationError('用户名不能为空')




    # def clean_email(self):
    #     val = self.cleaned_data.get('email')

    def clean(self): #全局钩子
        pwd = self.cleaned_data.get('pwd')
        r_pwd = self.cleaned_data.get('r_pwd')
        if pwd and r_pwd and pwd != r_pwd:
            raise ValidationError('两次密码不一致请重新输入')
        else:
            return self.cleaned_data  #把争取额信息返回









