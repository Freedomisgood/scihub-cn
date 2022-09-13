# -*- coding: utf-8 -*-
import asyncio

from scihub_cn.models import PaperInfo
from scihub_cn.scihub import SciHub


def test_api():
    """测试api下载功能"""
    https_proxy = "socks5h://127.0.0.1:10808"
    sh = SciHub(proxy=https_proxy)
    # result = sh.download(
    #     info={
    #         'scihub_url': "https://sci-hub.se/10.1016/j.apsb.2021.06.014"
    #     }
    # )
    # print(f"论文下载: {result}")
    # assert type(result) is PaperInfo

    result = sh.download({"doi": '10.1109/ACC.1999.786344'}, is_translate_title=True)
    print(f"论文下载: {result}")
    assert type(result) is PaperInfo

