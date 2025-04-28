document.getElementById("store-btn").addEventListener("click", async () => {
    const service = document.getElementById("store-service").value;
    const username = document.getElementById("store-username").value;
    const password = document.getElementById("store-password").value;

    const response = await fetch("/store", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ service, username, password }),
    });

    const data = await response.json();
    alert(data.message || "Error storing password");
});

document.getElementById("retrieve-btn").addEventListener("click", async () => {
    const service = document.getElementById("retrieve-service").value;

    const response = await fetch("/retrieve", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ service }),
    });

    const data = await response.json();
    if (data.error) {
        alert(data.error);
    } else {
        document.getElementById("result").innerHTML = `
            Username: ${data.username}<br>
            Password: ${data.password}
        `;
    }
});
