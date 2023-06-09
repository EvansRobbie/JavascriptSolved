// console.log('Helloo')

// Given an array of objects, each object representing a person with a name and age property, write a function that returns a new array containing the names of all people who are 18 years old or older.
// const people = [
// { name: 'Alice', age: 17 },
// { name: 'Eunice', age: 22 },
// { name: 'Charlie', age: 14 },
// { name: 'Max', age: 19 },
// ];
// I'll use the .filter and .map method to solve it

const Adult = (people) =>{
    return people.filter(person => person.age >= 18).map(person => person.name)
}
// .filter() - used to create an array with all elements that satisfy a given condition
// . map() method is used to extract the names of these people into a new array.
const people = [
{ name: 'Alice', age: 17 },
{ name: 'Eunice', age: 22 },
{ name: 'Charlie', age: 14 },
{ name: 'Max', age: 19 },
];

const nameOfAdults = Adult(people)
console.log(nameOfAdults) //[ 'Eunice', 'Max' ]