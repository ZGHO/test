import time, hashlib


#用户签名， 时间戳
def user_sign(request):
    if request.method == 'POST':
        client_time = request.POST.get('time', '')
        client_sign = request.POST.get('sign', '')
    else:
        return "error"

    if client_time == '' or client_sign == '':
        return "sign null"


    #服务器时间
    now_time = time.time()
    server_time = str(now_time).split('.')[0]
    #获取时间差
    time_difference = int(server_time) - int(client_time)
    if time_difference >= 60:
        return "timeout"

    #签名检查
    md5 = hashlib.md5()
    sign_str = client_time + "&Guest-Bugmaster"
    sign_bytes_utf-8 = sign_str.encode(encoding="utf-8")
    md5.update(sign_bytes_utf8)
    server_sign = md5.hexdigest()

    if server_sign != client_sign:
        return "sign fail"
    else:
        return "sign success"