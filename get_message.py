# -*- coding: utf-8 -*-

import json

from common import *
from lib.message_service import *


message_service = MessageService(client_id, api_key)

# 메시지 내역
print message_service.get_balance()
