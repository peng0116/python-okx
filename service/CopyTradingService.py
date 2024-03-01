from okx import CopyTrading
from okx import Account
from APIKEY import *
import json

if __name__ == '__main__':
    # flag是实盘与模拟盘的切换参数 flag is the key parameter which can help you to change between demo and real trading.
    # flag = '1'  # 模拟盘 demo trading
    flag = '0'  # 实盘 real trading

    # account api
    accountAPI = Account.AccountAPI(api_key, secret_key, passphrase, False, flag)
    # 查看账户持仓风险 GET Position_risk
    # result = accountAPI.get_position_risk('SWAP')
    # 查看账户余额  Get Balance
    # result = accountAPI.get_account_balance()

    # copy trading api
    copyTradingAPI = CopyTrading.CopyTradingAPI(api_key, secret_key, passphrase, False, flag)
    result = copyTradingAPI.first_copy_settings(name='127BE725D7F66EED', copymode='SMART_COPY', amount='100')
    # result = copyTradingAPI.first_copy_settings1(name='127BE725D7F66EED', amount='100')

    print(json.dumps(result))

