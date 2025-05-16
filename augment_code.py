import hashlib
import uuid
import base64
from urllib.parse import urlencode

def base64url_encode(data_bytes):
    return base64.urlsafe_b64encode(data_bytes).rstrip(b'=').decode('utf-8')

# 生成 PKCE 授权信息
code_verifier = base64url_encode(hashlib.sha256(uuid.uuid4().bytes).digest())
code_challenge = base64url_encode(hashlib.sha256(code_verifier.encode()).digest())
state = str(uuid.uuid4())
# 构造授权 URL
params = {
    "response_type": "code",
    "code_challenge": code_challenge,
    "code_challenge_method": "S256",
    "client_id": "augment-vscode-extension",
    "redirect_uri": "vscode://augment.vscode-augment/auth/result",
    "state": state,
    "scope": "email",
    "prompt": "login"
}
auth_url = f"https://auth.augmentcode.com/authorize?{urlencode(params)}"

print(auth_url)
