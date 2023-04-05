from django.shortcuts import render

# Create your views here.
def get_example(request):
    # 如果有就get
    try:
        urid=request.GET['user_id']
        urpass = request.GET['user_pass']
        se_byear=request.GET['byear']
        se_month=request.GET['bmonth']
        se_day  =request.GET['bday']
        urfmedia=request.GET.getlist('fmedia')
    #若是沒有，回傳NONE
    except:
        urid=None

    verified = urid is not None and urpass == '12345' or False
    #if urid != None and urpass =='12345':
    #    verified = True
    #else:
    #    verified = False
    years = range(1911, 2031)#不含2031
    mns   = range(1,      13)#不含13
    days  = range(1,      32)#不含32

    return render(request, 'get_example.html', locals())

