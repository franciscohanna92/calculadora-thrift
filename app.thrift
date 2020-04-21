// Definimos una excepción para operación inválida
exception Error {
    1: string reason
}

// Definimos la interfaz del servicio calculadora y sus operaciones
service Calculadora {
    string parImpar(1:int num),
    int sumar(1:int a, 2:int b),
    int restar(1:int a, 2:int b),
    int multiplicar(1:int a, 2:int b),
    double dividir(1:int a, 2:int b) throws (1:Error error)
}
