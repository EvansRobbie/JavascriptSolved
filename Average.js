// Given an array of objects, where each object represents a student with a name and an array of scores, write a function that returns a new array containing the names of all students whose average score is greater than or equal to 85.
const students = [
{ name: 'John', scores: [90, 80, 85] },
{ name: 'Jane', scores: [95, 92, 88] },
{ name: 'Jim', scores: [70, 80, 75] },
{ name: 'Jill', scores: [85, 90, 84] },
];

const getAverageScores = (students) =>{
    const result = []
    // We use for.. of to iterate over each object in the array
    for(const student of students){
        // usethe ,reduce() method to calculate the total scores of each student -
        //and then divide by the lengthof the student scores to get the average score
        const averageScore = student.scores.reduce((total, score) => total + score, 0)/ student.scores.length
        // is the average score greatet than or equal to 85 we push the name of the student to the array
        if (averageScore >= 85){
            result.push(student.name)
        }
    }

    return result
}

const studentWithHighSchool = getAverageScores(students)

console.log(studentWithHighSchool) //[ 'John', 'Jane', 'Jill' ]