const emailInput = document.querySelector("#e-mail");
const usernameInput = document.querySelector("#username");
const eyeIcons = document.querySelectorAll(".eye");


const hideInputIcon = (input) => {
    input.addEventListener("focus", () => {
        input.previousElementSibling.style.display = "none";
    });
}

const showInputIcon = (input) => {
    input.addEventListener("blur", () => {
        input.previousElementSibling.style.display = "block";
    });
}

hideInputIcon(emailInput);
hideInputIcon(usernameInput);

showInputIcon(emailInput);
showInputIcon(usernameInput);

const eyeIconsArr = Array.from(eyeIcons);
for (let i = 0; i < eyeIconsArr.length; i++) {
    const eyeIcon = eyeIcons[i];
    eyeIcon.addEventListener("click", () => {

        if (eyeIcon.previousElementSibling.type === "password") {
            eyeIcon.previousElementSibling.type = "text";
            eyeIcon.previousElementSibling.style.padding = "12px";
            eyeIcon.src = "../images/akar-icons_eye.svg";
            return;
        }
        eyeIcon.previousElementSibling.type = "password";
        eyeIcon.src = "../images/eye-closed.png";
    })
}
