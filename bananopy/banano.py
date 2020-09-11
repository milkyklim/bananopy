import requests
from collections import defaultdict

from bananopy.constants import BANANO_API
from bananopy.utils import fix_json
from bananopy.conversion import convert


class NodeException(Exception):
    """ Base class for RPC errors """


def call(action, params=None, url=BANANO_API):
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
    return fix_json(r)


def account_block_count(account):
    payload = {"account": account}
    r = call("account_block_count", payload)
    return fix_json(r)


def account_get(pub_key):
    payload = {"key": pub_key}
    return call("account_get", payload)


def account_history(
    account, count, raw=False, head="", offset=0, reverse=False, account_filter=[]
):
    payload = {
        "account": account,
        "count": count,
        "raw": raw,
        **({"head": head} if head != "" else {}),
        "offset": offset,
        "reverse": reverse,
        **({"account_filter": account_filter} if account_filter != [] else {}),
    }

    r = call("account_history", payload)
    r = fix_json(r)

    # hack to keep data structures consistent
    if r["history"] == {}:
        r["history"] = []

    return r


def account_info(account, representative=False, weight=False, pending=False):
    payload = {
        "account": account,
        "representative": representative,
        "weight": weight,
        "pending": pending,
    }
    r = call("account_info", payload)
    return fix_json(r)


def account_key(account):
    payload = {"account": account}
    return call("account_key", payload)


def account_representative(account):
    payload = {"account": account}
    return call("account_representative", payload)


def account_weight(account):
    payload = {"account": account}
    r = call("account_weight", payload)
    return fix_json(r)


def accounts_balances(accounts):
    payload = {"accounts": accounts}
    r = call("accounts_balances", payload)
    return fix_json(r)


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
    r = call("accounts_pending", payload)
    return fix_json(r)


def active_difficulty(include_trend=False):
    payload = {"include_trend": include_trend}
    r = call("active_difficulty", payload)
    return fix_json(r)


def available_supply():
    r = call("available_supply")
    return fix_json(r)


def block_account(hash):
    payload = {"hash": hash}
    return call("block_account", payload)


def block_confirm(hash):
    payload = {"hash": hash}
    r = call("block_confirm", payload)
    return fix_json(r)


def block_count(include_cemented=True):
    payload = {"include_cemented": include_cemented}
    r = call("block_count", payload)
    return fix_json(r)


def block_count_type():
    r = call("block_count_type")
    return fix_json(r)


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
    return fix_json(r)


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
    return fix_json(r)


def blocks(hashes, json_block=False):
    payload = {
        "json_block": json_block,
        "hashes": hashes,
    }
    r = call("blocks", payload)
    return fix_json(r)


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
    return fix_json(r)


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
    r = call("bootstrap_status")
    return fix_json(r)


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
    payload = {
        **({"hash": hash} if hash else {}),
    }
    r = call("confirmation_history", payload)
    return fix_json(r)


def confirmation_info(root, representatives=False, contents=False, json_block=False):
    payload = {
        "json_block": json_block,
        "root": root,
        "contents": contents,
        "representatives": representatives,
    }
    r = call("confirmation_info", payload)
    return fix_json(r)


def confirmation_quorum(peer_details=False, peers_stake_required=0):
    payload = {
        "peer_details": peer_details,
        "peers_stake_required": peers_stake_required,
    }
    r = call("confirmation_quorum", payload)
    return fix_json(r)


def database_txn_tracker():
    r = call("database_txn_tracker")
    return fix_json(r)


def delegators(account):
    payload = {"account": account}
    r = call("delegators", payload)
    return fix_json(r)


def delegators_count(account):
    payload = {"account": account}
    r = call("delegators_count", payload)
    return fix_json(r)


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
    return fix_json(r)


def frontier_count():
    r = call("frontier_count")
    return fix_json(r)


def frontiers(account, count=-1):
    payload = {"account": account, "count": count}
    return call("frontiers", payload)


def keepalive(address, port):
    payload = {"address": address, "port": port}
    r = call("keepalive", payload)
    return fix_json(r)


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
    r = call("ledger", payload)
    return fix_json(r)


def node_id():
    return call("node_id")


def node_id_delete():
    r = call("node_id_delete")
    return fix_json(r)


# version 21.0+
# def node_telemetry():
#     return call("node_telemetry")


def peers(peer_details=False):
    payload = {"peer_details": peer_details}
    r = call("peers", payload)
    return fix_json(r)


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
    r = call("pending", payload)
    return fix_json(r)


def pending_exists(hash, include_active=False, include_only_confirmed=False):
    payload = {
        "hash": hash,
        "include_active": include_active,
        "include_only_confirmed": include_only_confirmed,
    }
    r = call("pending_exists", payload)
    return fix_json(r)


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
    r = call("representatives", payload)
    return fix_json(r)


def representatives_online(weight=False):
    payload = {"weight": weight}
    r = call("representatives_online", payload)
    return fix_json(r)


def republish(hash, sources=False, destinations=False):
    payload = {
        "hash": hash,
        "sources": sources,
        "destinations": destinations,
    }
    return call("republish", payload)


def sign(
    block_type=None,
    previous_block=None,
    representative=None,
    balance=None,
    link=None,
    link_as_account=None,
    signature=None,
    work=None,
    hash=None,
    key=None,
    wallet=None,
    account=None,
    json_block=False,
):
    # distinguish between hash sign and block sign
    payload = (
        {"hash": hash}
        if hash is not None
        else {
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
    )
    r = call("sign", payload)
    return fix_json(r)


def stats(stats_type):
    payload = {"type": stats_type}
    r = call("stats", payload)
    return fix_json(r)


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
    return fix_json(r)


def version():
    r = call("version")
    return fix_json(r)


def unchecked(count=-1, json_block=False):
    payload = {"count": count, "json_block": json_block}
    r = call("unchecked", payload)
    return fix_json(r)


def unchecked_clear():
    r = call("unchecked_clear")
    return fix_json(r)


def unchecked_get(hash, json_block=False):
    payload = {"hash": hash, "json_block": json_block}
    r = call("unchecked_get", payload)
    return fix_json(r)


def unchecked_keys(key, count=-1, json_block=False):
    payload = {
        "key": key,
        "count": count,
        "json_block": json_block,
    }
    r = call("unchecked_keys", payload)
    return fix_json(r)


def unopened(account, count=-1, threshold=0):
    payload = {
        "account": account,
        "count": count,
        "threshold": threshold,
    }
    r = call("unopened", payload)
    return fix_json(r)


def uptime():
    r = call("uptime")
    return fix_json(r)


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
    return fix_json(r)


def work_peers():
    return call("work_peers")


def work_peers_clear():
    r = call("work_peers_clear")
    return fix_json(r)


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
    return fix_json(r)


def account_remove(wallet, account):
    payload = {"wallet": wallet, "account": account}
    r = call("account_remove", payload)
    return fix_json(r)


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
    return fix_json(r)


def password_enter(wallet, password):
    payload = {"wallet": wallet, "password": password}
    r = call("password_enter", payload)
    return fix_json(r)


def password_valid(wallet):
    payload = {"wallet": wallet}
    r = call("password_valid", payload)
    return fix_json(r)


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
    return fix_json(r)


def receive_minimum_set(amount):
    payload = {"amount": amount}
    r = call("receive_minimum_set", payload)
    return fix_json(r)


def search_pending(wallet):
    payload = {"wallet": wallet}
    r = call("search_pending", payload)
    return fix_json(r)


def search_pending_all():
    r = call("search_pending_all")
    return fix_json(r)


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
    return fix_json(r)


def wallet_balances(wallet, threshold=None):
    payload = {
        "wallet": wallet,
        **({"threshold": threshold} if threshold else {}),
    }
    r = call("wallet_balances", payload)
    return fix_json(r)


def wallet_change_seed(wallet, seed, count=0):
    payload = {
        "wallet": wallet,
        "seed": seed,
        "count": count,
    }
    r = call("wallet_change_seed", payload)
    return fix_json(r)


def wallet_contains(wallet, account):
    payload = {"wallet": wallet, "account": account}
    r = call("wallet_contains", payload)
    return fix_json(r)


def wallet_create(seed=None):
    payload = {
        **({"seed": seed} if seed else {}),
    }
    return call("wallet_create", payload)


def wallet_destroy(wallet):
    payload = {"wallet": wallet}
    r = call("wallet_destroy", payload)
    return fix_json(r)


def wallet_export(wallet):
    payload = {"wallet": wallet}
    r = call("wallet_export", payload)
    return fix_json(r)


def wallet_frontiers(wallet):
    payload = {"wallet": wallet}
    return call("wallet_frontiers", payload)


def wallet_history(wallet, modified_since=0):
    payload = {
        "wallet": wallet,
        "modified_since": modified_since,
    }
    r = call("wallet_history", payload)
    return fix_json(r)


def wallet_info(wallet):
    payload = {"wallet": wallet}
    r = call("wallet_info", payload)
    return fix_json(r)


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
    r = call("wallet_ledger", payload)
    return fix_json(r)


def wallet_lock(wallet):
    payload = {"wallet": wallet}
    r = call("wallet_lock", payload)
    return fix_json(r)


def wallet_locked(wallet):
    payload = {"wallet": wallet}
    r = call("wallet_locked", payload)
    return fix_json(r)


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
    r = call("wallet_pending", payload)
    return fix_json(r)


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
    return fix_json(r)


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
    return fix_json(r)


# shortcuts
def ban_from_raw(amount):
    return convert(amount, "raw", "ban")


def ban_to_raw(amount):
    return convert(amount, "ban", "raw")


def ban_to_banoshi(amount):
    return convert(amount, "ban", "banoshi")


def ban_from_banoshi(amount):
    return convert(amount, "banoshi", "ban")
