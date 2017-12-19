from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
"""
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
result = client.asr(get_file_content('8k.wav'), 'wav', 8000, {
    'lan': 'zh',
})
print(result)
"""

result  = client.synthesis('世界你好，这是广电运通语音合成的第一个版本啊', 'zh', 1, {
    'vol': 5,
})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('auido.mp3', 'wb') as f:
        f.write(result)
