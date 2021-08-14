class View(object):
    @staticmethod
    def show_crypto_currency(crypto_name, crypto_time, crypto_values):
        print(f"*********************[ {crypto_name} ]*********************")
        print(f'* "Crypto": "{crypto_name}"')
        print(f'* "Time": "{crypto_time}"')
        for value in crypto_values:
            print(f"*")
            print(f"[ PRICES ] *******************************")
            print(f'* "Parameters": {value["parameters"]}')
            print(f'* "Purchase without commissions": {value["purchase_without_commissions"]}')
            print(f'* "Purchase with commissions"   : {value["purchase_with_commissions"]}')
            print(f'* "Sale without commissions"    : {value["sale_without_commissions"]}')
            print(f'* "Sale with commissions"       : {value["sale_with_commissions"]}')
        print(f"******************************************")

    @staticmethod
    def show_crypto_currency_list(crypto_name, crypto_time, crypto_values):
        for i in range(len(crypto_name)):
            print("\n\n")
            print(f"******************[ {crypto_name[i]} ]******************")
            print(f'* "Crypto": "{crypto_name[i]}"')
            print(f'* "Time": "{crypto_time[i]}"')
            for value in crypto_values[i]:
                print(f"*")
                print(f"[ PRICES ] ************************************")
                print(f'* "Parameters": {value["parameters"]}')
                print(f'* "Purchase without commissions": {value["purchase_without_commissions"]}')
                print(f'* "Purchase with commissions"   : {value["purchase_with_commissions"]}')
                print(f'* "Sale without commissions"    : {value["sale_without_commissions"]}')
                print(f'* "Sale with commissions"       : {value["sale_with_commissions"]}')
                print(f"***********************************************")
