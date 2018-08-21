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
    str1 = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1534839870320&di=e666a5d0a0cf102c0170fd4a6ad7acfb&imgtype=jpg&src=http%3A%2F%2Fimg2.imgtn.bdimg.com%2Fit%2Fu%3D1745902082%2C3116919931%26fm%3D214%26gp%3D0.jpg"
    get_img_base64_from_url(str1)
