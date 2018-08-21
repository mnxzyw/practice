# coding=utf-8
import os,base64
import requests as req
from PIL import Image
from io import BytesIO

def get_img_base64_from_url(url):
    response = req.get(url)
    ls_f="![avatar](data:image/jpeg;base64,"+ base64.b64encode(BytesIO(response.content).read())+")"
    print ls_f

if __name__=='__main__':
    str1 = "http://fm.shiyunjj.com/2018/1411/5izf.jpg"
    get_img_base64_from_url(str1)
