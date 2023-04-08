from django import forms

class ContactForm(forms.Form):
    CITY =[
        ['TP', 'Taipei'],
        ['TY', 'Taoyuan'],
        ['TC', 'Taichung'],
        ['TN', 'Tainan'],
        ['KS', 'Kaohsiung'],
        ['HL', 'Hualien'],
        ['PH', 'Penghu'],
    ]

    user_name=forms.CharField(label='您的姓名', max_length=50, initial='小智')
    user_city=forms.ChoiceField(label='居住城市', choices=CITY) #下拉式選單 choice
    user_school=forms.BooleanField(label='是否在學', required=False) #required false代表非必填
    user_email=forms.EmailField(label='電子郵件')
    user_essage = forms.CharField(label='你的意見', widget=forms.Textarea) #widget 可以做text area
