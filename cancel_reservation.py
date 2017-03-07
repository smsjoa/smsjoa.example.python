# -*- coding: utf-8 -*-

import json

from common import *
from lib.message_service import *


message_service = MessageService(client_id, api_key)

# 예약 취소
param = [
	'', # msg_serial
]

print message_service.cancel_reservation(param)
