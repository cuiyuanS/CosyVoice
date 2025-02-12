"""
@Project ：CosyVoice 
@File    ：settings.py
@IDE     ：PyCharm 
@Author  ：CuiYuan
@Date    ：27 8月 2024 15:16 
@explain : 文件说明
"""
import os


class Settings:
    # 服务 绝对跟路径
    BASE_DIR = os.getcwd()

    CosyVoice2_PATH = "/home/cui/work/dy/CosyVoice/pretrained_models/CosyVoice2-0.5B"
    CosyVoice_300M_PATH = "/home/cui/work/dy/CosyVoice/pretrained_models/CosyVoice-300M"
    CosyVoice_300M_25Hz_PATH = "/home/cui/work/dy/CosyVoice/pretrained_models/CosyVoice-300M-25Hz"
    CosyVoice_300M_Instruct_PATH = "/home/cui/work/dy/CosyVoice/pretrained_models/CosyVoice-300M-Instruct"
    CosyVoice_300M_SFT_PATH = "/home/cui/work/dy/CosyVoice/pretrained_models/CosyVoice-300M-SFT"
    CosyVoice_TTSFRD_PATH = "/home/cui/work/dy/CosyVoice/pretrained_models/CosyVoice-ttsfrd"


settings = Settings()
