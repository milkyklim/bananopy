import bananopy.banano as ban
import json
import os


def unfold_keys(dictionary):
    r = []
    for k, v in dictionary.items():
        if isinstance(v, dict):
            r += unfold_keys(v)
            continue
        if isinstance(v, list):
            for el in v:
                r += unfold_keys(el)
            continue
        r.append(k)
    return r


def load_rpc_tests(folder="public"):
    jsons_directory = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "fixtures", folder
    )

    result = {}
    for filename in os.listdir(jsons_directory):
        if filename.endswith(".json"):
            action = filename[: -len(".json")]
            try:
                tests = json.load(open(os.path.join(jsons_directory, filename)))
            except Exception:
                print("Failed to load %s test" % filename)
                raise
            result[action] = tests
    return result


methods = {
    "account_balance": ban.account_balance,
    "account_block_count": ban.account_block_count,
    "account_get": ban.account_get,
    "account_history": ban.account_history,
    "account_info": ban.account_info,
    "account_key": ban.account_key,
    "account_representative": ban.account_representative,
    "account_weight": ban.account_weight,
    "accounts_balances": ban.accounts_balances,
    "accounts_frontiers": ban.accounts_frontiers,
    "accounts_pending": ban.accounts_pending,
    "active_difficulty": ban.active_difficulty,
    "available_supply": ban.available_supply,
    "block_account": ban.block_account,
    "block_confirm": ban.block_confirm,
    "block_count": ban.block_count,
    "block_count_type": ban.block_count_type,
    "block_create": ban.block_create,
    "block_hash": ban.block_hash,
    "block_info": ban.block_info,
    "blocks": ban.blocks,
    "blocks_info": ban.blocks_info,
    "bootstrap": ban.bootstrap,
    "bootstrap_any": ban.bootstrap_any,
    "bootstrap_lazy": ban.bootstrap_lazy,
    "bootstrap_status": ban.bootstrap_status,
    "chain": ban.chain,
    "confirmation_active": ban.confirmation_active,
    "confirmation_height_currently_processing": (
        ban.confirmation_height_currently_processing
    ),
    "confirmation_history": ban.confirmation_history,
    "confirmation_info": ban.confirmation_info,
    "confirmation_quorum": ban.confirmation_quorum,
    "database_txn_tracker": ban.database_txn_tracker,
    "delegators": ban.delegators,
    "delegators_count": ban.delegators_count,
    "deteministic_key": ban.deteministic_key,
    "epoch_upgrade": ban.epoch_upgrade,
    "frontier_count": ban.frontier_count,
    "frontiers": ban.frontiers,
    "keepalive": ban.keepalive,
    "key_create": ban.key_create,
    "key_expand": ban.key_expand,
    "ledger": ban.ledger,
    "node_id": ban.node_id,
    "node_id_delete": ban.node_id_delete,
    "peers": ban.peers,
    "pending": ban.pending,
    "pending_exists": ban.pending_exists,
    "process": ban.process,
    "representatives": ban.representatives,
    "representatives_online": ban.representatives_online,
    "republish": ban.republish,
    "sign": ban.sign,
    "stats": ban.stats,
    "stats_clear": ban.stats_clear,
    "stop": ban.stop,
    "successors": ban.successors,
    "validate_account_number": ban.validate_account_number,
    "version": ban.version,
    "unchecked": ban.unchecked,
    "unchecked_clear": ban.unchecked_clear,
    "unchecked_get": ban.unchecked_get,
    "unchecked_keys": ban.unchecked_keys,
    "unopened": ban.unopened,
    "uptime": ban.uptime,
    "work_cancel": ban.work_cancel,
    "work_generate": ban.work_generate,
    "work_peer_add": ban.work_peer_add,
    "work_peers": ban.work_peers,
    "work_peers_clear": ban.work_peers_clear,
    "work_validate": ban.work_validate,
    "account_create": ban.account_create,
    "account_list": ban.account_list,
    "account_move": ban.account_move,
    "account_remove": ban.account_remove,
    "account_representative_set": ban.account_representative_set,
    "accounts_create": ban.accounts_create,
    "password_change": ban.password_change,
    "password_enter": ban.password_enter,
    "password_valid": ban.password_valid,
    "receive": ban.receive,
    "receive_minimum": ban.receive_minimum,
    "receive_minimum_set": ban.receive_minimum_set,
    "search_pending": ban.search_pending,
    "search_pending_all": ban.search_pending_all,
    "send": ban.send,
    "wallet_add": ban.wallet_add,
    "wallet_add_watch": ban.wallet_add_watch,
    "wallet_balances": ban.wallet_balances,
    "wallet_change_seed": ban.wallet_change_seed,
    "wallet_contains": ban.wallet_contains,
    "wallet_create": ban.wallet_create,
    "wallet_destroy": ban.wallet_destroy,
    "wallet_export": ban.wallet_export,
    "wallet_frontiers": ban.wallet_frontiers,
    "wallet_history": ban.wallet_history,
    "wallet_info": ban.wallet_info,
    "wallet_ledger": ban.wallet_ledger,
    "wallet_lock": ban.wallet_lock,
    "wallet_locked": ban.wallet_locked,
    "wallet_pending": ban.wallet_pending,
    "wallet_representative": ban.wallet_representative,
    "wallet_representative_set": ban.wallet_representative_set,
    "wallet_republish": ban.wallet_republish,
    "wallet_work_get": ban.wallet_work_get,
    "work_get": ban.work_get,
    "work_set": ban.work_set,
    "ban_from_raw": ban.ban_from_raw,
    "ban_to_raw": ban.ban_to_raw,
    "ban_to_banoshi": ban.ban_to_banoshi,
    "ban_from_banoshi": ban.ban_from_banoshi,
}
