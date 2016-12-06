#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'DeveloperLx'

import sys, json, os
from urllib import request

if (len(sys.argv) < 2):
    print('请给出您的 GitHub ID 作为参数')
    exit()

github_id = sys.argv[1]
if (len(github_id) <= 0):
    print('请给出您的 GitHub ID 作为参数')
    exit()

print('（查询中...）')

PER_PAGE_REPO_MAX_COUNT = 30
cur_page = 1
total_repo = 0
total_star = 0

while True:

    url = 'https://api.github.com/users/%s/repos?page=%s' % (github_id, cur_page)

    with request.urlopen(url) as f:
        data = f.read()

        repo_json = data.decode('utf-8')
        repo_array = json.loads(repo_json)
        if (type(repo_array) != list):
            break

        for repo in repo_array:
            if (type(repo) != dict):
                continue
            total_repo += 1
            star = repo['stargazers_count']
            total_star += star

        if (len(repo_array) < PER_PAGE_REPO_MAX_COUNT):
            break

        cur_page += 1

prompt = ''

if (total_repo == 0 and total_star == 0):
    prompt = '%s，您的 GitHub 共有 0 个repo，0 个star（您的GitHub ID 敲错了？？）' % github_id
else:
    prompt = '%s，您的 GitHub 共有 %s 个repo，%s 个star' % (github_id, total_repo, total_star)

print('=== %s ===' % prompt)
sayPromptCommand = 'say %s' % prompt
os.system(sayPromptCommand)
