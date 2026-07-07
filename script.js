async function loadStaff(){

    const response = await fetch("/staff.json");

    const users = await response.json();

    const box = document.getElementById("staff");

    box.innerHTML = "";

    users.forEach(user => {

        box.innerHTML += `
        <div class="member">

            <img src="${user.avatar}">

            <a href="${user.profile}" target="_blank">
                ${user.name}
            </a>

        </div>
        `;

    });

    document.getElementById("status").innerHTML =
    "Aktywna ekipa: " + users.length + " osób";

}

loadStaff();