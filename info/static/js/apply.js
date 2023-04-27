function showOverlay(overlay) {
    if (!overlay.classList.contains('visible')) {
        overlay.classList.add('visible');
    }
}

function hideOverlay(overlay) {
    if (overlay.classList.contains('visible')) {
        overlay.classList.remove('visible');
    }
}

function addCloseTrigger(overlay) {
    overlay.querySelector(".title button").onclick = function() {
        hideOverlay(overlay);
    }
}

let form = document.getElementById("apply-form");
/*let fields = document.querySelectorAll("#apply-form .field");*/
let sendedOverlay = document.getElementById("sended-overlay");
let clearOverlay = document.getElementById("clear-overlay");

addCloseTrigger(sendedOverlay);
addCloseTrigger(clearOverlay);

form.addEventListener("submit", event => {
    if (form.reportValidity()) {
        showOverlay(sendedOverlay)
    }

    event.preventDefault();
    //return false;
});

document.getElementById('clear').addEventListener("click", event => {
    showOverlay(clearOverlay);
});

clearOverlay.querySelector(".answer-no").addEventListener("click", event => {
    hideOverlay(clearOverlay);
});

clearOverlay.querySelector(".answer-yes").addEventListener("click", event => {
    hideOverlay(clearOverlay);
    form.reset();
});