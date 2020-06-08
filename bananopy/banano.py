import requests
from collections import defaultdict

from bananopy.constants import BANANO_HTTP_PROVIDER_URI


# FIXME: check for wrong response
def post(payload, url=BANANO_HTTP_PROVIDER_URI):
    resp = requests.post(url, json=payload)
    json_resp = resp.json()
    return json_resp


def call(action, params=None, url=BANANO_HTTP_PROVIDER_URI):
    params = params or {}
    params["action"] = action
    response = post(params, url)
    return defaultdict(int, response)


def account_balance(account):
    payload = {"account": account}
    return call("account_balance", payload)


def account_block_count(account):
    payload = {"account": account}
    return call("account_block_count", payload)


def account_get(pub_key):
    payload = {"key": pub_key}
    return call("account_get", payload)


def account_history(
    account, count, raw=False, head="", offset=0, reverse=False, account_filter=[]
):
    payload = {"account": account, "count": count}
    return call("account_history", payload)


def account_info(account, representative=False, weight=False, pending=False):
    payload = {
        "account": account,
        "representative": representative,
        "weight": weight,
        "pending": pending,
    }
    return call("account_info", payload)


def account_key(account):
    payload = {"account": account}
    return call("account_key", payload)


def account_representative(account):
    payload = {"account": account}
    return call("account_representative", payload)


def account_weight(account):
    payload = {"account": account}
    return call("account_weight", payload)


def accounts_balances(accounts):
    payload = {"accounts": accounts}
    return call("accounts_balances", payload)


def accounts_frontiers(accounts):
    payload = {"accounts": accounts}
    return call("accounts_frontiers", payload)


def accounts_pending(
    accounts,
    threshold=0,
    source=False,
    include_active=False,
    sorting=False,
    include_only_confirmed=False,
):
    payload = {
        "accounts": accounts,
        "threshold": threshold,
        "source": source,
        "include_active": include_active,
        "sorting": sorting,
        "include_only_confirmed": include_only_confirmed,
    }
    return call("accounts_pending", payload)


def active_difficulty(include_trend=False):
    payload = {"include_trend": include_trend}
    return call("active_difficulty", payload)


def available_supply():
    return call("available_supply")


def block_account(block_hash):
    payload = {"hash": block_hash}
    return call("block_account", payload)


def block_confirm(block_hash):
    payload = {"hash": block_hash}
    return call("block_confirm", payload)


def block_count(include_cemented=True):
    payload = {"include_cemented": include_cemented}
    return call("block_count", payload)


def block_count_type():
    return call("block_count_type")


def block_create(
    block_type, balance, key, representative, link, previous, json_block=False
):
    payload = {
        "type": block_type,
        "balance": balance,
        "key": key,
        "representative": representative,
        "link": link,
        "previous": previous,
        "json_block": json_block,
    }
    return call("block_create", payload)


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
    return call("block_hash", payload)


def block_info(block_hash, json_block=False):
    payload = {
        "json_block": json_block,
        "hash": block_hash,
    }
    return call("block_info", payload)


def blocks(hashes, json_block=False):
    payload = {
        "json_block": json_block,
        "hashes": hashes,
    }
    return call("blocks", payload)


def blocks_info(
    hashes,
    include_not_found=False,
    pending=False,
    source=False,
    balance=False,
    json_block=False,
):
    payload = {
        "json_block": json_block,
        "include_not_found": include_not_found,
        "hashes": hashes,
        "pending": pending,
        "source": source,
        "balance": balance,
    }
    return call("blocks_info", payload)


def bootstrap(address, port, bypass_frontier_confirmation=False):
    payload = {
        "address": address,
        "port": port,
        "bypass_frontier_confirmation": bypass_frontier_confirmation,
    }
    return call("bootstrap", payload)


def bootstrap_any(force=False):
    payload = {"force": force}
    return call("bootstrap_any", payload)


def bootstrap_lazy(block_hash, force=False):
    payload = {"hash": block_hash, "force": force}
    return call("bootstrap_any", payload)


def bootstrap_status():
    return call("bootstrap_status")


def chain(block_hash, count=-1, offset=0, reverse=False):
    payload = {
        "block": block_hash,
        "count": count,
        "offset": offset,
        "reverse": reverse,
    }
    return call("chain", payload)


def confirmation_active(announcements=0):
    payload = {"announcements": announcements}
    return call("confirmation_active", payload)


def confirmation_height_currently_processing():
    return call("confirmation_height_currently_processing")


def confirmation_history(block_hash=None):
    payload = {
        **({"block_hash": block_hash} if block_hash else {}),
    }
    return call("confirmation_history", payload)


def confirmation_info(root, representatives=False, contents=False, json_block=False):
    payload = {
        "json_block": json_block,
        "root": root,
        "contents": contents,
        "representatives": representatives,
    }
    return call("confirmation_info", payload)


def confirmation_quorum(peer_details=False, peers_stake_required=0):
    payload = {
        "peer_details": peer_details,
        "peers_stake_required": peers_stake_required,
    }
    return call("confirmation_quorum", payload)


def database_txn_tracker():
    return call("database_txn_tracker")


def delegators(account):
    payload = {"account": account}
    return call("delegators", payload)


def delegators_count(account):
    payload = {"account": account}
    return call("delegators_count", payload)


def deteministic_key(seed, index=0):
    payload = {"seed": seed, "index": index}
    return call("deterministic_key", payload)


def epoch_upgrade(epoch, key, count=None):
    payload = {
        "epoch": epoch,
        "key": key,
        **({"count": count} if count else {}),
    }
    return call("epoch_upgrade", payload)


def frontier_count():
    return call("frontier_count")


def frontiers(account, count=-1):
    payload = {"account": account, "count": count}
    return call("frontiers", payload)


def keepalive(address, port):
    payload = {"address": address, "port": port}
    return call("keepalive", payload)


def key_create():
    return call("key_create")


def key_expand(key):
    payload = {"key": key}
    return call("key_expand", payload)


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
        "account": account,
        "count": count,
        "representative": representative,
        "weight": weight,
        "pending": pending,
        "modified_since": modified_since,
        "sorting": sorting,
        "threshold": threshold,
    }
    return call("ledger", payload)


def node_id():
    return call("node_id")


def node_id_delete():
    return call("node_id_delete")


# version 21.0+
# def node_telemetry():
#     return call("node_telemetry")


def peers(peer_details=False):
    payload = {"peer_details": peer_details}
    return call("peers", payload)


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
        "account": account,
        "count": count,
        "threshold": threshold,
        "source": source,
        "include_active": include_active,
        "min_version": min_version,
        "sorting": sorting,
        "include_only_confirmed": include_only_confirmed,
    }
    return call("pending", payload)


def pending_exists(block_hash, include_active=False, include_only_confirmed=False):
    payload = {
        "hash": block_hash,
        "include_active": include_active,
        "include_only_confirmed": include_only_confirmed,
    }
    return call("pending_exists", payload)


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
    return call("process", payload)


def representatives(count=-1, sorting=False):
    payload = {"count": count, "sorting": sorting}
    return call("representatives", payload)


def representatives_online(weight=False):
    payload = {"weight": weight}
    return call("representatives_online", payload)


def republish(block_hash, sources=False, destinations=False):
    payload = {
        "hash": block_hash,
        "sources": sources,
        "destinations": destinations,
    }
    return call("republish", payload)


def sign(
    block_type,
    previous_block,
    representative,
    balance,
    link,
    link_as_account,
    signature,
    work,
    key=None,
    wallet=None,
    account=None,
    json_block=False,
):
    payload = {
        "json_block": json_block,
        **({"key": key} if key else {}),
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
    return call("sign", payload)


# TODO: add support
# def sign_hash(hash):
#     payload = {"hash": hash}
#     return call("sign", payload)


def stats(stats_type):
    payload = {"type": stats_type}
    return call("stats", payload)


def stats_clear():
    return call("stats_clear")


def stop():
    return call("stop")


def successors(block_hash, count=-1, offset=0, reverse=False):
    payload = {
        "block": block_hash,
        "count": count,
        "offset": offset,
        "reverse": reverse,
    }
    return call("successors", payload)


def validate_account_number(account):
    payload = {"account": account}
    return call("validate_account_number", payload)


def version():
    return call("version")


def unchecked(count=-1, json_block=False):
    payload = {"count": count, "json_block": json_block}
    return call("unchecked", payload)


def unchecked_clear():
    return call("unchecked_clear")


def unchecked_get(block_hash, json_block=False):
    payload = {"hash": block_hash, "json_block": json_block}
    return call("unchecked_get", payload)


def unchecked_keys(key, count=-1, json_block=False):
    payload = {
        "key": key,
        "count": count,
        "json_block": json_block,
    }
    return call("unchecked_keys", payload)


def unopened(account, count=-1, threshold=0):
    payload = {
        "account": account,
        "count": count,
        "threshold": threshold,
    }
    return call("unopened", payload)


def uptime():
    return call("uptime")


def work_cancel(block_hash):
    payload = {"hash": block_hash}
    return call("work_cancel", payload)


def work_generate(
    block_hash, use_peers=False, difficulty=None, multiplier=None, account=None
):
    payload = {
        "hash": block_hash,
        "use_peers": use_peers,
        **({"difficulty": difficulty} if difficulty else {}),
        **({"multiplier": multiplier} if multiplier else {}),
        **({"account": difficulty} if account else {}),
    }
    return call("work_generate", payload)


def work_peer_add(address, port):
    payload = {"address": address, "port": port}
    return call("work_peer_add", payload)


def work_peers():
    return call("work_peers")


def work_peers_clear():
    return call("work_peers_clear")


def work_validate(work, hash, difficulty=None, multiplier=None):
    payload = {
        "hash": hash,
        **({"difficulty": difficulty} if difficulty else {}),
        **({"multiplier": multiplier} if multiplier else {}),
    }
    return call("work_validate", payload)


def account_create(wallet, index=None, work=True):
    payload = {
        "wallet": wallet,
        "work": work,
        **({"index": index} if index else {}),
    }
    return call("account_create", payload)


def account_list(wallet):
    payload = {"wallet": wallet}
    return call("account_list", payload)


def account_move(wallet, source, accounts):
    payload = {
        "wallet": wallet,
        "source": source,
        "accounts": accounts,
    }
    return call("account_move", payload)


def account_remove(wallet, account):
    payload = {"wallet": wallet, "account": account}
    return call("account_remove", payload)


def account_representative_set(wallet, account, representative, work=None):
    payload = {
        "wallet": wallet,
        "account": account,
        "representative": representative,
        **({"work": work} if work else {}),
    }
    return call("account_representative_set", payload)


def accounts_create(wallet, count, work=True):
    payload = {
        "wallet": wallet,
        "count": count,
        "work": work,
    }
    return call("accounts_create", payload)


def password_change(wallet, password):
    payload = {"wallet": wallet, "password": password}
    return call("password_change", payload)


def password_enter(wallet, password):
    payload = {"wallet": wallet, "password": password}
    return call("password_enter", payload)


def password_valid(wallet):
    payload = {"wallet": wallet}
    return call("password_valid", payload)


def receive(wallet, account, block, work=None):
    payload = {
        "wallet": wallet,
        "account": account,
        "block": block,
        **({"work": work} if work else {}),
    }
    return call("receive", payload)


def receive_minimum():
    return call("receive_minimum")


def receive_minimum_set(amount):
    payload = {"amount": amount}
    return call("receive_minimum_set", payload)


def search_pending(wallet):
    payload = {"wallet": wallet}
    return call("search_pending", payload)


def search_pending_all():
    return call("search_pending_all")


def send(wallet, source, destination, amount, id=None, work=None):
    payload = {
        "wallet": wallet,
        "source": source,
        "destination": destination,
        "amount": amount,
        **({"id": id} if id else {}),
        **({"work": work} if work else {}),
    }
    return call("send", payload)


def wallet_add(wallet, key, work=False):
    payload = {"wallet": wallet, "key": key, "work": work}
    return call("wallet_add", payload)


def wallet_add_watch(wallet, accounts):
    payload = {"wallet": wallet, "accounts": accounts}
    return call("wallet_add_watch", payload)


def wallet_balances(wallet, threshold=None):
    payload = {
        "wallet": wallet,
        **({"threshold": threshold} if threshold else {}),
    }
    return call("wallet_balances", payload)


def wallet_change_seed(wallet, seed, count=0):
    payload = {
        "wallet": wallet,
        "seed": seed,
        "count": count,
    }
    return call("wallet_change_seed", payload)


def wallet_contains(wallet, account):
    payload = {"wallet": wallet, "account": account}
    return call("wallet_contains", payload)


def wallet_create(seed=None):
    payload = {
        **({"seed": seed} if seed else {}),
    }
    return call("wallet_create", payload)


def wallet_destroy(wallet):
    payload = {"wallet": wallet}
    return call("wallet_destroy", payload)


def wallet_export(wallet):
    payload = {"wallet": wallet}
    return call("wallet_export", payload)


def wallet_frontiers(wallet):
    payload = {"wallet": wallet}
    return call("wallet_frontiers", payload)


def wallet_history(wallet, modified_since=0):
    payload = {
        "wallet": wallet,
        "modified_since": modified_since,
    }
    return call("wallet_history", payload)


def wallet_info(wallet):
    payload = {"wallet": wallet}
    return call("wallet_info", payload)


def wallet_ledger(
    wallet, representative=False, weight=False, pending=False, modified_since=0
):
    payload = {
        "wallet": wallet,
        "representative": representative,
        "weight": weight,
        "pending": pending,
        "modified_since": modified_since,
    }
    return call("wallet_ledger", payload)


def wallet_lock(wallet):
    payload = {"wallet": wallet}
    return call("wallet_lock", payload)


def wallet_locked(wallet):
    payload = {"wallet": wallet}
    return call("wallet_locked", payload)


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
        "wallet": wallet,
        "count": count,
        **({"threshold": threshold} if threshold else {}),
        "source": source,
        "include_active": include_active,
        "min_version": min_version,
        "include_only_confirmed": include_only_confirmed,
    }
    return call("wallet_pending", payload)


def wallet_representative(wallet):
    payload = {"wallet": wallet}
    return call("wallet_representative", payload)


def wallet_representative_set(wallet, representative, update_existing_accounts=False):
    payload = {
        "wallet": wallet,
        "representative": representative,
        "update_existing_accounts": update_existing_accounts,
    }
    return call("wallet_representative_set", payload)


def wallet_republish(wallet, count=-1):
    payload = {"wallet": wallet, "count": count}
    return call("wallet_history", payload)


def wallet_work_get(wallet):
    payload = {"wallet": wallet}
    return call("wallet_work_get", payload)


def work_get(wallet, account):
    payload = {"wallet": wallet, "account": account}
    return call("work_get", payload)


def work_set(wallet, account, work):
    payload = {"wallet": wallet, "account": account, "work": work}
    return call("work_set", payload)


def ban_from_raw(amount):
    return amount / 10 ** 29


def ban_to_raw(amount):
    return amount * (10 ** 29)


def ban_to_banoshi(amount):
    return amount * 100


def ban_from_banoshi(amount):
    return amount / 100
