# Document Verification Blockchain

A blockchain-based document verification system that allows users to securely store document hashes on a blockchain and verify document authenticity.[1][2][3]

## Features

- **Document Upload & Hashing**: Upload documents and generate SHA-256 hashes for blockchain storage[1]
- **Blockchain Storage**: Store document hashes in an immutable blockchain with timestamp verification[4][1]
- **Document Verification**: Upload documents to verify their existence and authenticity in the blockchain[1]
- **Real-time Blockchain View**: View the complete blockchain with all stored document hashes[4][1]
- **Web Interface**: User-friendly web interface for all operations[2][5]

## Technologies Used

- **Backend**: Flask (Python) for server-side operations[1]
- **Frontend**: HTML, CSS, JavaScript for the user interface[3][5][2]
- **Blockchain**: Custom blockchain implementation with SHA-256 hashing[1]
- **Storage**: JSON file-based blockchain persistence[4]

## Installation

### Prerequisites
- Python 3.x
- Flask

### Setup
1. Clone the repository:
```bash
git clone <your-repository-url>
cd <your-repository-name>
```

2. Install required dependencies:
```bash
pip install flask
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to `http://localhost:5000`

## Usage

### Adding Documents
1. Select "Add Document to Blockchain" section
2. Choose a file to upload
3. Click "Add Document" - the system will generate a SHA-256 hash and add it to the blockchain[1]

### Verifying Documents  
1. Select "Verify Document" section
2. Upload the document you want to verify
3. Click "Verify Document" - the system will check if the document hash exists in the blockchain[1]

### Viewing Blockchain
The bottom section displays the current blockchain state with all stored document hashes, timestamps, and block information[4][1]

## File Structure

```
├── app.py              # Main Flask application with blockchain logic
├── index.html          # Web interface template  
├── style.css           # Styling for the web interface
├── script.js           # Frontend JavaScript functionality
├── blockchain.json     # Blockchain data storage
└── documents/          # Folder for uploaded documents (created automatically)
```

## How It Works

1. **Document Hashing**: When a document is uploaded, the system generates a SHA-256 hash of its content[1]
2. **Blockchain Addition**: The hash is added as a new block in the blockchain with timestamp and previous block hash[1]
3. **Persistence**: The blockchain is saved to `blockchain.json` for permanent storage[4]
4. **Verification**: Document verification compares the uploaded file's hash against stored blockchain hashes[1]

## API Endpoints

- `GET /` - Main web interface[1]
- `POST /add_document` - Add document hash to blockchain[1]
- `POST /verify_document` - Verify document authenticity[1]
- `GET /get_blockchain` - Retrieve complete blockchain data[1]

## Security Features

- **Immutable Storage**: Once added, document hashes cannot be modified[1]
- **Hash Verification**: Uses SHA-256 cryptographic hashing for document integrity[1]
- **Blockchain Integrity**: Each block contains the previous block's hash, ensuring chain integrity[4][1]
- **Duplicate Prevention**: System prevents adding duplicate documents to the blockchain[1]

## License

This project is open source and available under the [MIT License].
