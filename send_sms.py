# -*- coding: utf-8 -*-

import json

from common import *
from lib.message_service import *


message_service = MessageService(client_id, api_key)

# 단문 일반 전송
data = {
	'msg_type': 'sms',
	'phone': '01000000001',
	'callback': '01000000000',
#	'trandate': '20150101000000', # 예약 시 설정
	'msg': u'SMS 일반 전송 메시지 테스트'
}


# 단문 개별 전송 (SMS만 지원)
#data = {
#	'msg_type': 'sms',
#	'callback': '01000000000',
##	'trandate': '20150101000000', # 예약 시 설정
#	'msg_list': json.dumps({
#		'01000000001': 'SMS 개별 전송 메시지 테스트 1',
#		'01000000002': 'SMS 개별 전송 메시지 테스트 2'
#	})
#}


print message_service.send_message(data)
