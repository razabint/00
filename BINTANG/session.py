# -*- coding: utf-8 -*-
from thrift.transport import THttpClient
from thrift.protocol import TCompactProtocol
from RYO import AuthService, TalkService, ChannelService, CallService, ShopService

class Session:
    def __init__(self, url, headers, path=''):
        self.host = url + path
        self.headers = headers
    def Auth(self, isopen=True):
        self.transport = THttpClient.THttpClient(self.host)
        self.transport.setCustomHeaders(self.headers)        
        self.protocol = TCompactProtocol.TCompactProtocol(self.transport)
        self._auth  = AuthService.Client(self.protocol)
        return self._auth
    def Talk(self, isopen=True):
        self.transport = THttpClient.THttpClient(self.host)
        self.transport.setCustomHeaders(self.headers)        
        self.protocol = TCompactProtocol.TCompactProtocol(self.transport)
        self._talk  = TalkService.Client(self.protocol)
        return self._talk
    def Channel(self, isopen=True):
        self.transport = THttpClient.THttpClient(self.host)
        self.transport.setCustomHeaders(self.headers)
        self.protocol = TCompactProtocol.TCompactProtocol(self.transport)
        self._channel  = ChannelService.Client(self.protocol)
        return self._channel
    def Call(self, isopen=True):
        self.transport = THttpClient.THttpClient(self.host)
        self.transport.setCustomHeaders(self.headers)
        self.protocol = TCompactProtocol.TCompactProtocol(self.transport)
        self._call  = CallService.Client(self.protocol)
        return self._call
    def Shop(self, isopen=True):
        self.transport = THttpClient.THttpClient(self.host)
        self.transport.setCustomHeaders(self.headers)
        self.protocol = TCompactProtocol.TCompactProtocol(self.transport)
        self._shop  = ShopService.Client(self.protocol)