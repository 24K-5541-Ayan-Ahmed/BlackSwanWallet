"""BlackSwan | Ayan Ahmed | 24K-5541. See THIRD_PARTY_NOTICES.md."""
from flask import Flask, render_template, request
from Blockchain.client.sendBlackSwan import SendBlackSwan
from Blockchain.Backend.core.Tx import Tx

app = Flask(__name__)

from flask import jsonify
from Blockchain.Backend.util.util import decode_base58


@app.route("/api/balance/<address>")
def account_balance(address):
    try:
        address_hash = decode_base58(address)
    except (ValueError, OverflowError):
        return jsonify(error="Invalid account address."), 400

    utxos = globals().get("UTXOS")

    if utxos is None:
        return jsonify(error="Start the blockchain first."), 503

    total = 0

    for transaction in utxos.values():
        for output in transaction.tx_outs:
            if output.script_pubkey.cmds[2] == address_hash:
                total += output.amount

    return jsonify(balance=f"{total / 100_000_000:.2f}")

@app.route("/", methods=["GET", "POST"])
def wallet():
    message = ""
    if request.method == "POST":
        FromAddress = request.form.get("fromAddress")
        ToAddress = request.form.get("toAddress")
        Amount = request.form.get("Amount", type=int)
        sendCoin = SendBlackSwan(FromAddress, ToAddress, Amount, UTXOS)
        TxObj = sendCoin.prepareTransaction()

        scriptPubKey = sendCoin.scriptPubKey(FromAddress)
        verified = True

        if not TxObj:
            message = "Invalid Transaction"

        if isinstance(TxObj, Tx):
            for index, tx in enumerate(TxObj.tx_ins):
                if not TxObj.verify_input(index, scriptPubKey):
                    verified = False

            if verified:
                MEMPOOL[TxObj.TxId] = TxObj
                message = "Transaction added in memory Pool"

    return render_template("wallet.html", message=message)


def main(utxos, MemPool):
    global UTXOS
    global MEMPOOL
    UTXOS = utxos
    MEMPOOL = MemPool
    app.run(host="127.0.0.1", port=5900, debug=False, use_reloader=False)
