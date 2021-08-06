class View(object):
    @staticmethod
    def show_crypto_currency(crypto_name, crypto_time, crypto_values):
        print(f"*********************[ {crypto_name} ]*********************")
        print(f'* "Crypto": "{crypto_name}"')
        print(f'* "Tiempo": "{crypto_time}"')
        for value in crypto_values:
            print(f"*")
            print(f"[ PRICES ] *******************************")
            print(f'* "Parametros": {value["parametros"]}')
            print(f'* "Compra S/comiciones": {value["compra_sin_comisiones"]}')
            print(f'* "Compra C/comiciones": {value["compra_con_comisiones"]}')
            print(f'* "Venta S/comisiones" : {value["venta_sin_comisiones"]}')
            print(f'* "Venta C/comisiones" : {value["venta_con_comisiones"]}')
        print(f"******************************************")

    @staticmethod
    def show_cryptos_currency_list(crypto_name, crypto_time, crypto_values):
        for i in range(len(crypto_name)):
            print("\n\n")
            print(f"******************[ {crypto_name[i]} ]******************")
            print(f'* "Crypto": "{crypto_name[i]}"')
            print(f'* "Tiempo": "{crypto_time[i]}"')
            for value in crypto_values[i]:
                print(f"*")
                print(f"[ PRICES ] ************************************")
                print(f'* "Parametros": {value["parametros"]}')
                print(f'* "Compra S/comiciones": {value["compra_sin_comisiones"]}')
                print(f'* "Compra C/comiciones": {value["compra_con_comisiones"]}')
                print(f'* "Venta S/comisiones" : {value["venta_sin_comisiones"]}')
                print(f'* "Venta C/comisiones" : {value["venta_con_comisiones"]}')
                print(f"***********************************************")
