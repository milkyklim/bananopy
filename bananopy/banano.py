import requests
from collections import defaultdict

from bananopy.constants import BANANO_HTTP_PROVIDER_URI

API = BANANO_HTTP_PROVIDER_URI


# FIXME: check for wrong response
def post(API, payload):
    resp = requests.post(API, json=payload)
    json_resp = resp.json()
    return json_resp


def account_balance(account):
    payload = {
        "action": "account_balance",
        "account": account,
    }
    response = post(API, payload)
    return defaultdict(int, response)


def account_block_count(account):
    payload = {
        "action": "account_block_count",
        "account": account,
    }
    response = post(API, payload)
    return defaultdict(int, response)


def account_get(pub_key):
    payload = {"action": "account_get", "key": pub_key}
    response = post(API, payload)
    return defaultdict(int, response)


def account_history(
    account, count, raw=False, head="", offset=0, reverse=False, account_filter=[]
):
    payload = {"action": "account_history", "account": account, "count": count}
    response = post(API, payload)
    return defaultdict(int, response)


def account_info(account, representative=False, weight=False, pending=False):
    payload = {
        "action": "account_info",
        "account": account,
        "representative": representative,
        "weight": weight,
        "pending": pending,
    }
    response = post(API, payload)
    return defaultdict(int, response)


def account_key(account):
    payload = {"action": "account_key", "account": account}
    response = post(API, payload)
    pub_key = defaultdict(int, response)
    return pub_key


def account_representative(account):
    payload = {"action": "account_representative", "account": account}
    response = post(API, payload)
    return defaultdict(int, response)


def account_weight(account):
    payload = {"action": "account_weight", "account": account}
    response = post(API, payload)
    return defaultdict(int, response)


def accounts_balances(accounts):
    payload = {"action": "accounts_balances", "accounts": accounts}
    response = post(API, payload)
    return defaultdict(int, response)


def accounts_frontiers(accounts):
    payload = {"action": "accounts_frontiers", "accounts": accounts}
    response = post(API, payload)
    return defaultdict(int, response)


def accounts_pending(
    accounts,
    threshold=0,
    source=False,
    include_active=False,
    sorting=False,
    include_only_confirmed=False,
):
    payload = {
        "action": "accounts_pending",
        "accounts": accounts,
        "threshold": threshold,
        "source": source,
        "include_active": include_active,
        "sorting": sorting,
        "include_only_confirmed": include_only_confirmed,
    }
    response = post(API, payload)
    return defaultdict(int, response)


def active_difficulty(include_trend=False):
    payload = {"action": "active_difficulty", "include_trend": include_trend}
    response = post(API, payload)
    return defaultdict(int, response)


def available_supply():
    payload = {"action": "available_supply"}
    response = post(API, payload)
    return defaultdict(int, response)


def block_account(block_hash):
    payload = {"action": "block_account", "hash": block_hash}
    response = post(API, payload)
    return defaultdict(int, response)


def block_confirm(block_hash):
    payload = {"action": "block_confirm", "hash": block_hash}
    response = post(API, payload)
    return defaultdict(int, response)


def block_count():
    payload = {"action": "block_count"}
    response = post(API, payload)
    return defaultdict(int, response)


def block_count_type():
    payload = {"action": "block_count_type"}
    response = post(API, payload)
    return defaultdict(int, response)


def block_create(block_type, balance, key, representative, link, previous):
    payload = {
        "action": "block_create",
        "type": block_type,
        "balance": balance,
        "key": key,
        "representative": representative,
        "link": link,
        "previous": previous,
    }
    response = post(API, payload)
    return defaultdict(int, response)


def block_hash(
    block_type,
    account,
    previous,
    representative,
    balance,
    link,
    link_as_account,
    signature,
    work,
):

    payload = {
        "action": "block_hash",
        "json_block": True,  # recommended
        "block": {
            "type": block_type,
            "account": account,
            "previous": previous,
            "representative": representative,
            "balance": balance,
            "link": link,
            "link_as_account": link_as_account,
            "signature": signature,
            "work": work,
        },
    }
    response = post(API, payload)
    return defaultdict(int, response)


def block_info(block_hash):
    payload = {
        "action": "block_info",
        "json_block": True,  # recommended
        "hash": block_hash,
    }
    response = post(API, payload)
    return defaultdict(int, response)


def blocks(hashes):
    payload = {
        "action": "blocks",
        "json_block": True,  # recommended
        "hashes": hashes,
    }
    response = post(API, payload)
    return defaultdict(int, response)


def blocks_info(
    hashes, include_not_found=False, pending=False, source=False, balance=False
):
    payload = {
        "action": "blocks_info",
        "json_block": True,  # recommended
        "include_not_found": include_not_found,
        "hashes": hashes,
        "pending": pending,
        "source": source,
        "balance": balance,
    }
    response = post(API, payload)
    return defaultdict(int, response)


def bootstrap(address, port):
    payload = {"action": "bootstrap", "address": address, "port": port}
    response = post(API, payload)
    return defaultdict(int, response)


def bootstrap_any():
    payload = {"action": "bootstrap_any"}
    response = post(API, payload)
    return defaultdict(int, response)


def bootstrap_lazy(block_hash):
    payload = {"action": "bootstrap_any", "hash": block_hash}
    response = post(API, payload)
    return defaultdict(int, response)


def bootstrap_status():
    payload = {"action": "bootstrap_status"}
    response = post(API, payload)
    return defaultdict(int, response)


def chain(block_hash, count=-1, offset=0):
    payload = {
        "action": "chain",
        "block": block_hash,
        "count": count,
        "offset": offset,
    }
    response = post(API, payload)
    return defaultdict(int, response)


def confirmation_active():
    payload = {"action": "confirmation_active"}
    response = post(API, payload)
    return defaultdict(int, response)


def confirmation_height_currently_processing():
    payload = {"action": "confirmation_height_currently_processing"}
    response = post(API, payload)
    return defaultdict(int, response)


# TODO: add optional hash argument
def confirmation_history():
    payload = {"action": "confirmation_history"}
    response = post(API, payload)
    return defaultdict(int, response)


def confirmation_info(root, representatives=False, contents=False):
    payload = {
        "action": "confirmation_info",
        "json_block": True,
        "root": root,
        "contents": contents,
        "representatives": representatives,
    }
    response = post(API, payload)
    return defaultdict(int, response)


# TODO: add missing parameters
def confirmation_quorum():
    payload = {"action": "confirmation_quorum"}
    response = post(API, payload)
    return defaultdict(int, response)


def database_txn_tracker():
    payload = {"action": "database_txn_tracker"}
    response = post(API, payload)
    return defaultdict(int, response)


def delegators(account):
    payload = {"action": "delegators", "account": account}
    response = post(API, payload)
    return defaultdict(int, response)


def delegators_count(account):
    payload = {"action": "delegators_count", "account": account}
    response = post(API, payload)
    return defaultdict(int, response)


def deteministic_key(seed, index=0):
    payload = {"action": "deterministic_key", "seed": seed, "index": index}
    response = post(API, payload)
    return defaultdict(int, response)


def epoch_upgrade(epoch, key):
    payload = {
        "action": "epoch_upgrade",
        "epoch": epoch,
        "key": key,
    }
    response = post(API, payload)
    return defaultdict(int, response)


def frontier_count():
    payload = {"action": "frontier_count"}
    response = post(API, payload)
    return defaultdict(int, response)


def frontiers(account, count=-1):
    payload = {"action": "frontiers", "account": account, "count": count}
    response = post(API, payload)
    return defaultdict(int, response)


def keepalive(address, port):
    payload = {"action": "keepalive", "address": address, "port": port}
    response = post(API, payload)
    return defaultdict(int, response)


def key_create():
    payload = {"action": "key_create"}
    response = post(API, payload)
    return defaultdict(int, response)


def key_expand(private_key):
    payload = {"action": "key_expand", "key": private_key}
    response = post(API, payload)
    return defaultdict(int, response)


# TODO: add missing params
def ledger(
    account,
    count=-1,
    representative=False,
    weight=False,
    pending=False,
    modified_since=0,
    sorting=False,
):
    payload = {
        "action": "ledger",
        "account": account,
        "count": count,
        "representative": representative,
        "weight": weight,
        "pending": pending,
        "modified_since": modified_since,
        "sorting": sorting,
    }
    response = post(API, payload)
    return defaultdict(int, response)


def node_id():
    payload = {"action": "node_id"}
    response = post(API, payload)
    return defaultdict(int, response)


def node_id_delete():
    payload = {"action": "node_id_delete"}
    response = post(API, payload)
    return defaultdict(int, response)


# version 21.0+
# def node_telemetry():
#     payload = {"action": "node_telemetry"}
#     response = post(API, payload)
#     return defaultdict(int, response)


def peers(peer_details=False):
    payload = {"action": "peers", "peer_details": peer_details}
    response = post(API, payload)
    return defaultdict(int, response)


def pending(
    account,
    count=-1,
    threshold=0,
    source=False,
    include_active=False,
    min_version=False,
    sorting=False,
    include_only_confirmed=True,  # recommended
):
    payload = {
        "action": "pending",
        "account": account,
        "count": count,
        "threshold": threshold,
        "source": source,
        "include_active": include_active,
        "min_version": min_version,
        "sorting": sorting,
        "include_only_confirmed": include_only_confirmed,
    }
    response = post(API, payload)
    return defaultdict(int, response)


def pending_exists(block_hash, include_active=False, include_only_confirmed=False):
    payload = {
        "action": "pending_exists",
        "hash": block_hash,
        "include_active": include_active,
        "include_only_confirmed": include_only_confirmed,
    }
    response = post(API, payload)
    return defaultdict(int, response)


def process(
    block_type,
    account,
    previous,
    representative,
    balance,
    link,
    link_as_account,
    signature,
    work,
    subtype="",
    force=False,
):
    payload = {
        "action": "process",
        "subtype": subtype,
        "block": {
            "type": block_type,
            "account": account,
            "previous": previous,
            "representative": representative,
            "balance": balance,
            "link": link,
            "link_as_account": link_as_account,
            "signature": signature,
            "work": work,
        },
        "force": force,
    }
    response = post(API, payload)
    return defaultdict(int, response)


def representatives(count=-1, sorting=False):
    payload = {"action": "representatives", "count": count, "sorting": sorting}
    response = post(API, payload)
    return defaultdict(int, response)


def representatives_online(weight=False):
    payload = {"action": "representatives_online", "weight": weight}
    response = post(API, payload)
    return defaultdict(int, response)


def republish(block_hash, sources=False, destinations=False):
    payload = {
        "action": "republish",
        "hash": block_hash,
        "sources": sources,
        "destinations": destinations,
    }
    response = post(API, payload)
    return defaultdict(int, response)


# TODO: add json_block
def sign_key(
    private_key,
    block_type,
    account,
    previous_block,
    representative,
    balance,
    link,
    link_as_account,
    signature,
    work,
):
    payload = {
        "action": "sign",
        "key": private_key,
        "block": {
            "type": block_type,
            "account": account,
            "previous": previous_block,
            "representative": representative,
            "balance": balance,
            "link": link,
            "link_as_account": link_as_account,
            "signature": signature,
            "work": work,
        },
    }
    response = post(API, payload)
    return defaultdict(int, response)


# FIXME: sub call from sign_key
# def sign_wallet(
#     wallet,
#     block_type,
#     account,
#     previous_block,
#     representative,
#     balance,
#     link,
#     link_as_account,
#     signature,
#     work,
# ):
#     payload = {
#         "action": "sign",
#         "walllet": wallet,
#         "account": account,
#         "block": {
#             "type": block_type,
#             "account": account,
#             "previous": previous_block,
#             "representative": representative,
#             "balance": balance,
#             "link": link,
#             "link_as_account": link_as_account,
#             "signature": signature,
#             "work": work,
#         },
#     }
#     response = post(API, payload)
#     return defaultdict(int, response)


# types are "counters", "samples", "objects"
def stats(stat_type):
    payload = {"action": "stats", "type": stat_type}
    response = post(API, payload)
    return defaultdict(int, response)


def stats_clear():
    payload = {"action": "stats_clear"}
    response = post(API, payload)
    return defaultdict(int, response)


def stop():
    payload = {"action": "stop"}
    response = post(API, payload)
    return defaultdict(int, response)


def successors(block_hash, count=-1, offset=0, reverse=False):
    payload = {
        "action": "successors",
        "block": block_hash,
        "count": count,
        "offset": offset,
        "reverse": reverse,
    }
    response = post(API, payload)
    return defaultdict(int, response)


def validate_account_number(account):
    payload = {"action": "validate_account_number", "account": account}
    response = post(API, payload)
    return defaultdict(int, response)


def version():
    payload = {"action": "version"}
    response = post(API, payload)
    return defaultdict(int, response)


def unchecked(count=-1, json_block=True):
    payload = {"action": "unchecked", "count": count, "json_block": json_block}
    response = post(API, payload)
    return defaultdict(int, response)


def unchecked_clear():
    payload = {"action": "unchecked_clear"}
    response = post(API, payload)
    return defaultdict(int, response)


def unchecked_get(block_hash, json_block=True):
    payload = {"action": "unchecked_get", "hash": block_hash, "json_block": json_block}
    response = post(API, payload)
    return defaultdict(int, response)


def unchecked_keys(key, count=-1, json_block=True):
    payload = {
        "action": "unchecked_keys",
        "key": key,
        "count": count,
        "json_block": json_block,
    }
    response = post(API, payload)
    return defaultdict(int, response)


# TODO: threshold parameter
def unopened(account, count=-1, threshold=0):
    payload = {
        "action": "unopened",
        "account": account,
        "count": count,
        "threshold": threshold,
    }
    response = post(API, payload)
    return defaultdict(int, response)


def uptime():
    payload = {"action": "uptime"}
    response = post(API, payload)
    return defaultdict(int, response)


def work_cancel(block_hash):
    payload = {"action": "work_cancel", "hash": block_hash}
    response = post(API, payload)
    return defaultdict(int, response)


def work_generate(block_hash, use_peers=False):
    payload = {"action": "work_generate", "hash": block_hash, "use_peers": use_peers}
    response = post(API, payload)
    return defaultdict(int, response)


def work_peer_add(address, port):
    payload = {"action": "work_peer_add", "address": address, "port": port}
    response = post(API, payload)
    return defaultdict(int, response)


def work_peers():
    payload = {"action": "work_peers"}
    response = post(API, payload)
    return defaultdict(int, response)


def work_peers_clear():
    payload = {"action": "work_peers_clear"}
    response = post(API, payload)
    return defaultdict(int, response)


# TODO:
def work_validate():
    pass


def account_create(wallet, index=0, work=True):
    payload = {
        "action": "account_create",
        "wallet": wallet,
        "index": index,
        "work": work,
    }
    response = post(API, payload)
    return defaultdict(int, response)


def account_list(wallet):
    payload = {"action": "account_list", "wallet": wallet}
    response = post(API, payload)
    return defaultdict(int, response)


def account_move(wallet, source, accounts):
    payload = {
        "action": "account_move",
        "wallet": wallet,
        "source": source,
        "accounts": accounts,
    }
    response = post(API, payload)
    return defaultdict(int, response)


def account_remove(wallet, account):
    payload = {"action": "account_remove", "wallet": wallet, "account": account}
    response = post(API, payload)
    return defaultdict(int, response)


def account_representative_set(wallet, account, representative):
    payload = {
        "action": "account_representative_set",
        "wallet": wallet,
        "account": account,
        "representative": representative,
    }
    response = post(API, payload)
    return defaultdict(int, response)


def accounts_create(wallet, count, work="true"):
    payload = {
        "action": "accounts_create",
        "wallet": wallet,
        "count": count,
        "work": work,
    }
    response = post(API, payload)
    return defaultdict(int, response)


def password_change(wallet, password):
    payload = {"action": "password_change", "wallet": wallet, "password": password}
    response = post(API, payload)
    return defaultdict(int, response)


def password_enter(wallet, password):
    payload = {"action": "password_enter", "wallet": wallet, "password": password}
    response = post(API, payload)
    return defaultdict(int, response)


def password_valid(wallet):
    payload = {"action": "password_valid", "wallet": wallet}
    response = post(API, payload)
    return defaultdict(int, response)


def receive(wallet, account, block):
    payload = {
        "action": "receive",
        "wallet": wallet,
        "account": account,
        "block": block,
    }
    response = post(API, payload)
    return defaultdict(int, response)


def receive_minimum():
    payload = {"action": "receive_minimum"}
    response = post(API, payload)
    return defaultdict(int, response)


def set_receive_minimum(amount):
    payload = {"action": "receive_minimum_set", "amount": amount}
    response = post(API, payload)
    return defaultdict(int, response)


def search_pending(wallet):
    payload = {"action": "search_pending", "wallet": wallet}
    response = post(API, payload)
    return defaultdict(int, response)


def search_pending_all():
    payload = {"action": "search_pending_all"}
    response = post(API, payload)
    return defaultdict(int, response)


def send(wallet, source, destination, amount):
    payload = {
        "action": "send",
        "wallet": wallet,
        "source": source,
        "destination": destination,
        "amount": amount,
    }
    response = post(API, payload)
    return defaultdict(int, response)


def wallet_add(wallet, key, work=False):
    payload = {"action": "wallet_add", "wallet": wallet, "key": key, "work": work}
    response = post(API, payload)
    return defaultdict(int, response)


def wallet_add_watch(wallet, accounts):
    payload = {"action": "wallet_add_watch", "wallet": wallet, "accounts": accounts}
    response = post(API, payload)
    return defaultdict(int, response)


def wallet_balances(wallet):
    payload = {"action": "wallet_balances", "wallet": wallet}
    response = post(API, payload)
    return defaultdict(int, response)


def wallet_change_seed(wallet, seed):
    payload = {"action": "wallet_change_seed", "wallet": wallet, "seed": seed}
    response = post(API, payload)
    return defaultdict(int, response)


def wallet_contains(wallet, account):
    payload = {"action": "wallet_contains", "wallet": wallet, "account": account}
    response = post(API, payload)
    return defaultdict(int, response)


def wallet_create():
    payload = {"action": "wallet_create"}
    response = post(API, payload)
    return defaultdict(int, response)


def seed_wallet_create(seed):
    payload = {"action": "wallet_create", "seed": seed}
    response = post(API, payload)
    return defaultdict(int, response)


def wallet_destroy(wallet):
    payload = {"action": "wallet_destroy", "wallet": wallet}
    response = post(API, payload)
    return defaultdict(int, response)


def wallet_export(wallet):
    payload = {"action": "wallet_export", "wallet": wallet}
    response = post(API, payload)
    return defaultdict(int, response)


def wallet_frontiers(wallet):
    payload = {"action": "wallet_frontiers", "wallet": wallet}
    response = post(API, payload)
    return defaultdict(int, response)


def wallet_history(wallet, modified_since=0):
    payload = {
        "action": "wallet_history",
        "wallet": wallet,
        "modified_since": modified_since,
    }
    response = post(API, payload)
    return defaultdict(int, response)


def wallet_info(wallet):
    payload = {"action": "wallet_info", "wallet": wallet}
    response = post(API, payload)
    return defaultdict(int, response)


def wallet_ledger(
    wallet, representative=False, weight=False, pending=False, modified_since=0
):
    payload = {
        "action": "wallet_ledger",
        "wallet": wallet,
        "representative": representative,
        "weight": weight,
        "pending": pending,
        "modified_since": modified_since,
    }
    response = post(API, payload)
    return defaultdict(int, response)


def wallet_lock(wallet):
    payload = {"action": "wallet_lock", "wallet": wallet}
    response = post(API, payload)
    return defaultdict(int, response)


def wallet_locked(wallet):
    payload = {"action": "wallet_locked", "wallet": wallet}
    response = post(API, payload)
    return defaultdict(int, response)


def wallet_pending(
    wallet,
    count=-1,
    threshold=0,
    source=False,
    include_active=False,
    min_version=False,
    include_only_confirmed=False,
):
    payload = {
        "action": "wallet_pending",
        "wallet": wallet,
        "count": count,
        "threshold": threshold,
        "source": source,
        "include_active": include_active,
        "min_version": min_version,
        "include_only_confirmed": include_only_confirmed,
    }
    response = post(API, payload)
    return defaultdict(int, response)


def wallet_representative(wallet):
    payload = {"action": "wallet_representative", "wallet": wallet}
    response = post(API, payload)
    return defaultdict(int, response)


def set_wallet_representative(wallet, representative, update_existing_accounts=False):
    payload = {
        "action": "wallet_representative_set",
        "wallet": wallet,
        "representative": representative,
        "update_existing_accounts": update_existing_accounts,
    }
    response = post(API, payload)
    return defaultdict(int, response)


def wallet_republish(wallet, count=-1):
    payload = {"action": "wallet_history", "wallet": wallet, "count": count}
    response = post(API, payload)
    return defaultdict(int, response)


def wallet_work(wallet):
    payload = {"action": "wallet_work_get", "wallet": wallet}
    response = post(API, payload)
    return defaultdict(int, response)


def work(wallet, account):
    payload = {"action": "get_work", "wallet": wallet, "account": account}
    response = post(API, payload)
    return defaultdict(int, response)


def set_work(wallet, account, work):
    payload = {"action": "get_work", "wallet": wallet, "account": account, "work": work}
    response = post(API, payload)
    return defaultdict(int, response)


def ban_from_raw(amount):
    return amount / 10 ** 29


def ban_to_raw(amount):
    return amount * (10 ** 29)


def ban_to_banoshi(amount):
    return amount * 100


def ban_from_banoshi(amount):
    return amount / 100
