class Question {
    constructor(text, options, correctAnswer){
        this.text = text,
        this.options = options,
        this.correctAnswer = correctAnswer
    }
    checkAnswer(usersAnswer){
        return usersAnswer === this.correctAnswer   
    }
}

class Quiz {
    constructor(){
        this.questions = [],
        this.currentQuestionIndex = 0,
        this.score = 0
    }
    addQuestion(question){
        this.questions.push(question)
    }
    nextQuestion(){
        this.currentQuestionIndex++
    }
    submitAnswer(usersAnswer){
        const currentQuestion = this.questions[this.currentQuestionIndex]
        if (currentQuestion.checkAnswer(usersAnswer)){
            this.score++
        }
        this.nextQuestion()
    }
}

const quiz = new Quiz()
// create Question
const question1 = new Question(
    "What is the capital of France?",
    ["Paris", "London", "Berlin", "Rome"],
    "Paris"
  );
  
  const question2 = new Question(
    "Which planet is known as the Red Planet?",
    ["Mars", "Venus", "Jupiter", "Saturn"],
    "Mars"
  );

//   Add questions to quiz

quiz.addQuestion(question1)
quiz.addQuestion(question2)

// simulate user answering questions

quiz.submitAnswer('Paris') // correct ansswer
quiz.submitAnswer('Venus') // incorrect answer

// score

console.log('Score:', quiz.score) // total score