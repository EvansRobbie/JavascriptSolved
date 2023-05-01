class Car {
    constructor(make, model, year, isAvailable){
        this.make = make,
        this.model = model,
        this.year = year,
        this.isAvailable = isAvailable
    }
     toggleAvailability (){
        this.isAvailable = !this.isAvailable
    }
}

class Rental {
    constructor(car, renterName, rentalStartDate, rentalEndDate ){
        this.car = car,
        this.renterName = renterName,
        this.rentalStartDate =rentalStartDate,
        this.rentalEndDate = rentalEndDate
    }
    carRentalDuration(){
        const start = this.rentalStartDate.getTime()
        const end = this.rentalEndDate.getTime()
        const duration = end - start
        return Math.ceil(duration/ (1000 * 3600 * 24))
    }
}

// create car instance
const car = new Car('Toyota', 'Camry', 2020, true)

// create rental instance

const rentalStartDate = new Date('2023-04-01')
const rentalEndDate = new Date('2023-04-10')

const rental = new Rental(car, 'Jane Doe', rentalStartDate, rentalEndDate)

const rentalDuration = rental.carRentalDuration()
console.log('rental Duration in days:', rentalDuration)