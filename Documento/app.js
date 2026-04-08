document.addEventListener("DOMContentLoaded", () => {

    const API_URL = "http://127.0.0.1:5000/users";

    const container = document.getElementById("users-container");
    const statusDiv = document.getElementById("status");
    const searchInput = document.getElementById("search");

    let users = [];

    // -----------------------
    // Obtener usuarios
    // -----------------------
    async function fetchUsers() {
        try {
            statusDiv.innerHTML = "<p class='loading'>Cargando...</p>";

            const response = await fetch(API_URL);

            if (!response.ok) {
                throw new Error("Error al obtener usuarios");
            }

            users = await response.json();

            console.log("Usuarios cargados:", users);

            statusDiv.innerHTML = "";
            renderUsers(users);

        } catch (error) {
            statusDiv.innerHTML = `<p class='error'>${error.message}</p>`;
        }
    }

    // -----------------------
    // Renderizar usuarios
    // -----------------------
    function renderUsers(data) {
        container.innerHTML = "";

        if (data.length === 0) {
            container.innerHTML = "<p>No hay coincidencias</p>";
            return;
        }

        data.forEach(user => {
            const card = document.createElement("div");
            card.className = "card";

            card.innerHTML = `
                <h3>${user.name}</h3>
                <p>${user.email}</p>
            `;

            container.appendChild(card);
        });
    }

    // -----------------------
    // Filtro por nombre
    // -----------------------
    searchInput.addEventListener("input", (e) => {
        const value = e.target.value.toLowerCase().trim();

        const filtered = users.filter(user =>
            user.name.toLowerCase().includes(value)
        );

        console.log("Filtro:", value, filtered);

        renderUsers(filtered);
    });

    // -----------------------
    // Inicializar
    // -----------------------
    fetchUsers();
});