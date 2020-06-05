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


def block_count(include_cemented=True):
    payload = {"action": "block_count", "include_cemented": include_cemented}
    response = post(API, payload)
    return defaultdict(int, response)


def block_count_type():
    payload = {"action": "block_count_type"}
    response = post(API, payload)
    return defaultdict(int, response)


def block_create(
    block_type, balance, key, representative, link, previous, json_block=False
):
    payload = {
        "action": "block_create",
        "type": block_type,
        "balance": balance,
        "key": key,
        "representative": representative,
        "link": link,
        "previous": previous,
        "json_block": json_block,
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
    json_block=False,
):

    payload = {
        "action": "block_hash",
        "json_block": json_block,
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


def block_info(block_hash, json_block=False):
    payload = {
        "action": "block_info",
        "json_block": json_block,
        "hash": block_hash,
    }
    response = post(API, payload)
    return defaultdict(int, response)


def blocks(hashes, json_block=False):
    payload = {
        "action": "blocks",
        "json_block": json_block,
        "hashes": hashes,
    }
    response = post(API, payload)
    return defaultdict(int, response)


def blocks_info(
    hashes,
    include_not_found=False,
    pending=False,
    source=False,
    balance=False,
    json_block=False,
):
    payload = {
        "action": "blocks_info",
        "json_block": json_block,
        "include_not_found": include_not_found,
        "hashes": hashes,
        "pending": pending,
        "source": source,
        "balance": balance,
    }
    response = post(API, payload)
    return defaultdict(int, response)


def bootstrap(address, port, bypass_frontier_confirmation=False):
    payload = {
        "action": "bootstrap",
        "address": address,
        "port": port,
        "bypass_frontier_confirmation": bypass_frontier_confirmation,
    }
    response = post(API, payload)
    return defaultdict(int, response)


def bootstrap_any(force=False):
    payload = {"action": "bootstrap_any", "force": force}
    response = post(API, payload)
    return defaultdict(int, response)


def bootstrap_lazy(block_hash, force=False):
    payload = {"action": "bootstrap_any", "hash": block_hash, "force": force}
    response = post(API, payload)
    return defaultdict(int, response)


def bootstrap_status():
    payload = {"action": "bootstrap_status"}
    response = post(API, payload)
    return defaultdict(int, response)


def chain(block_hash, count=-1, offset=0, reverse=False):
    payload = {
        "action": "chain",
        "block": block_hash,
        "count": count,
        "offset": offset,
        "reverse": reverse,
    }
    response = post(API, payload)
    return defaultdict(int, response)


def confirmation_active(announcements=0):
    payload = {"action": "confirmation_active", "announcements": announcements}
    response = post(API, payload)
    return defaultdict(int, response)


def confirmation_height_currently_processing():
    payload = {"action": "confirmation_height_currently_processing"}
    response = post(API, payload)
    return defaultdict(int, response)


def confirmation_history(block_hash=None):
    payload = {
        "action": "confirmation_history",
        **({"block_hash": block_hash} if block_hash else {}),
    }
    response = post(API, payload)
    return defaultdict(int, response)


def confirmation_info(root, representatives=False, contents=False, json_block=False):
    payload = {
        "action": "confirmation_info",
        "json_block": json_block,
        "root": root,
        "contents": contents,
        "representatives": representatives,
    }
    response = post(API, payload)
    return defaultdict(int, response)


def confirmation_quorum(peer_details=False, peers_stake_required=0):
    payload = {
        "action": "confirmation_quorum",
        "peer_details": peer_details,
        "peers_stake_required": peers_stake_required,
    }
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


def epoch_upgrade(epoch, key, count=None):
    payload = {
        "action": "epoch_upgrade",
        "epoch": epoch,
        "key": key,
        **({"count": count} if count else {}),
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


def ledger(
    account,
    count=-1,
    representative=False,
    weight=False,
    pending=False,
    modified_since=0,
    sorting=False,
    threshold=0,
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
        "threshold": threshold,
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
    include_only_confirmed=True,
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
    json_block=False,
    subtype="",
    force=False,
    watch_work=True,
):
    payload = {
        "action": "process",
        "json_block": json_block,
        "subtype": subtype,
        "watch_work": watch_work,
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


def sign(
    block_type,
    previous_block,
    representative,
    balance,
    link,
    link_as_account,
    signature,
    work,
    private_key=None,
    wallet=None,
    account=None,
    json_block=False,
):
    payload = {
        "action": "sign",
        "json_block": json_block,
        **({"key": private_key} if private_key else {}),
        **({"wallet": wallet} if wallet else {}),
        **({"account": account} if account else {}),
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


# TODO: add support
# def sign_hash(hash):
#     payload = {"action": "sign", "hash": hash}
#     response = post(API, payload)
#     return defaultdict(int, response)


def stats(stats_type):
    payload = {"action": "stats", "type": stats_type}
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


def unchecked(count=-1, json_block=False):
    payload = {"action": "unchecked", "count": count, "json_block": json_block}
    response = post(API, payload)
    return defaultdict(int, response)


def unchecked_clear():
    payload = {"action": "unchecked_clear"}
    response = post(API, payload)
    return defaultdict(int, response)


def unchecked_get(block_hash, json_block=False):
    payload = {"action": "unchecked_get", "hash": block_hash, "json_block": json_block}
    response = post(API, payload)
    return defaultdict(int, response)


def unchecked_keys(key, count=-1, json_block=False):
    payload = {
        "action": "unchecked_keys",
        "key": key,
        "count": count,
        "json_block": json_block,
    }
    response = post(API, payload)
    return defaultdict(int, response)


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


def work_generate(
    block_hash, use_peers=False, difficulty=None, multiplier=None, account=None
):
    payload = {
        "action": "work_generate",
        "hash": block_hash,
        "use_peers": use_peers,
        **({"difficulty": difficulty} if difficulty else {}),
        **({"multiplier": multiplier} if multiplier else {}),
        **({"account": difficulty} if account else {}),
    }
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


def work_validate(work, hash, difficulty=None, multiplier=None):
    payload = {
        "action": "work_validate",
        "hash": hash,
        **({"difficulty": difficulty} if difficulty else {}),
        **({"multiplier": multiplier} if multiplier else {}),
    }
    response = post(API, payload)
    return defaultdict(int, response)


def account_create(wallet, index=None, work=True):
    payload = {
        "action": "account_create",
        "wallet": wallet,
        "work": work,
        **({"index": index} if index else {}),
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


def account_representative_set(wallet, account, representative, work=None):
    payload = {
        "action": "account_representative_set",
        "wallet": wallet,
        "account": account,
        "representative": representative,
        **({"work": work} if work else {}),
    }
    response = post(API, payload)
    return defaultdict(int, response)


def accounts_create(wallet, count, work=True):
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


def receive(wallet, account, block, work=None):
    payload = {
        "action": "receive",
        "wallet": wallet,
        "account": account,
        "block": block,
        **({"work": work} if work else {}),
    }
    response = post(API, payload)
    return defaultdict(int, response)


def receive_minimum():
    payload = {"action": "receive_minimum"}
    response = post(API, payload)
    return defaultdict(int, response)


def receive_minimum_set(amount):
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


def send(wallet, source, destination, amount, id=None, work=None):
    payload = {
        "action": "send",
        "wallet": wallet,
        "source": source,
        "destination": destination,
        "amount": amount,
        **({"id": id} if id else {}),
        **({"work": work} if work else {}),
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


def wallet_balances(wallet, threshold=None):
    payload = {
        "action": "wallet_balances",
        "wallet": wallet,
        **({"threshold": threshold} if threshold else {}),
    }
    response = post(API, payload)
    return defaultdict(int, response)


def wallet_change_seed(wallet, seed, count=0):
    payload = {
        "action": "wallet_change_seed",
        "wallet": wallet,
        "seed": seed,
        "count": count,
    }
    response = post(API, payload)
    return defaultdict(int, response)


def wallet_contains(wallet, account):
    payload = {"action": "wallet_contains", "wallet": wallet, "account": account}
    response = post(API, payload)
    return defaultdict(int, response)


def wallet_create(seed=None):
    payload = {
        "action": "wallet_create",
        **({"seed": seed} if seed else {}),
    }
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
    threshold=None,
    source=False,
    include_active=False,
    min_version=False,
    include_only_confirmed=False,
):
    payload = {
        "action": "wallet_pending",
        "wallet": wallet,
        "count": count,
        **({"threshold": threshold} if threshold else {}),
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


def wallet_representative_set(wallet, representative, update_existing_accounts=False):
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


def wallet_work_get(wallet):
    payload = {"action": "wallet_work_get", "wallet": wallet}
    response = post(API, payload)
    return defaultdict(int, response)


def work_get(wallet, account):
    payload = {"action": "work_get", "wallet": wallet, "account": account}
    response = post(API, payload)
    return defaultdict(int, response)


def work_set(wallet, account, work):
    payload = {"action": "work_set", "wallet": wallet, "account": account, "work": work}
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
