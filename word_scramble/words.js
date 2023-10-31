const words = ["apple", "banana", "cherry", "grape", "orange", "antartica", "astronaut", "season", "earth", "jupiter"]
let currentWord = "";

function scrambleWord(word) {
    const array = word.split("");
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array.join("");
}

function getRandomWord() {
    return words[Math.floor(Math.random() * words.length)];
}

function newGame() {
    currentWord = getRandomWord();
    const scrambled = scrambleWord(currentWord);
    document.getElementById("scrambled-word").textContent = scrambled;
    document.getElementById("message").textContent = "";
    document.getElementById("guess").value = "";
}

document.getElementById("check-button").addEventListener("click", function() {
    const guess = document.getElementById("guess").value.toLowerCase();
    if (guess === currentWord) {
        document.getElementById("message").textContent = "Correct! You have unscrambled the word.";
        newGame();
    } else {
        document.getElementById("message").textContent = "Try again.";
    }
});

newGame();