import requests


def get_ip_address(request):
    ip = str()
    try:
        x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forward:
            ip = x_forward.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
    except:
        pass
    return ip

def get_user_country(request):
    ip_address = get_ip_address(request)
    url = f"http://ipinfo.io/{ip_address}/json"
    data = requests.get(url)
    return data.json()