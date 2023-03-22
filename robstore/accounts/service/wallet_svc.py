
# from django.http import JsonResponse
from ..models import Wallet


def get_wallet_info(user_id):
    wallet = Wallet.objects.get(user_id=user_id['user_id'])
    return wallet


def deposit_wallet_money(deposit_infos):
    wallet = Wallet.objects.filter(user_id=deposit_infos['user_id'])
    for wall in wallet:
        wallet_new_value = wall.amount_stored + deposit_infos['amount']
        wall.amount_stored = wallet_new_value
    Wallet.objects.bulk_update(wallet, ['amount_stored'])

    return {
        "deposited": {
            "wallet_id": wallet[0].id,
            "user_id": wallet[0].user_id,
            "amount_deposited": deposit_infos['amount'],
            "new_value": wallet[0].amount_stored
        }
    }
