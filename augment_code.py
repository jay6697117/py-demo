"""
OAuth 2.0 PKCE (Proof Key for Code Exchange) 授权流程实现

本脚本为 Augment VSCode 扩展实现 OAuth 2.0 PKCE 授权流程。
PKCE 是一种安全扩展，用于防止授权码拦截攻击，特别适用于公共客户端（如桌面应用程序）。

主要功能：
1. 生成 PKCE 所需的 code_verifier 和 code_challenge
2. 构造完整的 OAuth 授权 URL
3. 输出可用于浏览器访问的授权链接

作者：Augment Code
用途：VSCode 扩展身份验证
"""

import hashlib
import uuid
import base64
from urllib.parse import urlencode


def base64url_encode(data_bytes):
    """
    将字节数据编码为 base64url 格式

    base64url 编码是 base64 编码的 URL 安全变体，它：
    - 使用 '-' 和 '_' 替代 '+' 和 '/'
    - 移除末尾的填充字符 '='

    参数:
        data_bytes (bytes): 需要编码的字节数据

    返回:
        str: base64url 编码后的字符串
    """
    return base64.urlsafe_b64encode(data_bytes).rstrip(b'=').decode('utf-8')


# 生成 PKCE 授权信息
# code_verifier: PKCE 流程中的密钥验证器，用于后续验证授权码的合法性
code_verifier = base64url_encode(hashlib.sha256(uuid.uuid4().bytes).digest())

# code_challenge: 基于 code_verifier 生成的挑战码，使用 SHA256 哈希算法
# 授权服务器将存储此值，用于后续验证 code_verifier
code_challenge = base64url_encode(hashlib.sha256(code_verifier.encode()).digest())

# state: 随机生成的状态参数，用于防止 CSRF 攻击
# 客户端需要验证回调中的 state 参数与此值匹配
state = str(uuid.uuid4())

# 构造授权 URL 参数
params = {
    "response_type": "code",           # 指定使用授权码流程
    "code_challenge": code_challenge,   # PKCE 挑战码
    "code_challenge_method": "S256",    # 挑战码生成方法（SHA256）
    "client_id": "augment-vscode-extension",  # 客户端标识符
    "redirect_uri": "vscode://augment.vscode-augment/auth/result",  # 授权后的重定向 URI
    "state": state,                     # 防 CSRF 攻击的状态参数
    "scope": "email",                   # 请求的权限范围
    "prompt": "login"                   # 强制用户重新登录
}

# 构造完整的授权 URL
auth_url = f"https://auth.augmentcode.com/authorize?{urlencode(params)}"

# 输出授权 URL，用户可以在浏览器中访问此链接进行身份验证
print(auth_url)
