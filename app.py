import hashlib
import datetime
import json
import os
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)
UPLOAD_FOLDER = "documents"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ---------------- Block & Blockchain ----------------
class Block:
    def __init__(self, index, timestamp, doc_hash, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.doc_hash = doc_hash
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.doc_hash}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self, filename="blockchain.json"):
        self.filename = filename
        if os.path.exists(self.filename):
            self.load_chain()
        else:
            self.chain = [self.create_genesis_block()]
            self.save_chain()

    def create_genesis_block(self):
        return Block(0, str(datetime.datetime.now()), "Genesis Block", "0")

    def add_block(self, doc_hash):
        last_block = self.chain[-1]
        new_block = Block(len(self.chain), str(datetime.datetime.now()), doc_hash, last_block.hash)
        self.chain.append(new_block)
        self.save_chain()

    def find_block(self, doc_hash):
        for block in self.chain[1:]:  # skip genesis block
            if block.doc_hash == doc_hash:
                return block
        return None

    def save_chain(self):
        chain_data = []
        for block in self.chain:
            chain_data.append({
                "index": block.index,
                "timestamp": block.timestamp,
                "doc_hash": block.doc_hash,
                "previous_hash": block.previous_hash,
                "hash": block.hash
            })
        with open(self.filename, "w") as f:
            json.dump(chain_data, f, indent=4)

    def load_chain(self):
        with open(self.filename, "r") as f:
            chain_data = json.load(f)
            self.chain = []
            for data in chain_data:
                block = Block(data["index"], data["timestamp"], data["doc_hash"], data["previous_hash"])
                block.hash = data["hash"]
                self.chain.append(block)

# Initialize blockchain
blockchain = Blockchain()

# ---------------- Flask Routes ----------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_document", methods=["POST"])
def add_document():
    if "document" in request.files:
        file = request.files["document"]
        if file.filename != "":
            file_bytes = file.read()
            doc_hash = hashlib.sha256(file_bytes).hexdigest()
            if blockchain.find_block(doc_hash):
                return jsonify({"status":"error","message":"Document already exists in blockchain."})
            blockchain.add_block(doc_hash)
            # Save file (optional)
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            with open(file_path, "wb") as f:
                f.write(file_bytes)
            return jsonify({"status":"success","message":f"Document added! Hash: {doc_hash}"})
    return jsonify({"status":"error","message":"No document uploaded."})

@app.route("/verify_document", methods=["POST"])
def verify_document():
    if "verify" in request.files:
        file = request.files["verify"]
        if file.filename != "":
            file_bytes = file.read()
            doc_hash = hashlib.sha256(file_bytes).hexdigest()
            block = blockchain.find_block(doc_hash)
            if block:
                return jsonify({
                    "status":"success",
                    "message":f"Document verified! Block index: {block.index}, Timestamp: {block.timestamp}"
                })
            else:
                return jsonify({"status":"error","message":"Document not found in blockchain."})
    return jsonify({"status":"error","message":"No document uploaded."})

@app.route("/get_blockchain", methods=["GET"])
def get_blockchain():
    chain_data = []
    for block in blockchain.chain[1:]:  # skip genesis
        chain_data.append({
            "index": block.index,
            "hash": block.hash,
            "previous_hash": block.previous_hash,
            "timestamp": block.timestamp
        })
    return jsonify(chain_data)

if __name__ == "__main__":
    app.run(debug=True)
