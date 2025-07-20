import requests
from data.config import Config


class APIClient:
    """Клиент для работы с API"""
    
    def __init__(self, base_url=Config.BASE_URL, timeout=Config.API_TIMEOUT):
        self.base_url = base_url
        self.timeout = timeout
        self.session = requests.Session()
    
    def post(self, endpoint, **kwargs):
        url = self.base_url + endpoint
        kwargs.setdefault('timeout', self.timeout)
        return self.session.post(url, **kwargs)
    
    def get(self, endpoint, **kwargs):
        url = self.base_url + endpoint
        kwargs.setdefault('timeout', self.timeout)
        return self.session.get(url, **kwargs)
    
    def patch(self, endpoint, **kwargs):
        url = self.base_url + endpoint
        kwargs.setdefault('timeout', self.timeout)
        return self.session.patch(url, **kwargs)
    
    def delete(self, endpoint, **kwargs):
        url = self.base_url + endpoint
        kwargs.setdefault('timeout', self.timeout)
        return self.session.delete(url, **kwargs)
    
    def post_multipart(self, endpoint, data=None, files=None, headers=None, **kwargs):
        url = self.base_url + endpoint
        kwargs.setdefault('timeout', self.timeout)
        
        request_headers = self.session.headers.copy()
        if headers:
            request_headers.update(headers)
        
        return self.session.post(url, data=data, files=files, headers=request_headers, **kwargs) 