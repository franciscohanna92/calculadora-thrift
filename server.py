import glob
import sys
sys.path.append('gen-py')

from app import Calculadora
from app.ttypes import Error

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


class CalculadoraHandler:
    def __init__(self):
        self.log = {}

    def parImpar(self, num):
        if(num % 2 == 0):
            return 'Par'
        return 'Impar'

    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise Error('No se puede dividir por cero')
        return a / b


if __name__ == '__main__':
    handler = CalculadoraHandler()
    processor = Calculadora.Processor(handler)
    transport = TSocket.TServerSocket(host='127.0.0.1', port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print('Iniciando servidor en el puerto 9090')
    server.serve()
    print('Saliendo...')