# BlackSwan: A Blockchain Wallet

**Name:** Ayan Ahmed  
**Student ID:** 24K-5541  
**Section:** BSFT-5B  
**Instructor:** Syed Waqar Ali  
**Project Repo:** [BlackSwanWallet](https://github.com/24K-5541-Ayan-Ahmed/BlackSwanWallet)  
**Currency:** BSWAN

## Overview

BlackSwan is a fully functional blockchain wallet built by watching tutorial videos provided. It incorporates all features as shown in the tutorial videos.

## Features

- **Wallet Interface:** Displays account names, public addresses, and a transfer form.
- **Show Balance:** Retrieves and displays an account’s available balance.
- **Copy Address:** Copies the selected account’s public address to the clipboard.
- **Transfer BSWAN:** Allows users to enter a sender address, recipient address, and amount.
- **Transaction Feedback:** Displays messages after a transaction submission.
- **Account Creation:** Generates private keys and corresponding public addresses.
- **Digital Signatures:** Signs transactions and verifies ownership of funds.
- **Automatic Mining:** Mines blocks while the blockchain program is running.
- **Local Storage:** Saves account records and blockchain history in JSON-formatted files.

## Technologies and Tools Used

| Technology / Tool | Purpose |
| --- | --- |
| Python 3.10.11 | Implements blockchain logic, accounts, transactions, and mining. |
| Flask | Serves the wallet interface and handles transfer and balance requests. |
| Jinja2 | Renders HTML templates and displays backend messages. |
| HTML | Structures the account cards, buttons, and transfer form. |
| CSS | Styles the layout, colors, inputs, and buttons. |
| JavaScript | Implements Show Balance and Copy Address interactions. |
| Fetch API | Requests balances without reloading the page. |
| Clipboard API | Copies public addresses to the clipboard. |
| Boxicons | Provides icons for interface buttons. |
| SHA-256 | Supports transaction hashing, block hashing, and proof-of-work. |
| RIPEMD-160 | Helps generate public-address hashes. |
| Elliptic Curve Cryptography - secp256k1 | Supports key generation, transaction signing, and signature verification. |
| PyCryptodome | Provides RIPEMD-160 hashing. |
| Python multiprocessing | Runs mining alongside the wallet server and shares transaction data between processes. |
| JSON-formatted Files | Store account records and mined blocks locally. |
| Visual Studio Code | Used for development and running the project. |
| pip and venv | Manage dependencies and the Python environment. |

## How the Project Works

### 1. Starting the Blockchain

Running `blockchain.py` starts automatic mining and the Flask wallet server. The wallet can be accessed at:

```text
http://127.0.0.1:5900/
```

### 2. Creating Accounts

The account generator creates a private key and derives its corresponding public address.

- The **public address** identifies where funds can be received.
- The **private key** is used to sign transactions and authorize spending.

### 3. Checking Balances

Clicking **Show Balance** sends a request to the Flask balance endpoint. The backend totals the unspent transaction outputs belonging to the selected address and returns the balance in BSWAN.

An unspent transaction output, or **UTXO**, represents funds received by an address that have not yet been spent.

### 4. Copying Addresses

Clicking **Copy Address** uses JavaScript and the Clipboard API to copy the selected public address. This makes it easier to fill the transfer form and reduces typing mistakes.

### 5. Sending Transactions

The user enters:

- Sender address
- Recipient address
- Amount in BSWAN

The backend selects available funds to cover the payment and transaction fee. It creates an output for the recipient and returns any remaining funds to the sender as change.

The transaction is signed using the sender’s private key. After signature verification, it is added to the **memory pool**, where it waits to be mined.

### 6. Mining Blocks

The miner includes pending transactions in a block and calculates their Merkle root. It then searches for a nonce that produces a block-header hash below the mining target.

A mining-reward transaction is also included in the block.

### 7. Updating Records

After mining:

- The block is saved to the local blockchain file.
- Included transactions are removed from the memory pool.
- Spent outputs are removed from the available funds.
- New payment and change outputs become available.

## Running the Project

Use Python 3.10. From the project folder on Windows, run:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m ensurepip --upgrade
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m Blockchain.Backend.core.blockchain
```

Open `http://127.0.0.1:5900/` in a browser.

Keep the terminal running while using the wallet. Press **Ctrl+C** to stop the program.

## Implementation Notes

- One BSWAN equals **100,000,000 base units**.
- The implementation uses a **50 BSWAN block reward** and a **1 BSWAN transaction fee**.
- Mining rewards go to the address configured as `MINER_ADDRESS` in `Blockchain/Backend/core/Tx.py`.
- Creating an account does not automatically make it the mining recipient.
- The balance endpoint reads the running node’s in-memory UTXO data. The original implementation does not rebuild this data from saved blocks after a restart.
- This project is a local educational prototype. Private keys are stored in local account records, and production wallet security is outside its scope.

## Source and Attribution

Adapted from [Blockchain Implementation in Python from Scratch](https://github.com/anni1236012/Blockchain-Implementation-in-Python-from-Scratch).

BlackSwan branding, wallet styling, and the Show Balance and Copy Address interface features were customized for this project. 
