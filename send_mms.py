# -*- coding: utf-8 -*-

import json

from common import *
from lib.message_service import *


message_service = MessageService(client_id, api_key)

# 멀티 전송
data = {
	'msg_type': 'mms',
	'phone': '01000000001',
	'callback': '01000000000',
	'subject': u'MMS 제목 테스트',
#	'trandate': '20150101000000', # 예약 시 설정
	'msg': u'MMS 메시지 테스트'
}

files = {'image': open('./mms/sample.jpg', 'rb')} # MMS 이미지 경로

print message_service.send_message(data, files)
