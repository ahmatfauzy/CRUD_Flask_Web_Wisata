const tombol = document.getElementById("hamburger-menu");
const menu = document.querySelector(".menu");

tombol.addEventListener("click", () => {
  menu.classList.toggle("aktif");
});

document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("#pesan form");

  form.addEventListener("submit", (event) => {
    event.preventDefault();

    const name = document.querySelector("#name").value;
    const orderType = document.querySelector("#order-type").value;

    alert(`Hi ${name}, pesanan Anda (${orderType}) sedang diproses.`);
  });
});
