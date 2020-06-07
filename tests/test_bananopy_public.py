from tests.constants import (
    ADDRESS,
    BLOCK_HASH,
    BURN_ADDRESS,
    PRIVATE_KEY,
    PUB_KEY,
)

import bananopy.banano as ban
from bananopy.utils import unfold_keys
from bananopy import __version__


def test_version():
    assert __version__ == "0.1.0"


def test_account_balance(account=ADDRESS):
    expected = {
        "balance": "6900000000000000000000000000000",
        "pending": "114811000000000000000000000000000",
    }
    response = ban.account_balance(account)
    assert expected == response


def test_account_block_count(account=ADDRESS):
    expected = {
        "block_count": "1",
    }
    response = ban.account_block_count(account)
    assert expected == response


def test_account_get(account=ADDRESS, pub_key=PUB_KEY):
    expected = {
        "account": account,
    }
    response = ban.account_get(pub_key)
    assert expected == response


def test_account_history(account=ADDRESS):
    expected = {
        "account": "ban_19benis4t3ex3orc7acp76jqghi4gk8potks33sie1k48e4w5cfbggeexkyq",
        "history": [
            {
                "type": "receive",
                "account": (
                    "ban_3uicdzy8ckcqsi5efyoy16u4y5dqkimawbzuwzj5jnxpjxmxjn9q8yyykkxc"
                ),
                "amount": "6900000000000000000000000000000",
                "local_timestamp": "1590691741",
                "height": "1",
                "hash": (
                    "9F97F18B2BE5764C85644231E1AF42FF2317FE58C8432FA160BD8396AF2AD9CD"
                ),
            }
        ],
    }
    response = ban.account_history(account, count=1)
    assert expected == response


def test_account_info(account=ADDRESS):
    expected = {
        "frontier": "9F97F18B2BE5764C85644231E1AF42FF2317FE58C8432FA160BD8396AF2AD9CD",
        "open_block": "9F97F18B2BE5764C85644231E1AF42FF2317FE58C8432FA160BD8396AF2AD9CD",
        "representative_block": (
            "9F97F18B2BE5764C85644231E1AF42FF2317FE58C8432FA160BD8396AF2AD9CD"
        ),
        "balance": "6900000000000000000000000000000",
        "modified_timestamp": "1590691741",
        "block_count": "1",
        "account_version": "0",
        "confirmation_height": "1",
    }

    response = ban.account_info(account)
    assert expected == response


# TODO:
def test_account_info_representative(account=ADDRESS):
    expected = {
        "frontier": "9F97F18B2BE5764C85644231E1AF42FF2317FE58C8432FA160BD8396AF2AD9CD",
        "open_block": "9F97F18B2BE5764C85644231E1AF42FF2317FE58C8432FA160BD8396AF2AD9CD",
        "representative_block": (
            "9F97F18B2BE5764C85644231E1AF42FF2317FE58C8432FA160BD8396AF2AD9CD"
        ),
        "balance": "6900000000000000000000000000000",
        "modified_timestamp": "1590691741",
        "block_count": "1",
        "account_version": "0",
        "confirmation_height": "1",
        "representative": (
            "ban_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94xr"
        ),
        "weight": "0",
        "pending": "114811000000000000000000000000000",
    }
    response = ban.account_info(
        account, representative=True, weight=True, pending=True,
    )
    assert expected == response


def test_account_key(account=ADDRESS, pub_key=PUB_KEY):
    expected = {
        "key": PUB_KEY,
    }
    response = ban.account_key(account)
    assert expected == response


def test_account_representative(account=ADDRESS):
    expected = {
        "representative": (
            "ban_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94xr"
        )
    }
    response = ban.account_representative(account)
    assert expected == response


def test_account_weight(account=ADDRESS):
    expected = {"weight": "0"}
    response = ban.account_weight(account)
    assert expected == response


def test_accounts_balances(accounts=[ADDRESS, BURN_ADDRESS]):
    expected = {
        "balances": {
            "ban_19benis4t3ex3orc7acp76jqghi4gk8potks33sie1k48e4w5cfbggeexkyq": {
                "balance": "6900000000000000000000000000000",
                "pending": "114811000000000000000000000000000",
            },
            "ban_1burnbabyburndiscoinferno111111111111111111111111111aj49sw3w": {
                "balance": "0",
                "pending": "50432040866727713701998759104055400892",
            },
        }
    }
    response = ban.accounts_balances(accounts)
    assert expected == response


def test_account_frontiers(accounts=[ADDRESS]):
    expected = {
        "frontiers": {
            "ban_19benis4t3ex3orc7acp76jqghi4gk8potks33sie1k48e4w5cfbggeexkyq": (
                "9F97F18B2BE5764C85644231E1AF42FF2317FE58C8432FA160BD8396AF2AD9CD"
            )
        }
    }
    response = ban.accounts_frontiers(accounts)
    assert expected == response


def test_accounts_pending(accounts=[ADDRESS]):
    expected = {
        "blocks": {
            "ban_19benis4t3ex3orc7acp76jqghi4gk8potks33sie1k48e4w5cfbggeexkyq": [
                "5E5C7C3792A436925C45989323BB2680D619DD305780CB6255ECFA282B810AD4",
                "73F79E4ABC5DD1F5631BF5DF896AA4B78C119EA54D0E677F49DE18894A43737C",
                "8B999BA7EDB2B6C06EBE65423C778C803B8168F3D89B049703C6D96A444F8994",
                "A73075C4054DA96D96D3E3B776B029D65ECC337832C1E9C2FD0791751FC20D6D",
                "F975D8D223A453051885A59DFDDA5025DE003C02AA666F97717EF781D3144868",
            ]
        }
    }
    response = ban.accounts_pending(accounts)
    assert expected == response


def test_active_difficulty():
    # TODO:
    # test that all keys are returned cause exact values are unknown
    expected = ["network_minimum", "network_current", "multiplier"]
    response = ban.active_difficulty()
    assert all((key in expected) for key in response.keys())


def test_available_supply():
    expected = {"available": "340280730846938463463374589668199818054"}
    response = ban.available_supply()
    assert expected == response


def test_block_account(block_hash=BLOCK_HASH):
    expected = {"account": ADDRESS}
    response = ban.block_account(block_hash)
    assert expected == response


def test_block_confirm(block_hash=BLOCK_HASH):
    expected = {"started": "1"}
    response = ban.block_confirm(block_hash)
    assert expected == response


def test_block_count():
    # TODO:
    # test that all keys are returned cause exact values are unknown
    expected = ["count", "unchecked", "cemented"]
    response = ban.block_count()
    assert all((key in expected) for key in response.keys())


def test_block_count_type():
    # TODO:
    # test that all keys are returned cause exact values are unknown
    expected = ["send", "receive", "open", "change", "state_v0", "state_v1", "state"]
    response = ban.block_count_type()
    assert all((key in expected) for key in response.keys())


def test_block_hash():
    # TODO:
    # response = ban.block_hash(
    # block_type,
    # account,previous,
    # representative,
    # balance,
    # link,
    # link_as_account,
    # signature,
    # work,
    # )
    pass


def test_block_info(block_hash=BLOCK_HASH):
    expected = {
        "block_account": (
            "ban_19benis4t3ex3orc7acp76jqghi4gk8potks33sie1k48e4w5cfbggeexkyq"
        ),
        "amount": "6900000000000000000000000000000",
        "balance": "6900000000000000000000000000000",
        "height": "1",
        "local_timestamp": "1590691741",
        "confirmed": "true",
        "contents": {
            "type": "state",
            "account": (
                "ban_19benis4t3ex3orc7acp76jqghi4gk8potks33sie1k48e4w5cfbggeexkyq"
            ),
            "previous": (
                "0000000000000000000000000000000000000000000000000000000000000000"
            ),
            "representative": (
                "ban_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94xr"
            ),
            "balance": ("6900000000000000000000000000000"),
            "link": "BE9212348E60305F447EF05C70E0CE3B25085CF70C527D5D4BA96C9C549D9962",
            "link_as_account": (
                "ban_3hnk4atawr3idx49xw4wg5iewgs733ghg54khognqcdemjcbu8d48i9w66d3"
            ),
            "signature": (
                "83F3BAF9993E9A8944D4052D3E99992918D43D74BF964BA13716E603D9C7B4EA"
                "C1CD3741F232E9B8D96C9858003C3D08C453A779171A607EC4B01143655D3800"
            ),
            "work": "eb1508d683a4915f",
        },
        "subtype": "receive",
    }
    response = ban.block_info(block_hash, json_block=True)
    assert response == expected


def test_blocks(hashes=[BLOCK_HASH]):
    expected = {
        "blocks": {
            "9F97F18B2BE5764C85644231E1AF42FF2317FE58C8432FA160BD8396AF2AD9CD": {
                "type": "state",
                "account": (
                    "ban_19benis4t3ex3orc7acp76jqghi4gk8potks33sie1k48e4w5cfbggeexkyq"
                ),
                "previous": (
                    "0000000000000000000000000000000000000000000000000000000000000000"
                ),
                "representative": (
                    "ban_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94xr"
                ),
                "balance": "6900000000000000000000000000000",
                "link": (
                    "BE9212348E60305F447EF05C70E0CE3B25085CF70C527D5D4BA96C9C549D9962"
                ),
                "link_as_account": (
                    "ban_3hnk4atawr3idx49xw4wg5iewgs733ghg54khognqcdemjcbu8d48i9w66d3"
                ),
                "signature": (
                    "83F3BAF9993E9A8944D4052D3E99992918D43D74BF964BA13716E603D9C7B4EA"
                    "C1CD3741F232E9B8D96C9858003C3D08C453A779171A607EC4B01143655D3800"
                ),
                "work": "eb1508d683a4915f",
            }
        }
    }
    response = ban.blocks(hashes, json_block=True)
    assert response == expected


def test_blocks_info(hashes=[BLOCK_HASH]):
    expected = {
        "blocks": {
            "9F97F18B2BE5764C85644231E1AF42FF2317FE58C8432FA160BD8396AF2AD9CD": {
                "block_account": "ban_19benis4t3ex3orc7acp76jqghi4gk8potks33sie1k48e4w5cfbggeexkyq",
                "amount": "6900000000000000000000000000000",
                "balance": "6900000000000000000000000000000",
                "height": "1",
                "local_timestamp": "1590691741",
                "confirmed": "true",
                "contents": {
                    "type": "state",
                    "account": "ban_19benis4t3ex3orc7acp76jqghi4gk8potks33sie1k48e4w5cfbggeexkyq",
                    "previous": "0000000000000000000000000000000000000000000000000000000000000000",
                    "representative": "ban_1bananobh5rat99qfgt1ptpieie5swmoth87thi74qgbfrij7dcgjiij94xr",
                    "balance": "6900000000000000000000000000000",
                    "link": "BE9212348E60305F447EF05C70E0CE3B25085CF70C527D5D4BA96C9C549D9962",
                    "link_as_account": "ban_3hnk4atawr3idx49xw4wg5iewgs733ghg54khognqcdemjcbu8d48i9w66d3",
                    "signature": "83F3BAF9993E9A8944D4052D3E99992918D43D74BF964BA13716E603D9C7B4EAC1CD3741F232E9B8D96C9858003C3D08C453A779171A607EC4B01143655D3800",
                    "work": "eb1508d683a4915f",
                },
                "subtype": "receive",
            }
        }
    }
    response = ban.blocks_info(hashes, json_block=True)
    assert response == expected


def test_bootstrap_lazy(block_hash=BLOCK_HASH):
    expected = {
        "success": "",
    }
    response = ban.bootstrap_lazy(block_hash)
    assert response == expected


def test_bootstrap_status():
    # TODO:
    # test that all keys are returned cause exact values are unknown
    expected = [
        "clients",
        "pulls",
        "pulling",
        "connections",
        "idle",
        "target_connections",
        "total_blocks",
        "runs_count",
        "requeued_pulls",
        "frontiers_received",
        "frontiers_confirmed",
        "mode",
        "lazy_blocks",
        "lazy_state_backlog",
        "lazy_balances",
        "lazy_destinations",
        "lazy_undefined_links",
        "lazy_pulls",
        "lazy_keys",
        "lazy_key_1",
        "duration",
    ]
    response = ban.bootstrap_status()
    assert all((key in expected) for key in unfold_keys(response))


def test_chain(block_hash=BLOCK_HASH):
    expected = {
        "blocks": ["9F97F18B2BE5764C85644231E1AF42FF2317FE58C8432FA160BD8396AF2AD9CD"]
    }
    response = ban.chain(block_hash)
    assert response == expected


def test_confirmation_active():
    # TODO:
    # test that all keys are returned cause exact values are unknown
    expected = ["confirmations", "unconfirmed", "confirmed"]
    response = ban.confirmation_active()
    assert all((key in expected) for key in response.keys())


def test_confirmation_history(block_hash=BLOCK_HASH):
    # TODO:
    expected = [
        "average",
        "blocks",
        "confirmation_stats",
        "confirmations",
        "count",
        "duration",
        "hash",
        "request_count",
        "tally",
        "time",
        "voters",
    ]
    response = ban.confirmation_history()
    assert all((key in expected) for key in unfold_keys(response))


def test_confirmation_info(block_hash=BLOCK_HASH):
    # TODO:
    expected = {"error": "Active confirmation not found"}
    response = ban.confirmation_info(block_hash, representatives=True)
    assert all((key in expected) for key in unfold_keys(response))


def test_confirmation_quorum():
    # TODO:
    expected = [
        "quorum_delta",
        "online_weight_quorum_percent",
        "online_weight_minimum",
        "online_stake_total",
        "peers_stake_total",
        "peers_stake_required",
    ]
    response = ban.confirmation_quorum()
    assert all((key in expected) for key in response.keys())


def test_delegators(account=ADDRESS):
    expected = {"delegators": ""}
    response = ban.delegators(account)
    assert response == expected


def test_delegators_count(account=ADDRESS):
    expected = {"count": "0"}
    response = ban.delegators_count(account)
    assert response == expected


def test_deteministic_key():
    params = {
        "seed": "0000000000000000000000000000000000000000000000000000000000000000",
        "index": "0",
    }
    expected = {
        "private": "9F0E444C69F77A49BD0BE89DB92C38FE713E0963165CCA12FAF5712D7657120F",
        "public": "C008B814A7D269A1FA3C6528B19201A24D797912DB9996FF02A1FF356E45552B",
        "account": "ban_3i1aq1cchnmbn9x5rsbap8b15akfh7wj7pwskuzi7ahz8oq6cobd99d4r3b7",
    }
    response = ban.deteministic_key(**params)
    assert response == expected


def test_frontier_count():
    # TODO:
    expected = ["count"]
    response = ban.frontier_count()
    assert (
        all((key in expected) for key in response.keys()) and int(response["count"]) > 0
    )


def test_frontiers(account=ADDRESS):
    expected = {
        "frontiers": {
            "ban_19benis4t3ex3orc7acp76jqghi4gk8potks33sie1k48e4w5cfbggeexkyq": (
                "9F97F18B2BE5764C85644231E1AF42FF2317FE58C8432FA160BD8396AF2AD9CD"
            )
        }
    }
    response = ban.frontiers(account, count=1)
    assert response == expected


def test_key_create():
    # TODO:
    expected = ["private", "public", "account"]
    response = ban.key_create()
    assert all((key in expected) for key in response.keys())


def test_key_expand(private_key=PRIVATE_KEY):
    expected = {
        "private": "9F97F18B2BE5764C85644231E1AF42FF2317FE58C8432FA160BD8396AF2AD9CD",
        "public": "657A078D611D7DC2A159BFBC3B457782D7379910DA050E92CFDA4B9C906BEF8E",
        "account": "ban_1sdt1y8p49dxrciomhxw9f4qh1pq8yej3pi73tbezpkdmka8quwgke9m9719",
    }
    response = ban.key_expand(private_key)
    assert response == expected


def test_peers():
    # TODO:
    expected = ["peers"]
    response = ban.peers()
    assert all((key in expected) for key in response.keys())


def test_pending(account=ADDRESS):
    expected = {
        "blocks": ["5E5C7C3792A436925C45989323BB2680D619DD305780CB6255ECFA282B810AD4"]
    }
    response = ban.pending(account, count=1)
    assert response == expected


def test_pending_exists(block_hash=BLOCK_HASH):
    expected = {"exists": "0"}
    response = ban.pending_exists(block_hash)
    assert response == expected


def test_process():
    # TODO:
    pass


def test_representatives():
    # TODO:
    expected = ["representatives"]
    response = ban.representatives()
    assert all((key in expected) for key in response.keys())


def test_representatives_online():
    # TODO:
    expected = ["representatives"]
    response = ban.representatives_online()
    assert all((key in expected) for key in response.keys())


def test_republish(block_hash=BLOCK_HASH):
    # TODO:
    # expected = {}
    # response = ban.republish(block_hash)
    # assert response == expected
    pass


def test_sign_key():
    # TODO:
    # expect = {}
    # response = ban.sign_key()
    # assert response == expected
    pass


# def test_sign_wallet():
#     # TODO:
#     # expect = {}
#     # response = ban.sign_wallet()
#     # assert response == expected
#     pass


def test_stats():
    # TODO:
    expected = [
        "counters",
        "created",
        "type",
        "entries",
        "time",
        "type",
        "detail",
        "dir",
        "value",
        "stat_duration_seconds",
    ]
    response = ban.stats("counters")
    assert all((key in expected) for key in unfold_keys(response))


def test_stats_clear():
    expected = {"success": ""}
    response = ban.stats_clear()
    assert response == expected


def test_successors(block_hash=BLOCK_HASH):
    expected = {
        "blocks": ["9F97F18B2BE5764C85644231E1AF42FF2317FE58C8432FA160BD8396AF2AD9CD"]
    }
    response = ban.successors(block_hash, count=1)
    assert response == expected


def test_validate_account_number(account=ADDRESS):
    expected = {"valid": "1"}
    response = ban.validate_account_number(account)
    assert response == expected


def test_node_version():
    expected = {
        "rpc_version": "1",
        "store_version": "15",
        "protocol_version": "17",
        "node_vendor": "BANANO V20.0",
        "network": "live",
        "network_identifier": (
            "F61A79F286ABC5CC01D3D09686F0567812B889A5C63ADE0E82DD30F3B2D96463"
        ),
        "build_info": '882e9eb "GNU C++ version " "5.4.0 20160609" "BOOST 107000" BUILT "May 26 2020"',
    }
    response = ban.version()
    assert response == expected


def test_unchecked():
    expected = {"blocks": ""}
    response = ban.unchecked()
    assert response == expected


def test_unchecked_get(block_hash=BLOCK_HASH):
    expected = {"error": "Block not found"}
    response = ban.unchecked_get(block_hash)
    assert response == expected


def test_unchecked_keys(private_key=PRIVATE_KEY):
    expected = {"unchecked": ""}
    response = ban.unchecked_keys(private_key)
    assert response == expected


def test_uptime():
    response = ban.uptime()
    assert int(response["seconds"]) > 0


def test_work_validate():
    # TODO:
    pass
