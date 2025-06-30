import socket
import requests

def get_local_ip():
    """
    获取本机IP地址
    :return:
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

def get_public_ip():
    """
    获取公网IP地址
    :return:
    """
    try:
        response = requests.get('https://api.ipify.org')
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        pass
    return None

if __name__ == '__main__':
    local_ip = get_local_ip()
    public_ip = get_public_ip()
    print(f"本地IP地址: {local_ip}")
    if public_ip:
        print(f"公网IP地址: {public_ip}")
    else:
        print("无法获取公网IP地址。")
