from build_mail_util import *

#generate html table
#you need to supply the csv file, and the table title
#the tool only support the standard html table
#add_seq:1|0   add a sequence at the first column or not

def build_html_content():
    mail_content = []
    mail_content_total = []
    relate_owner="<Br><B>业务负责人：John&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;数据负责人：Palo<B><Br/><Br>"
    mail_content = build_head(relate_owner)
    mail_content_total = build_head(relate_owner)

    ################################商户充值日报##################################
    report_name = "商户充值合计"
    text_file = "/home/e/xjc/tmp/wkd_recharge_total.txt"
    content_title = [ '充值日期', '充值额度', '账户消费', '账户余额' ]
    #content_title = [ '充值日期', '充值总计', '消费总计' ]
    mail_content = build_report_content(content_title, text_file, mail_content, report_name = report_name, add_seq = 0)

    ################################商户充值合计##################################
    report_name = "商户充值日报"
    text_file = "/home/e/xjc/tmp/wkd_recharge.txt"
    content_title = [ '序号', '门店id', '门店名称', '省', '市', '区县', '商家电话', '充值日期', '充值额度', '账户消费', '账户余额' ]
    mail_content = build_report_content(content_title, text_file, mail_content, report_name = report_name, add_seq = 1)
    ############################## 商户充值明细 ################################
    report_name = "商户充值明细"
    text_file = "/home/e/xjc/tmp/wkd_recharge_detail.txt"
    content_title = [ '序号', '充值流水号', '门店ID', '门店名称', '商户id', '商户名称', '省', '市', '区县', '门店联系人', '门店联系人手机', '充值金额', '创建>充值记录时间', '创建交易时间', '支付成功时间', '交易成功时间', '更新时间', '第三方平台流水号', '交易状态', '充值渠道', ]
    mail_content = build_report_content(content_title, text_file, mail_content, report_name = report_name, add_seq = 1)
    ############################## html tail ################################
    mail_content = build_tail(mail_content)
    mail_content_total = build_tail(mail_content_total)

    # write into html file
    html_file_name = '/home/e/xjc/tmp/merchant_recharge.html'
    if os.path.exists(html_file_name):
        os.remove(html_file_name)
    html_file = open(html_file_name, 'w')
    html_file.write('\n'.join(mail_content))
    html_file.close()

def build_html_content():
    mail_content = []
    mail_content_total = []
    '''
    relate_owner="""<Br><B>业务负责人：你猜&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;数据负责人：不告诉你<B><Br/><Br>
            """
    '''
    relate_owner=''
    mail_content = build_head(relate_owner)
    mail_content_total = build_head(relate_owner)

    ################################ 呼叫中心日常运营数据 ##################################
    report_name = """
    <font color="#FF0000">
    </font>
    </br></br>
    <B>平安坐享理赔: %s</B></br></br>
    """ % (data_dt)

    #report_name = "APP数据报表</br></br>"
    text_file = hive_export_file
    content_title = title_list
    mail_content = build_report_content(content_title, text_file, mail_content, report_name = report_name, add_seq = 0)

    ############################## html tail ################################
    mail_content = build_tail(mail_content)
    mail_content_total = build_tail(mail_content_total)

    # write into html file
    html_file_name = mail_html_file
    if os.path.exists(html_file_name):
        os.remove(html_file_name)
    html_file = open(html_file_name, 'w')
    html_file.write('\n'.join(mail_content))
    html_file.close()

