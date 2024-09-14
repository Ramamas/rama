document.addEventListener("DOMContentLoaded", () => {
    const choices = document.querySelectorAll(".choice");
    const userChoiceDisplay = document.getElementById("user-choice");
    const computerChoiceDisplay = document.getElementById("computer-choice");
    const messageDisplay = document.getElementById("message");

    const choicesArray = ["rock", "paper", "scissors"];

    choices.forEach(choice => {
        choice.addEventListener("click", () => {
            const userChoice = choice.id;
            const computerChoice = getComputerChoice();
            const result = getResult(userChoice, computerChoice);

            userChoiceDisplay.textContent = capitalize(userChoice);
            computerChoiceDisplay.textContent = capitalize(computerChoice);
            messageDisplay.textContent = result;
        });
    });

    function getComputerChoice() {
        const randomIndex = Math.floor(Math.random() * 3);
        return choicesArray[randomIndex];
    }

    function getResult(userChoice, computerChoice) {
        if (userChoice === computerChoice) {
            return "YOU TIED!";
        } else if (
            (userChoice === "rock" && computerChoice === "scissors") ||
            (userChoice === "scissors" && computerChoice === "paper") ||
            (userChoice === "paper" && computerChoice === "rock")
        ) {
            return "YOU WIN!";
        } else {
            return "YOU LOST!";
        }
    }

    function capitalize(str) {
        return str.charAt(0).toUpperCase() + str.slice(1);
    }
});
