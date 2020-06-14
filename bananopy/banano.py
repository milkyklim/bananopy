import requests
from collections import defaultdict

from bananopy.constants import BANANO_HTTP_PROVIDER_URI


class NodeException(Exception):
    """ Base class for RPC errors """


def call(action, params=None, url=BANANO_HTTP_PROVIDER_URI):
    params = params or {}
    params["action"] = action
    response = requests.post(url, json=params)
    json_response = response.json()

    if "error" in json_response:
        raise NodeException(json_response)

    return defaultdict(str, json_response)


def account_balance(account):
    payload = {"account": account}
    r = call("account_balance", payload)
    for k, v in r.items():
        r[k] = int(v)

    return r


def account_block_count(account):
    payload = {"account": account}
    r = call("account_block_count", payload)
    r["block_count"] = int(r["block_count"])

    return r


def account_get(pub_key):
    payload = {"key": pub_key}
    return call("account_get", payload)


def account_history(
    account, count, raw=False, head="", offset=0, reverse=False, account_filter=[]
):
    payload = {"account": account, "count": count}
    r = call("account_history", payload)
    for i, _ in enumerate(r["history"]):
        for key in ("amount", "local_timestamp", "height"):
            r["history"][i][key] = int(r["history"][i][key])

    return r


def account_info(account, representative=False, weight=False, pending=False):
    payload = {
        "account": account,
        "representative": representative,
        "weight": weight,
        "pending": pending,
    }

    r = call("account_info", payload)
    for k in (
        "account_version",
        "modified_timestamp",
        "confirmation_height",
        "block_count",
        "balance",
        "pending",
        "weight",
    ):
        if k in r:
            r[k] = int(r[k])

    return r


def account_key(account):
    payload = {"account": account}
    return call("account_key", payload)


def account_representative(account):
    payload = {"account": account}
    return call("account_representative", payload)


def account_weight(account):
    payload = {"account": account}
    r = call("account_weight", payload)
    r["weight"] = int(r["weight"])

    return r


def accounts_balances(accounts):
    payload = {"accounts": accounts}
    r = call("accounts_balances", payload)
    for account, balances in r["balances"].items():
        for key in balances:
            r["balances"][account][key] = int(r["balances"][account][key])

    return r


def accounts_frontiers(accounts):
    payload = {"accounts": accounts}
    return call("accounts_frontiers", payload)


# FIXME: check for errors
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

    r = call("accounts_pending", payload)
    for account, data in r["blocks"].items():
        if isinstance(data, list):  # list of block hashes, no change needed
            continue
        if not data:
            r["blocks"][account] = []  # convert a "" response to []
            continue
        for key, value in data.items():
            if isinstance(value, str):  # amount
                r["blocks"][account][key] = int(value)
            elif isinstance(value, dict):  # dict with "amount" and "source"
                for key in ("amount",):
                    if key in value:
                        r["blocks"][account][value][key] = int(
                            r["blocks"][account][value][key]
                        )

    return r


# FIXME: check for errors
def active_difficulty(include_trend=False):
    payload = {"include_trend": include_trend}
    r = call("active_difficulty", payload)
    r["multiplier"] = int(r["multiplier"])
    r["difficulty_trend"] = [int(v) for v in r["difficulty_trend"]]

    return r


def available_supply():
    r = call("available_supply")
    r["available"] = int(r["available"])
    return r


def block_account(hash):
    payload = {"hash": hash}
    return call("block_account", payload)


def block_confirm(hash):
    payload = {"hash": hash}
    r = call("block_confirm", payload)
    r["started"] = int(r["started"])

    return r


def block_count(include_cemented=True):
    payload = {"include_cemented": include_cemented}
    r = call("block_count", payload)
    for k, v in r.items():
        r[k] = int(v)

    return r


def block_count_type():
    r = call("block_count_type")
    for k, v in r.items():
        r[k] = int(v)

    return r


def block_create(type, balance, key, representative, link, previous, json_block=False):
    payload = {
        "type": type,
        "balance": balance,
        "key": key,
        "representative": representative,
        "link": link,
        "previous": previous,
        "json_block": json_block,
    }
    r = call("block_create", payload)

    # FIXME:
    # r["block"]["balance"] = int(r["block"]["balance"])

    return r


def block_hash(
    type,
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
            "type": type,
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


def block_info(hash, json_block=False):
    payload = {
        "json_block": json_block,
        "hash": hash,
    }

    r = call("block_info", payload)
    for key in ("amount", "balance", "height", "local_timestamp"):
        r[key] = int(r[key])

    # FIXME:
    # r["confirmed"] = bool(r["confirmed"])
    r["contents"]["balance"] = int(r["contents"]["balance"])

    return r


def blocks(hashes, json_block=False):
    payload = {
        "json_block": json_block,
        "hashes": hashes,
    }
    r = call("blocks", payload)
    for block, _ in r["blocks"].items():
        r["blocks"][block]["balance"] = int(r["blocks"][block]["balance"])

    return r


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

    r = call("blocks_info", payload)
    for block, info in r["blocks"].items():
        for key in ("amount", "balance", "height", "local_timestamp"):
            r["blocks"][block][key] = int(r["blocks"][block][key])
        r["blocks"][block]["contents"]["balance"] = int(r["blocks"][block]["balance"])

    # FIXME: case when json_block is false
    # + "confirmed" field

    return r


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


def bootstrap_lazy(hash, force=False):
    payload = {"hash": hash, "force": force}
    return call("bootstrap_any", payload)


def bootstrap_status():
    # FIXME: update
    return call("bootstrap_status")


def chain(hash, count=-1, offset=0, reverse=False):
    payload = {
        "block": hash,
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


def confirmation_history(hash=None):
    # FIXME: update
    payload = {
        **({"hash": hash} if hash else {}),
    }
    return call("confirmation_history", payload)


def confirmation_info(root, representatives=False, contents=False, json_block=False):
    # FIXME: update
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
    r = call("confirmation_quorum", payload)
    for k, v in r.items():
        r[k] = int(v)

    return r


def database_txn_tracker():
    # FIXME:
    return call("database_txn_tracker")


def delegators(account):
    payload = {"account": account}
    r = call("delegators", payload)
    if r["delegators"] == "":
        r["delegators"] = {}

    for k, _ in r["delegators"].items():
        r["delegators"][k] = int(r["delegators"][k])

    return r


def delegators_count(account):
    payload = {"account": account}
    r = call("delegators_count", payload)
    r["count"] = int(r["count"])

    return r


def deterministic_key(seed, index=0):
    payload = {"seed": seed, "index": index}
    return call("deterministic_key", payload)


def epoch_upgrade(epoch, key, count=None):
    payload = {
        "epoch": epoch,
        "key": key,
        **({"count": count} if count else {}),
    }
    r = call("epoch_upgrade", payload)
    r["started"] = int(r["started"])

    return r


def frontier_count():
    r = call("frontier_count")
    r["count"] = int(r["count"])

    return r


def frontiers(account, count=-1):
    payload = {"account": account, "count": count}
    return call("frontiers", payload)


def keepalive(address, port):
    payload = {"address": address, "port": port}
    r = call("keepalive", payload)

    print(r)

    r["started"] = int(r["started"])

    return r


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
    # FIXME:
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
    r = call("ledger", payload)
    return r


def node_id():
    return call("node_id")


def node_id_delete():
    r = call("node_id_delete")
    r["deprecated"] = int(r["deprecated"])

    return r


# version 21.0+
# def node_telemetry():
#     return call("node_telemetry")


def peers(peer_details=False):
    # FIXME:
    payload = {"peer_details": peer_details}
    r = call("peers", payload)

    return r


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
    # FIXME:
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
    r = call("pending", payload)

    return r


def pending_exists(hash, include_active=False, include_only_confirmed=False):
    payload = {
        "hash": hash,
        "include_active": include_active,
        "include_only_confirmed": include_only_confirmed,
    }
    r = call("pending_exists", payload)
    r["exists"] = int(r["exists"])

    return r


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
    # FIXME:
    payload = {"count": count, "sorting": sorting}
    r = call("representatives", payload)

    print(r)
    raise Exception

    return r


def representatives_online(weight=False):
    # FIXME: weight
    payload = {"weight": weight}
    return call("representatives_online", payload)


def republish(hash, sources=False, destinations=False):
    payload = {
        "hash": hash,
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
    # FIXME:
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
    # FIXME: depends on state_type
    payload = {"type": stats_type}
    return call("stats", payload)


def stats_clear():
    return call("stats_clear")


def stop():
    return call("stop")


def successors(hash, count=-1, offset=0, reverse=False):
    payload = {
        "block": hash,
        "count": count,
        "offset": offset,
        "reverse": reverse,
    }
    return call("successors", payload)


def validate_account_number(account):
    payload = {"account": account}
    r = call("validate_account_number", payload)
    r["valid"] = int(r["valid"])

    return r


def version():
    r = call("version")
    for key in ("rpc_version", "store_version", "protocol_version"):
        r[key] = int(r[key])

    return r


def unchecked(count=-1, json_block=False):
    # FIXME: check if correct
    payload = {"count": count, "json_block": json_block}
    r = call("unchecked", payload)

    if r["blocks"] == "":
        r["blocks"] = {}

    for hash, blocks in r["blocks"].items():
        for key in blocks:
            r["blocks"][hash][key] = int(r["blocks"][hash][key])

    return r


def unchecked_clear():
    r = call("unchecked_clear")
    r["success"] = {}
    return r


def unchecked_get(hash, json_block=False):
    payload = {"hash": hash, "json_block": json_block}
    r = call("unchecked_get", payload)
    r["contents"]["balance"] = int(r["contents"]["balance"])

    return r


def unchecked_keys(key, count=-1, json_block=False):
    payload = {
        "key": key,
        "count": count,
        "json_block": json_block,
    }
    r = call("unchecked_keys", payload)
    if r["unchecked"] == "":
        r["unchecked"] = {}

    for i, _ in enumerate(r["unchecked"]):
        r["unchecked"][i]["contents"]["balance"] = int(
            r["unchecked"][i]["contents"]["balance"]
        )

    return r


def unopened(account, count=-1, threshold=0):
    # FIXME: test empty
    payload = {
        "account": account,
        "count": count,
        "threshold": threshold,
    }
    r = call("unopened", payload)
    for account, balance in r["accounts"].items():
        r["accounts"][account] = int(balance)

    return r


def uptime():
    r = call("uptime")
    r["seconds"] = int(r["seconds"])
    return r


def work_cancel(hash):
    payload = {"hash": hash}
    return call("work_cancel", payload)


def work_generate(
    hash, use_peers=False, difficulty=None, multiplier=None, account=None
):
    payload = {
        "hash": hash,
        "use_peers": use_peers,
        **({"difficulty": difficulty} if difficulty else {}),
        **({"multiplier": multiplier} if multiplier else {}),
        **({"account": difficulty} if account else {}),
    }
    return call("work_generate", payload)


def work_peer_add(address, port):
    payload = {"address": address, "port": port}
    r = call("work_peer_add", payload)
    r["success"] = {}
    return r


def work_peers():
    return call("work_peers")


def work_peers_clear():
    r = call("work_peers_clear")
    r["success"] = {}
    return r


def work_validate(work, hash, difficulty=None, multiplier=None):
    payload = {
        "hash": hash,
        **({"difficulty": difficulty} if difficulty else {}),
        **({"multiplier": multiplier} if multiplier else {}),
    }
    return call("work_validate", payload)


def account_create(wallet, index=None, work=True):
    # FIXME: use Decimals for multiplier
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
    r = call("account_move", payload)
    r["moved"] = int(r["moved"])

    return r


def account_remove(wallet, account):
    payload = {"wallet": wallet, "account": account}
    r = call("account_remove", payload)
    r["removed"] = int(r["removed"])

    return r


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
    r = call("password_change", payload)
    r["changed"] = int(r["changed"])

    return r


def password_enter(wallet, password):
    payload = {"wallet": wallet, "password": password}
    r = call("password_enter", payload)
    r["valid"] = int(r["valid"])

    return r


def password_valid(wallet):
    payload = {"wallet": wallet}
    r = call("password_valid", payload)
    r["valid"] = int(r["valid"])

    return r


def receive(wallet, account, block, work=None):
    payload = {
        "wallet": wallet,
        "account": account,
        "block": block,
        **({"work": work} if work else {}),
    }
    return call("receive", payload)


def receive_minimum():
    r = call("receive_minimum")
    r["amount"] = int(r["amount"])

    return r


def receive_minimum_set(amount):
    payload = {"amount": amount}
    r = call("receive_minimum_set", payload)
    r["success"] = {}

    return r


def search_pending(wallet):
    payload = {"wallet": wallet}
    r = call("search_pending", payload)
    r["started"] = int(r["started"])

    return r


def search_pending_all():
    r = call("search_pending_all")
    r["success"] = {}

    return r


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
    r = call("wallet_add_watch", payload)
    r["success"] = {}

    return r


def wallet_balances(wallet, threshold=None):
    payload = {
        "wallet": wallet,
        **({"threshold": threshold} if threshold else {}),
    }
    r = call("wallet_balances", payload)
    for account, balances in r["balances"].items():
        for key in balances:
            r["balances"][account][key] = int(r["balances"][account][key])

    return r


def wallet_change_seed(wallet, seed, count=0):
    payload = {
        "wallet": wallet,
        "seed": seed,
        "count": count,
    }

    r = call("wallet_change_seed", payload)
    r["success"] = {}
    r["restored_count"] = int(r["restored_count"])
    return r


def wallet_contains(wallet, account):
    payload = {"wallet": wallet, "account": account}
    r = call("wallet_contains", payload)
    r["exists"] = int(r["exists"])

    return r


def wallet_create(seed=None):
    payload = {
        **({"seed": seed} if seed else {}),
    }
    return call("wallet_create", payload)


def wallet_destroy(wallet):
    payload = {"wallet": wallet}
    r = call("wallet_destroy", payload)
    r["destroyed"] = int(r["destroyed"])

    return r


def wallet_export(wallet):
    # FIXME:
    payload = {"wallet": wallet}
    return call("wallet_export", payload)


def wallet_frontiers(wallet):
    payload = {"wallet": wallet}
    return call("wallet_frontiers", payload)


def wallet_history(wallet, modified_since=0):
    # FIXME:
    payload = {
        "wallet": wallet,
        "modified_since": modified_since,
    }
    return call("wallet_history", payload)


def wallet_info(wallet):
    payload = {"wallet": wallet}
    r = call("wallet_info", payload)
    for key, value in r.items:
        r[key] = int(value)

    return r


def wallet_ledger(
    wallet, representative=False, weight=False, pending=False, modified_since=0
):
    # FIXME:
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
    r = call("wallet_lock", payload)
    r["locked"] = int(r["locked"])
    return r


def wallet_locked(wallet):
    payload = {"wallet": wallet}
    r = call("wallet_locked", payload)
    r["locked"] = int(r["locked"])
    return r


def wallet_pending(
    wallet,
    count=-1,
    threshold=None,
    source=False,
    include_active=False,
    min_version=False,
    include_only_confirmed=False,
):
    # FIXME:
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
    r = call("wallet_representative_set", payload)
    r["set"] = int(r["set"])

    return r


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
    r = call("work_set", payload)
    r["success"] = {}

    return r


def ban_from_raw(amount):
    return amount / 10 ** 29


def ban_to_raw(amount):
    return amount * (10 ** 29)


def ban_to_banoshi(amount):
    return amount * 100


def ban_from_banoshi(amount):
    return amount / 100
