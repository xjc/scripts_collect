#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,os
import email
import subprocess

reload(sys)
sys.setdefaultencoding('utf8')

def run_shell_cmd(shellcmd, encoding='utf8'):
    res = subprocess.Popen(shellcmd, shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    results = []
    while True:
        line = res.stdout.readline().decode(encoding).strip()
        if line == '' and res.poll() is not None:
            break
        else:
            results.append(line)
    try:
        for failed in ['failed', 'at org.apache.hadoop']:
            if [i.strip() for i in results if i.strip() != '' ][-1].lower().startswith(failed):
                print('hadoop命令执行失败，请检查！')
                sys.exit(-1)
    except:
        pass
    return [res.returncode, '\n'.join(results)]

def build_head(relate_owner):

    full_mail_content = []
    #table_end="</table>"
    #html_head="<html><body>"
    html_head="""<html>
                    <head>
                    <style type="text/css">
                      td
                        {
                          white-space: nowrap;
                        }
                   </style>
             </head>
             <body>
    """

    full_mail_content.append(html_head)
    full_mail_content.append(relate_owner.encode('utf-8'))
    return full_mail_content

    #return full_mail_content

def build_table_end(full_mail_content):
    table_end="</table>"
    full_mail_content.append(table_end)
    full_mail_content.append("<br>"*3)

def build_tail(full_mail_content):
    tail_content = "</html>"
    full_mail_content.append(tail_content)
    return full_mail_content

def build_report_content(content_title, text_file, full_mail_content, report_name="商户日报", add_seq=0):
    
    table_head="<table border=1 style='border-collapse:collapse;width:50%;border-style:none;font-size:11pt;font-color:white' cellspacing='1'>"
    full_mail_content.append(report_name.encode('utf-8'))
    full_mail_content.append(table_head)

    try:
        text_content_file = open(text_file, 'r')
        text_content = text_content_file.readlines()
        text_content_file.close()
    except Exception as e:
        print("file does not exist: %s" % (text_file))
        print(str(e))
        sys.exit(-1)
    text_content = [ i for i in text_content if i.strip != '']

    ############################# table title ##########################################
    table_title_content_part1='''<thread><tr style='background:#0067A6;font-color:white;word-break:keep-all;'>'''
    pre1 = '''<td><p align='center' style='text-align:center'><font color=white>'''
    end1 = '''</font></p></td>'''
    table_title_content_part2 = [ pre1 + i + end1 + "\n" for i in content_title ]
    table_title_content_part3 = '''</tr></thread>'''
    table_title_content = table_title_content_part1 + '\n'.join(table_title_content_part2) + table_title_content_part3

    full_mail_content.append(table_title_content.encode('utf-8'))

    ############################# table body ##########################################
    statics_part = []
    num_line = 0
    for line in text_content:
        tmp_line = []
        tmp_line_list = line.split('\t')
        if add_seq == 1:
            num_line+=1
            tmp_line_list.insert(0, num_line)
        print(555555555555)
        print(line)
        tmp_line_str = '<tr>' + ''.join([ '<td align="center">' + str(i) + '</td>\n' for i in tmp_line_list ]) + '</tr>'
        statics_part.append(tmp_line_str)

    statics_part_str = '\n'.join(statics_part)
    full_mail_content.append(statics_part_str)

    ############################# table end ##########################################
    build_table_end(full_mail_content)

    return full_mail_content
