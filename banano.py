import requests

API = 'http://45.32.180.42:7072'


def post_get(API, payload):
    resp = requests.post(API, json=payload)
    json_resp = resp.json()
    return json_resp


def get_account_balance(account):
    class Balance:
        balance = 0
        pending = 0
    balance = Balance()
    payload = {"action": "account_balance",
               "account": account}
    response = post_get(API, payload)
    balance.balance = response['balance']
    balance.pending = response['pending']
    return balance


def get_account_block_count(account):
    block_count = 0
    payload = {"action": "account_block_count",
               "account": account}
    response = post_get(API, payload)
    block_count = response['block_count']
    return block_count


def get_account(pub_key):
    payload = {"action": "account_get",
               "account": pub_key}
    response = post_get(API, payload)
    account = response['account']
    return account


def get_account_history(account, count, raw="false", head="", offset=0, reverse="false", account_filter=[]):
    class History:
        account = ""
        history = []
        previous = ""
    history = History()
    payload = {"action": "account_history",
               "account": account,
               "count": count}
    response = post_get(API, payload)
    history.account = response['account']
    history.history = response['history']
    history.history = response['previous']
    return history


def get_account_info(account, representative="false", weight="false", pending="false"):
    class Info:
        frontier = ""
        open_block = ""
        representative_block = ""
        balance = 0
        modified_timestamp = 0
        block_count = 0
        account_version = 0
    info = Info()
    payload = {"action": "account_info",
               "account": account,
               "representative": representative,
               "weight": weight,
               "pending": pending}
    response = post_get(API, payload)
    info.frontier = response['frontier']
    info.open_block = response['open_block']
    info.representative_block = response['representative_block']
    info.balance = response['balance']
    info.modified_timestamp = response['modified_timestamp']
    info.block_count = response['block_count']
    info.account_version = response['account_version']
    info.representative = response['representative']
    info.weight = response['weight']
    info.pending = response['pending']
    return info


def get_account_key(account):
    payload = {"action": "account_key",
               "account": account}
    response = post_get(API, payload)
    pub_key = response['key']
    return pub_key


def get_representative(account):
    payload = {"action": "account_representative",
               "account": account}
    response = post_get(API, payload)
    representative = response['representative']
    return representative


def get_weight(account):
    payload = {"action": "account_weight",
               "account": account}
    response = post_get(API, payload)
    weight = response['weight']
    return weight


def get_accounts_balances(accounts):
    payload = {"action": "accounts_balances",
               "account": accounts}
    response = post_get(API, payload)
    balances = response['balances']
    return balances


def get_accounts_frontiers(accounts):
    payload = {"action": "accounts_frontiers",
               "account": accounts}
    response = post_get(API, payload)
    frontiers = response['frontiers']
    return frontiers


def get_accounts_pending(accounts, threshold=0, source="false", include_active="false", sorting="false", include_only_confirmed="false"):
    payload = {"action": "accounts_pending",
               "account": accounts,
               "threshold": threshold,
               "source": source,
               "include_active": include_active,
               "sorting": sorting,
               "include_only_confirmed": include_only_confirmed}
    response = post_get(API, payload)
    blocks = response['blocks']
    return blocks


def get_active_difficulty(include_trend="false"):
    class Difficulty:
        network_minimum = ""
        network_current = ""
        multiplier = ""
        difficulty_trend = []
    difficulty = Difficulty()
    payload = {"action": "active_difficulty",
               "include_trend": include_trend}
    response = post_get(API, payload)
    difficulty.network_minimum = response['network_minimum']
    difficulty.network_current = response['network_current']
    difficulty.multiplier = response['multiplier']
    difficulty.difficulty_trend = response['difficulty_trend']
    return difficulty


def get_available_supply():
    payload = {"action": "available_supply"}
    response = post_get(API, payload)
    supply = response['available']
    return supply


def get_block_account(block_hash):
    payload = {"action": "block_account",
               "hash": block_hash}
    response = post_get(API, payload)
    account = response['account']
    return account


def get_block_confirm(block_hash):
    payload = {"action": "block_confirm",
               "hash": block_hash}
    response = post_get(API, payload)
    started = response['started']
    return started


def get_block_count(include_cemented="true"):
    class BlockCount:
        count = 0
        unchecked = 0
        cemented = 0
    count = BlockCount()
    payload = {"action": "block_count",
               "include_cemented": include_cemented}
    response = post_get(API, payload)
    count.count = response['count']
    count.unchecked = response['unchecked']
    count.cemented = response['cemented']
    return count


def get_block_count_type():
    class BlockCount:
        send = 0
        receive = 0
        open = 0
        change = 0
        state_v0 = 0
        state_v1 = 0
        state = 0
    count = BlockCount()
    payload = {"action": "block_count_type"}
    response = post_get(API, payload)
    count.send = response['send']
    count.receive = response['receive']
    count.open = response['open']
    count.change = response['change']
    count.state_v0 = response['state_v0']
    count.state_v1 = response['state_v1']
    count.state = response['state']
    return count


def create_block(block_type, balance, key, representative, link, previous):
    class Block:
        block_hash = ""
        difficulty = ""
        block = []
    block = Block()
    payload = {"action": "block_create",
               "type": block_type,
               "balance": balance,
               "key": key,
               "representative": representative,
               "link": link,
               "previous": previous}
    response = post_get(API, payload)
    block.block_hash = response['hash']
    block.difficulty = response['difficulty']
    block.block = response['block']
    return block


def get_hash(block_type, account, previous, representative, balance, link, link_as_account, signature, work):

    payload = {"action": "block_hash",
               "block": {
                   "type": block_type,
                   "account": account,
                   "previous": previous,
                   "representative": representative,
                   "balance": balance,
                   "link": link,
                   "link_as_account": link_as_account,
                   "signature": signature,
                   "work": work}
               }
    response = post_get(API, payload)
    block_hash = response['hash']
    return block_hash


def get_block_info(block_hash):
    class Block:
        block_account = ""
        amount = 0
        balance = 0
        height = 0
        local_timestamp = 0
        confirmed = ""
        contents = []
        subtype = ""
    block = Block()
    payload = {"action": "block_info",
               "hash": block_hash}
    response = post_get(API, payload)
    block.block_account = response['block_account']
    block.amount = response['amount']
    block.balance = response['balance']
    block.height = response['height']
    block.local_timestamp = response['local_timestamp']
    block.confirmed = response['confirmed']
    block.contents = response['contents']
    block.subtype = response['subtype']
    return block


def get_blocks(hashes):
    payload = {"action": "blocks",
               "hashes": hashes}
    response = post_get(API, payload)
    blocks = response['blocks']
    return blocks


def get_blocks_info(hashes, include_not_found="false", pending="false", source="false", balance="false"):
    payload = {"action": "blocks_info",
               "include_not_found": include_not_found,
               "hashes": hashes,
               "pending": pending,
               "source": source,
               "balance": balance}
    response = post_get(API, payload)
    blocks = response['blocks']
    return blocks


def bootstrap(address, port):
    payload = {"action": "bootstrap",
               "address": address,
               "port": port}
    response = post_get(API, payload)
    success = response["success"]
    return success


def bootstrap_any():
    payload = {"action": "bootstrap_any"}
    response = post_get(API, payload)
    success = response["success"]
    return success


def bootstrap_lazy(block_hash):
    payload = {"action": "bootstrap_any",
               "hash": block_hash}
    response = post_get(API, payload)
    started = response["started"]
    return started


def get_bootstrap_status():
    class Status:
        clients = 0
        pulls = 0
        pulling = 0
        connections = 0
        idle = 0
        target_connections = 0
        total_blocks = 0
        runs_count = 0
        requeued_pulls = 0
        frontiers_received = ""
        frontiers_confirmed = ""
        mode = ""
        lazy_blocks = 0
        lazy_state_backlog = 0
        lazy_balances = 0
        lazy_destinations = 0
        lazy_undefined_links = 0
        lazy_pulls = 0
        lazy_keys = 0
        lazy_key_1 = ""
        duration = 0
    status = Status()
    payload = {"action": "bootstrap_status"}
    response = post_get(API, payload)
    status.clients = response["clients"]
    status.pulls = response["pulls"]
    status.pulling = response["pulling"]
    status.connections = response["connections"]
    status.idle = response["idle"]
    status.target_connections = response["target_connections"]
    status.total_blocks = response["total_blocks"]
    status.runs_count = response["runs_count"]
    status.requeued_pulls = response["requeued_pulls"]
    status.frontiers_received = response["frontiers_received"]
    status.frontiers_confirmed = response["frontiers_confirmed"]
    status.mode = response["mode"]
    status.lazy_blocks = response["lazy_blocks"]
    status.lazy_state_backlog = response["lazy_state_backlog"]
    status.lazy_balances = response["lazy_balances"]
    status.lazy_destinations = response["lazy_destinations"]
    status.lazy_undefined_links = response["lazy_undefined_links"]
    status.lazy_pulls = response["lazy_pulls"]
    status.lazy_keys = response["lazy_keys"]
    status.lazy_key_1 = response["lazy_key_1"]
    status.duration = response["duration"]
    return status


def get_chain(block_hash, count=-1):
    payload = {"action": "chain",
               "block": block_hash,
               "count": count}
    response = post_get(API, payload)
    blocks = response["blocks"]
    return blocks


def get_confirmation_active(announcements=0):
    class Confirmations:
        confirmations = []
        unconfirmed = 0
        confirmed = 0
    confirmations = Confirmations()
    payload = {"action": "confirmation_active",
               "announcements": announcements}
    response = post_get(API, payload)
    confirmations.confirmations = response["confirmations"]
    confirmations.unconfirmed = response["unconfirmed"]
    confirmations.confirmed = response["confirmed"]
    return confirmations


def get_confirmation_height_currently_processing():
    payload = {"action": "confirmation_height_currently_processing"}
    response = post_get(API, payload)
    block_hash = response["hash"]
    return block_hash


def get_confirmation_history():
    class Confirmations:
        count = 0
        average = 0
        confirmations = []
    confirmations = Confirmations()
    payload = {"action": "confirmation_history"}
    response = post_get(API, payload)
    confirmations.count = response["confirmation_stats"]["count"]
    confirmations.average = response["confirmation_stats"]["average"]
    confirmations.confirmations = response["confirmations"]
    return confirmations


def get_confirmation_info():
    class Info:
        announcements = 0
        voters = 0
        last_winner = ""
        total_tally = ""
        blocks = []
    info = Info()
    payload = {"action": "confirmation_info"}
    response = post_get(API, payload)
    info.announcements = response["announcements"]
    info.voters = response["voters"]
    info.last_winner = response["last_winner"]
    info.total_tally = response["total_tally"]
    info.blocks = response["blocks"]
    return info


def get_confirmation_quorum():
    class Quorum:
        quorum_delta = 0
        online_weight_quorum_percent = 0
        online_weight_minimum = 0
        online_stake_total = 0
        peers_stake_total = 0
        peers_stake_required = 0
        peers = []
    quorum = Quorum()
    payload = {"action": "confirmation_history"}
    response = post_get(API, payload)
    quorum.quorum_delta = response["quorum_delta"]
    quorum.online_weight_quorum_percent = response["online_weight_quorum_percent"]
    quorum.online_weight_minimum = response["online_weight_minimum"]
    quorum.online_stake_total = response["online_stake_total"]
    quorum.peers_stake_total = response["peers_stake_total"]
    quorum.peers_stake_required = response["peers_stake_required"]
    quorum.peers = response["peers"]
    return quorum


def get_database_txn_tracker():
    payload = {"action": "database_txn_tracker"}
    response = post_get(API, payload)
    txn_tracking = response["txn_tracking"]
    return txn_tracking


def get_delegators(account):
    payload = {"action": "get_delegators",
               "account": account}
    response = post_get(API, payload)
    delegators = response["delegators"]
    return delegators


def get_delegators_count(account):
    payload = {"action": "get_delegators_count",
               "account": account}
    response = post_get(API, payload)
    count = response["count"]
    return count


def get_deteministic_key(seed, index=0):
    class Keys:
        private = ""
        public = ""
        account = ""
    keys = Keys()
    payload = {"action": "deterministic_key",
               "seed": seed,
               "index": index}
    response = post_get(API, payload)
    keys.private = response["private"]
    keys.public = response["public"]
    keys.account = response["account"]
    return keys


def get_frontiers_count():
    payload = {"action": "get_frontiers_count"}
    response = post_get(API, payload)
    count = response["count"]
    return count


def get_frontiers(account, count=-1):
    payload = {"action": "get_frontiers",
               "account": account,
               "count": count}
    response = post_get(API, payload)
    frontiers = response["frontiers"]
    return frontiers


def keepalive(address, port):
    payload = {"action": "keepalive",
               "address": address,
               "port": port}
    response = post_get(API, payload)
    started = response['started']
    return started


def get_key_create():
    class Keys:
        private = ""
        public = ""
        account = ""
    keys = Keys()
    payload = {"action": "key_create"}
    response = post_get(API, payload)
    keys.private = response["private"]
    keys.public = response["public"]
    keys.account = response["account"]
    return keys


def get_key_expand(private_key):
    class Keys:
        private = ""
        public = ""
        account = ""
    keys = Keys()
    payload = {"action": "key_expand",
               "key": private_key}
    response = post_get(API, payload)
    keys.private = response["private"]
    keys.public = response["public"]
    keys.account = response["account"]
    return keys


def get_ledger(account, count=-1, representative="false", weight="false", pending="false", modified_since=0, sorting="false"):
    payload = {"action": "ledger",
               "account": account,
               "count": count,
               "representative": representative,
               "weight": weight,
               "pending": pending,
               "modified_since": modified_since,
               "sorting": sorting
               }
    response = post_get(API, payload)
    accounts = response['accounts']
    return accounts


def get_node_id():
    class Keys:
        private = ""
        public = ""
        as_account = ""
        node_id = ""
    keys = Keys()
    payload = {"action": "node_id"}
    response = post_get(API, payload)
    keys.private = response["private"]
    keys.public = response["public"]
    keys.as_account = response["as_account"]
    keys.node_id = response["node_id"]
    return keys


def node_id_delete():
    payload = {"action": "node_id_delete"}
    response = post_get(API, payload)
    deprecated = response["deprecated"]
    return deprecated


def get_peers(peer_details="false"):
    payload = {"action": "peers",
               "peer_details": peer_details}
    response = post_get(API, payload)
    peers = response["peers"]
    return peers


def get_pending(count=-1, threshold=0, source="false", include_active="false", min_version="false", sorting="false", include_only_confirmed="false"):
    payload = {"action": "pending",
               "count": count,
               "threshold": threshold,
               "source": source,
               "include_active": include_active,
               "min_version": min_version,
               "sorting": sorting,
               "include_only_confirmed": include_only_confirmed}
    response = post_get(API, payload)
    blocks = response["blocks"]
    return blocks


def pending_exists(block_hash, include_active="false", include_only_confirmed="false"):
    payload = {"action": "pending_exists",
               "hash": block_hash,
               "include_active": include_active,
               "include_only_confirmed": include_only_confirmed}
    response = post_get(API, payload)
    exists = response["exists"]
    return exists


def process(block_type, account, previous, representative, balance, link, link_as_account, signature, work, subtype="", force="false"):
    payload = {"action": "process",
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
                   "work": work},
               "force": force
               }
    response = post_get(API, payload)
    exists = response["exists"]
    return exists


def get_representatives(count=-1, sorting="false"):
    payload = {"action": "representatives",
               "count": count,
               "sorting": sorting}
    response = post_get(API, payload)
    representatives = response["representatives"]
    return representatives


def get_representatives_online(weight="false"):
    payload = {"action": "representatives_online",
               "weight": weight}
    response = post_get(API, payload)
    representatives = response["representatives"]
    return representatives


def republish(block_hash, sources="false", destinations="false"):
    payload = {"action": "republish",
               "hash": block_hash,
               "sources": sources,
               "destinations": destinations}
    response = post_get(API, payload)
    blocks = response["blocks"]
    return blocks


def sign_key(private_key, block_type, account, previous_block, representative, balance, link, link_as_account, signature, work):
    class Signed:
        signature = ""
        block = []
    signed = Signed()
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
            "work": work}
    }
    response = post_get(API, payload)
    signed.signature = response["signature"]
    signed.block = response["block"]
    return signed


def sign_wallet(wallet, block_type, account, previous_block, representative, balance, link, link_as_account, signature, work):
    class Signed:
        signature = ""
        block = []
    signed = Signed()
    payload = {
        "action": "sign",
        "walllet": wallet,
        "account": account,
        "block": {
            "type": block_type,
            "account": account,
            "previous": previous_block,
            "representative": representative,
            "balance": balance,
            "link": link,
            "link_as_account": link_as_account,
            "signature": signature,
            "work": work}
    }
    response = post_get(API, payload)
    signed.signature = response["signature"]
    signed.block = response["block"]
    return signed


# types are "samples", "objects"
def get_stats(stat_type):
    payload = {"action": "stats",
               "type": stat_type}
    response = post_get(API, payload)
    stats = response
    return stats


def stats_clear():
    payload = {"action": "stats_clear"}
    response = post_get(API, payload)
    success = response['success']
    return success


def stop_node():
    payload = {"action": "stop"}
    response = post_get(API, payload)
    success = response['success']
    return success


def get_successors(block_hash, count=-1, offset=0, reverse="false"):
    payload = {
        "action": "successors",
        "block": block_hash,
        "count": count,
        "offset": offset,
        "reverse": reverse}
    response = post_get(API, payload)
    blocks = response['blocks']
    return blocks


def validate_account_number(account):
    payload = {"action": "validate_account_number",
               "account": account}
    response = post_get(API, payload)
    valid = response['valid']
    return valid


def get_version():
    class Version:
        rpc_version = 0
        store_version = 0
        protocol_version = 0
        node_vendor = ""
        store_vendor = ""
        network = ""
        network_identifier = ""
        build_info = ""
    version = Version()
    payload = {"action": "version"}
    response = post_get(API, payload)
    version.rpc_version = response['rpc_version']
    version.store_version = response['store_version']
    version.protocol_version = response['protocol_version']
    version.node_vendor = response['node_vendor']
    version.store_vendor = response['store_vendor']
    version.network = response['network']
    version.network_identifier = response['network_identifier']
    version.build_info = response['build_info']
    return version


def get_all_unchecked(count=-1):
    payload = {"action": "unchecked",
               "count": count}
    response = post_get(API, payload)
    blocks = response['blocks']
    return blocks


def unchecked_clear():
    payload = {"action": "unchecked_clear"}
    response = post_get(API, payload)
    success = response['success']
    return success


def get_unchecked(block_hash):
    class Block:
        modified_timestamp = 0
        contents = []
    block = Block()
    payload = {"action": "unchecked_get",
               "hash": block_hash}
    response = post_get(API, payload)
    block.modified_timestamp = response['modified_timestamp']
    block.contents = response["contents"]
    return block


def get_unchecked_keys(key, count=-1):
    payload = {"action": "unchecked_keys",
               "key": key,
               "count": count}
    response = post_get(API, payload)
    unchecked = response['unchecked']
    return unchecked


def get_unopened(account, count=-1, threshold=0):
    payload = {"action": "unopened",
               "account": account,
               "count": count,
               "threshold": threshold}
    response = post_get(API, payload)
    accounts = response['accounts']
    return accounts


def get_uptime():
    payload = {"action": "uptime"}
    response = post_get(API, payload)
    seconds = response['seconds']
    return seconds


def work_cancel(block_hash):
    payload = {"action": "work_cancel",
               "hash": block_hash}
    response = post_get(API, payload)


def work_generate(block_hash, use_peers="false"):
    class Work:
        work = ""
        difficulty = ""
        multiplier = ""
        block_hash = ""
    work = Work()
    payload = {"action": "work_generate",
               "hash": block_hash,
               "use_peers": use_peers}
    response = post_get(API, payload)
    work.work = response['work']
    work.difficulty = response['difficulty']
    work.multiplier = response['multiplier']
    work.block_hash = response['hash']
    return work


def work_peer_add(address, port):
    payload = {
        "action": "work_peer_add",
        "address": address,
        "port": port}
    response = post_get(API, payload)
    success = response['success']
    return success


def get_work_peers():
    payload = {"action": "work_peers"}
    response = post_get(API, payload)
    work_peers = response['work_peers']
    return work_peers


def work_peers_clear():
    payload = {"action": "work_peers_clear"}
    response = post_get(API, payload)
    success = response['success']
    return success


def account_create(wallet, index=0, work="true"):
    payload = {
        "action": "account_create",
        "wallet": wallet,
        "index": index,
        "work": work}
    response = post_get(API, payload)
    account = response['account']
    return account


def get_account_list(wallet):
    payload = {
        "action": "account_list",
        "wallet": wallet}
    response = post_get(API, payload)
    accounts = response['accounts']
    return accounts


def account_move(wallet, source, accounts):
    payload = {"action": "account_move",
               "wallet": wallet,
               "source": source,
               "accounts": accounts}
    response = post_get(API, payload)
    moved = response['moved']
    return moved


def account_remove(wallet, account):
    payload = {"action": "account_remove",
               "wallet": wallet,
               "account": account}
    response = post_get(API, payload)
    removed = response['removed']
    return removed


def set_account_representative(wallet, account, representative):
    payload = {"action": "account_representative_set",
               "wallet": wallet,
               "account": account,
               "representative": representative}
    response = post_get(API, payload)
    block = response['block']
    return block


def accounts_create(wallet, count, work="true"):
    payload = {
        "action": "accounts_create",
        "wallet": wallet,
        "count": count,
        "work": work}
    response = post_get(API, payload)
    accounts = response['accounts']
    return accounts


def set_password(wallet, password):
    payload = {"action": "password_change",
               "wallet": wallet,
               "password": password}
    response = post_get(API, payload)
    changed = response['changed']
    return changed


def password_enter(wallet, password):
    payload = {"action": "password_enter",
               "wallet": wallet,
               "password": password}
    response = post_get(API, payload)
    valid = response['valid']
    return valid


def receive(wallet, account, block):
    payload = {
        "action": "receive",
        "wallet": wallet,
        "account": account,
        "block": block}
    response = post_get(API, payload)
    block = response['block']
    return block


def get_receive_minimum():
    payload = {"action": "receive_minimum"}
    response = post_get(API, payload)
    amount = response['amount']
    return amount


def set_receive_minimum(amount):
    payload = {"action": "receive_minimum_set",
               "amount": amount}
    response = post_get(API, payload)
    success = response['success']
    return success


def search_pending(wallet):
    payload = {"action": "search_pending",
               "wallet": wallet}
    response = post_get(API, payload)
    started = response['started']
    return started


def search_pending_all():
    payload = {"action": "search_pending_all"}
    response = post_get(API, payload)
    success = response['success']
    return success


def send(wallet, source, destination, amount):
    payload = {
        "action": "send",
        "wallet": wallet,
        "source": source,
        "destination": destination,
        "amount": amount}
    response = post_get(API, payload)
    block = response['block']
    return block


def wallet_add(wallet, key, work="false"):
    payload = {
        "action": "wallet_add",
        "wallet": wallet,
        "key": key,
        "work": work}
    response = post_get(API, payload)
    account = response['account']
    return account


def wallet_add_watch(wallet, accounts):
    payload = {
        "action": "wallet_add_watch",
        "wallet": wallet,
        "accounts": accounts}
    response = post_get(API, payload)
    success = response['success']
    return success


def wallet_balances(wallet):
    payload = {
        "action": "wallet_balances",
        "wallet": wallet}
    response = post_get(API, payload)
    balances = response['balances']
    return balances


def wallet_change_seed(wallet, seed):
    class Success:
        success = ""
        last_restored_account = ""
        restored_count = 0
    success = Success()
    payload = {
        "action": "wallet_change_seed",
        "wallet": wallet,
        "seed": seed}
    response = post_get(API, payload)
    success.success = response['success']
    success.success = response['last_restored_account']
    success.success = response['restored_count']
    return success


def wallet_contains(wallet, account):
    payload = {
        "action": "wallet_contains",
        "wallet": wallet,
        "account": account}
    response = post_get(API, payload)
    exists = response['exists']
    return exists


def wallet_create():
    payload = {
        "action": "wallet_create"}
    response = post_get(API, payload)
    wallet = response['wallet']
    return wallet


def seed_wallet_create(seed):
    payload = {
        "action": "wallet_create",
        "seed": seed}
    response = post_get(API, payload)
    wallet = response['wallet']
    return wallet


def wallet_destroy(wallet):
    payload = {
        "action": "wallet_destroy",
        "wallet": wallet}
    response = post_get(API, payload)
    destroyed = response['destroyed']
    return destroyed


def wallet_export(wallet):
    payload = {
        "action": "wallet_export",
        "wallet": wallet}
    response = post_get(API, payload)
    json = response['json']
    return json


def get_wallet_frontiers(wallet):
    payload = {
        "action": "wallet_frontiers",
        "wallet": wallet}
    response = post_get(API, payload)
    frontiers = response['frontiers']
    return frontiers


def get_wallet_history(wallet, modified_since=0):
    payload = {
        "action": "wallet_history",
        "wallet": wallet,
        "modified_since": modified_since}
    response = post_get(API, payload)
    history = response['history']
    return history


def wallet_info(wallet):
    class Info:
        balance = 0
        pending = 0
        accounts_count = 0
        adhoc_count = 0
        deterministic_count = 0
        deterministic_index = 0
    info = Info()
    payload = {
        "action": "wallet_info",
        "wallet": wallet}
    response = post_get(API, payload)
    info.balance = response['balance']
    info.pending = response['pending']
    info.accounts_count = response['accounts_count']
    info.adhoc_count = response['adhoc_count']
    info.deterministic_count = response['deterministic_count']
    info.deterministic_index = response['deterministic_index']
    return info


def get_wallet_ledger(wallet, representative="false", weight="false", pending="false", modified_since=0):
    payload = {
        "action": "wallet_ledger",
        "wallet": wallet,
        "representative": representative,
        "weight": weight,
        "pending": pending,
        "modified_since": modified_since}
    response = post_get(API, payload)
    accounts = response['accounts']
    return accounts


def wallet_lock(wallet):
    payload = {
        "action": "wallet_lock",
        "wallet": wallet}
    response = post_get(API, payload)
    locked = response['locked']
    return locked


def get_wallet_locked(wallet):
    payload = {
        "action": "wallet_locked",
        "wallet": wallet}
    response = post_get(API, payload)
    locked = response['locked']
    return locked


def get_wallet_pending(wallet, count=-1, threshold=0, source="false", include_active="false", min_version="false", include_only_confirmed="false"):
    payload = {
        "action": "wallet_pending",
        "wallet": wallet,
        "count": count,
        "threshold": threshold,
        "source": source,
        "include_active": include_active,
        "min_version": min_version,
        "include_only_confirmed": include_only_confirmed}
    response = post_get(API, payload)
    blocks = response['blocks']
    return blocks


def get_wallet_representative(wallet):
    payload = {
        "action": "wallet_representative",
        "wallet": wallet}
    response = post_get(API, payload)
    representative = response['representative']
    return representative


def set_wallet_representative(wallet, representative, update_existing_accounts="false"):
    payload = {
        "action": "wallet_representative_set",
        "wallet": wallet,
        "representative": representative,
        "update_existing_accounts": update_existing_accounts}
    response = post_get(API, payload)
    success = response['set']
    return success


def wallet_republish(wallet, count=-1):
    payload = {
        "action": "wallet_history",
        "wallet": wallet,
        "count": count}
    response = post_get(API, payload)
    blocks = response['blocks']
    return blocks


def get_wallet_work(wallet):
    payload = {
        "action": "wallet_work_get",
        "wallet": wallet}
    response = post_get(API, payload)
    works = response['works']
    return works


def get_work(wallet, account):
    payload = {
        "action": "get_work",
        "wallet": wallet,
        "account": account}
    response = post_get(API, payload)
    work = response['work']
    return work


def set_work(wallet, account, work):
    payload = {
        "action": "get_work",
        "wallet": wallet,
        "account": account,
        "work": work}
    response = post_get(API, payload)
    success = response['success']
    return success


def ban_from_raw(amount):
    amount = amount/10**29
    return amount


def ban_to_raw(amount):
    amount = amount*(10**29)
    return amount


def ban_to_banoshi(amount):
    amount = amount*100
    return amount


def ban_from_banoshi(amount):
    amount = amount/100
    return amount

