// Given an object representing a car, with properties for the make, model, year, and a method to display the car's information, write a function that takes the car object and adds a new method to the object called age. The age method should return the current age of the car based on the current year and the car's year property.
const car = {
make: 'Ford',
model: 'Ranger',
year: 2023,
displayInfo: function() {
console.log(`Make: ${this.make}, Model: ${this.model}, Year: ${this.year}`);
},
age: function() {
    const currentYear = new Date().getFullYear()
    return currentYear - this.year
}
};
 console.log(car.age()) //2