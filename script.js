document.addEventListener("DOMContentLoaded", () => {
    const addForm = document.getElementById("addForm");
    const verifyForm = document.getElementById("verifyForm");
    const messageBox = document.getElementById("message");
    const blockchainTableBody = document.querySelector("#blockchainTable tbody");

    function refreshBlockchainTable() {
        fetch("/get_blockchain")
            .then(response => response.json())
            .then(data => {
                blockchainTableBody.innerHTML = "";
                data.forEach(block => {
                    const row = document.createElement("tr");
                    row.innerHTML = `
                        <td>${block.index}</td>
                        <td>${block.hash}</td>
                        <td>${block.previous_hash}</td>
                        <td>${block.timestamp}</td>
                    `;
                    blockchainTableBody.appendChild(row);
                });
            });
    }

    // Load table on start
    refreshBlockchainTable();

    addForm.addEventListener("submit", (e) => {
        e.preventDefault();
        const formData = new FormData(addForm);
        fetch("/add_document", { method: "POST", body: formData })
            .then(res => res.json())
            .then(data => {
                messageBox.textContent = data.message;
                messageBox.style.color = data.status === "success" ? "green" : "red";
                refreshBlockchainTable();
            });
    });

    verifyForm.addEventListener("submit", (e) => {
        e.preventDefault();
        const formData = new FormData(verifyForm);
        fetch("/verify_document", { method: "POST", body: formData })
            .then(res => res.json())
            .then(data => {
                messageBox.textContent = data.message;
                messageBox.style.color = data.status === "success" ? "green" : "red";
            });
    });
});
