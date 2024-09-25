import os
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

rpc_user = os.getenv("RPC_USER", "admin")
rpc_password = os.getenv("RPC_PASSWORD", "admin")
rpc_port = os.getenv("RPC_PORT", "18332")
rpc_connection = AuthServiceProxy(f"http://{rpc_user}:{rpc_password}@127.0.0.1:{rpc_port}")

def get_new_address():
    try:
        new_address = rpc_connection.getnewaddress()
        print(f"New testnet address: {new_address}")
        return new_address
    except JSONRPCException as e:
        print(f"Error getting new address: {e}")

def get_balance():
    try:
        balance = rpc_connection.getbalance()
        print(f"Balance: {balance} BTC")
        return balance
    except JSONRPCException as e:
        print(f"Error fetching balance: {e}")

def send_transaction(to_address, amount):
    try:
        txid = rpc_connection.sendtoaddress(to_address, amount)
        print(f"Transaction sent! TXID: {txid}")
        return txid
    except JSONRPCException as e:
        print(f"Error sending transaction: {e}")

if __name__ == "__main__":
    new_address = get_new_address()
    balance = get_balance()
    
    rpc_connection._close()
