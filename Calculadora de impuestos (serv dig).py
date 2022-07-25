
from colorama import Fore
from colorama import Style


def calcular_impuesto(monto, porcentaje):
    impuesto = monto * porcentaje
    return impuesto


def principal():
    print(Fore.CYAN + Style.BRIGHT, '=' * 60)
    print(Fore.YELLOW, '\t\tCALCULADORA DE IMPUESTOS SERVICIOS DIGITALES', Fore.RESET)
    # entrada de monto
    print(Fore.CYAN, '=' * 60, Fore.GREEN)
    monto = float(input(' Ingrese Monto a calcular: '))

    # calculo de impuestos
    imp_pais = calcular_impuesto(monto, 0.08)
    percep_ganancias = calcular_impuesto(monto, 0.45225)
    serv_dig = calcular_impuesto(monto, 0.21)
    monto_total = monto + imp_pais + percep_ganancias + serv_dig

    # salida de montos
    print(Fore.CYAN, '=' * 60, )
    print(Fore.LIGHTRED_EX, 'Impuesto Pais:', Fore.LIGHTGREEN_EX, round(imp_pais, 2),'$', Fore.RESET)
    print(Fore.LIGHTRED_EX, 'Percepcion de Ganancias:', Fore.LIGHTGREEN_EX, round(percep_ganancias, 2),'$', Fore.RESET)
    print(Fore.LIGHTRED_EX, 'Servicios Digitales:', Fore.LIGHTGREEN_EX, round(serv_dig, 2),'$', Fore.RESET)
    print(Fore.CYAN, '=' * 60)
    print(Fore.LIGHTYELLOW_EX, 'Monto Total a Pagar:', Fore.LIGHTGREEN_EX, round(monto_total, 2), '$', Fore.RESET)
    print(Fore.CYAN, '=' * 60)


if __name__ == '__main__':
    principal()
