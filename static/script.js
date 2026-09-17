// =========================================
// PYQUIZ - QUIZ NAVIGATION
// =========================================

const questions = document.querySelectorAll(".js-question");

const previousButton = document.getElementById("previousButton");
const nextButton = document.getElementById("nextButton");
const submitButton = document.getElementById("submitButton");

const currentQuestion = document.getElementById("currentQuestion");
const totalQuestions = document.getElementById("totalQuestions");

const progressFill = document.getElementById("progressFill");
const progressPercent = document.getElementById("progressPercent");


// =========================================
// CHECK IF QUIZ PAGE EXISTS
// =========================================

if (questions.length > 0) {

    let currentIndex = 0;

    totalQuestions.textContent = questions.length;


    // =========================================
    // SHOW QUESTION
    // =========================================

   function showQuestion(index) {

    questions.forEach(function (question, i) {

        if (i === index) {

            question.style.display = "block";

            // Restart animation
            question.style.animation = "none";

            void question.offsetWidth;

            question.style.animation =
                "questionFade 0.35s ease";

        } else {

            question.style.display = "none";

        }

    });


    // Update question number

    currentQuestion.textContent = index + 1;


    // Update progress

    const progress =
        ((index + 1) / questions.length) * 100;

    progressFill.style.width = progress + "%";

    progressPercent.textContent =
        Math.round(progress) + "%";


    // Previous button

    if (index === 0) {

        previousButton.style.display = "none";

    } else {

        previousButton.style.display = "block";

    }


    // Next / Submit

    if (index === questions.length - 1) {

        nextButton.style.display = "none";
        submitButton.style.display = "block";

    } else {

        nextButton.style.display = "block";
        submitButton.style.display = "none";

    }

}


    // =========================================
    // NEXT
    // =========================================

    nextButton.addEventListener("click", function () {

        const currentOptions =
            questions[currentIndex].querySelectorAll(
                'input[type="radio"]'
            );

        let selected = false;


        currentOptions.forEach(function (option) {

            if (option.checked) {
                selected = true;
            }

        });


        if (!selected) {

            alert("Please choose an answer first! 🌱");
            return;

        }


        if (currentIndex < questions.length - 1) {

            currentIndex++;

            showQuestion(currentIndex);

        }

    });


    // =========================================
    // PREVIOUS
    // =========================================

    previousButton.addEventListener("click", function () {

        if (currentIndex > 0) {

            currentIndex--;

            showQuestion(currentIndex);

        }

    });


    // =========================================
    // SUBMIT
    // =========================================

    submitButton.addEventListener("click", function (event) {

        const currentOptions =
            questions[currentIndex].querySelectorAll(
                'input[type="radio"]'
            );

        let selected = false;


        currentOptions.forEach(function (option) {

            if (option.checked) {
                selected = true;
            }

        });


        if (!selected) {

            event.preventDefault();

            alert("Please choose an answer first! 🌱");

        }

    });


    // =========================================
    // START QUIZ
    // =========================================

    showQuestion(currentIndex);

}