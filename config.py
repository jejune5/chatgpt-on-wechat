# encoding:utf-8

import json
import os
from common.log import logger

config = {
    "open_ai_api_key": "YOUR API KEY",
    "model": "gpt-3.5-turbo",
    "proxy": "",
    "single_chat_prefix": ["bot", "@bot"],
    "single_chat_reply_prefix": "",
    "group_chat_prefix": ["@bot"],
    "group_name_white_list": ["ChatGPT测试群", "ChatGPT测试群2"],
    "image_create_prefix": ["画", "发", "找"],
    "speech_recognition": False,
    "voice_reply_voice": False,
    "conversation_max_tokens": 1000,
    "expires_in_seconds": 36000,
    "character_desc": "你是ChatGPT, 一个由OpenAI训练的大型语言模型, 你旨在回答并解决人们的任何问题，并且可以使用多种语言与人交流。"
}


def load_config():
    global config
    config.update(
        {
            "open_ai_api_key": os.getenv("open_ai_api_key", "YOUR API KEY"),
            "model": os.getenv("model", "gpt-3.5-turbo"),
            "single_chat_prefix": os.getenv("single_chat_prefix", "bot @bot").split(),
            "group_chat_prefix": os.getenv("group_chat_prefix", "bot @bot").split(),
            "group_name_white_list": os.getenv("group_name_white_list", "ChatGPT测试群 ChatGPT测试群2").split(),
        }
    )
    # config_path = "config.json"
    # if not os.path.exists(config_path):
    #     raise Exception('配置文件不存在，请根据config-template.json模板创建config.json文件')
    #
    # config_str = read_file(config_path)
    # # 将json字符串反序列化为dict类型
    # config = json.loads(config_str)

    logger.info("[INIT] load config: {}".format(config))


def get_root():
    return os.path.dirname(os.path.abspath(__file__))


def read_file(path):
    with open(path, mode='r', encoding='utf-8') as f:
        return f.read()


def conf():
    return config
