
import base64
import json
import requests


class MessageService:
	def __init__(self, user_id, api_key):
		self.user_id = user_id
		self.api_key = api_key

		self.__service_url = 'https://api.smsjoa.com'
		self.__version = '1'
		self.__token = self.__get_token()


	def __del__(self):
		self.__delete_token()


	def __get_token(self):
		headers = {'Authorization':'Basic ' + base64.b64encode(self.user_id + ":" + self.api_key)}
		result = self.__execute('token', 'post', headers)
		return result.json()['token'] if result else ''


	def __delete_token(self):
		headers = {'Authorization':'Bearer ' + self.__token}
		self.__execute('token', 'delete', headers)


	def __execute(self, uri, method, headers, data=None, is_multi_part=False, files=None):
		result = getattr(requests, method)(self.__service_url + '/' + self.__version + '/' + uri, headers=headers, data=data, files=files);
		return result if result.status_code == 200 else None


	def send_message(self, data, files=None):
		headers = {'Authorization':'Bearer ' + self.__token}
		result = self.__execute('send', 'post', headers, data, (True if data['msg_type'] == 'mms' else False), files)
		return result.json() if result else None


	def get_balance(self):
		headers = {'Authorization':'Bearer ' + self.__token}
		result = self.__execute('balance', 'get', headers)
		return result.json() if result else None


	def get_message(self, param):
		headers = {'Authorization':'Bearer ' + self.__token}
		result = self.__execute('send/' + '/'.join(param), 'get', headers)
		return result.json() if result else None


	def cancel_reservation(self, param):
		headers = {'Authorization':'Bearer ' + self.__token}
		result = self.__execute('reservation/' + param[0], 'delete', headers)
		return result.json() if result else None
