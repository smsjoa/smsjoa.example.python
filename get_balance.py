# -*- coding: utf-8 -*-

import json

from common import *
from lib.message_service import *


message_service = MessageService(client_id, api_key)

# �ܾ� ��ȸ
print message_service.get_balance()
