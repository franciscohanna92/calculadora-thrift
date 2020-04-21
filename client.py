import sys
import glob
sys.path.append('gen-py')

from app import Calculadora
from app.ttypes import Error

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


def main():
    # Creamos un socket, el cliente y nos conectamos al servidor
    transport = TSocket.TSocket('localhost', 9090)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = Calculadora.Client(protocol)
    transport.open()

    print('El número 12 es: ' + client.parImpar(12))
    print('El número 31 es: ' + client.parImpar(31))

    print('2 + 5 = %d' % client.sumar(2, 5))
    print('14 - 8 = %d' % client.restar(14, 8))
    print('4 * 3 = %d' % client.multiplicar(4, 3))
    print('18 / 6 = %d' % client.dividir(18, 6))

    try:
        cociente = client.dividir(5, 0)
    except Error as e:
        print('5 / 0 = Error: %r' % e.reason)

    transport.close()


if __name__ == '__main__':
    try:
        main()
    except Thrift.TException as tx:
        print('%s' % tx.message)