# -*- coding: utf-8 -*-

import json

from common import *
from lib.message_service import *


message_service = MessageService(client_id, api_key)

# 장문 전송
data = {
	'msg_type': 'lms',
	'phone': '01000000001',
	'callback': '01000000000',
	'subject': u'LMS 제목 테스트',
#	'trandate': '20150101000000', # 예약 시 설정
	'msg': u'LMS 메시지 테스트'
}

print message_service.send_message(data)
