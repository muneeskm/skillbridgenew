console.log("JS LOADED");

const popup = document.getElementById("popup");
const closeBtn = document.getElementById("closePopupBtn");

let currentJobId = null;

document.querySelectorAll(".openPopupBtn").forEach(btn => {
    btn.addEventListener("click", function () {

        currentJobId = this.getAttribute("data-job");

        console.log("Selected Job:", currentJobId);

        popup.style.display = "flex";
    });
});

// ONLINE button (add id="onlineBtn" in HTML)
document.getElementById("onlineBtn").addEventListener("click", function () {
    if (currentJobId) {
        window.location.href = `/payment/${currentJobId}/`;
    }
});

// close popup
closeBtn.addEventListener("click", function () {
    popup.style.display = "none";
});