// Write a function that takes an array of objects, where each object represents a product with a name, price, and category property. The function should return an object that groups the products by their categories, with the category names as keys and the arrays of products as values.
const products = [
{ name: 'Laptop', price: 1200, category: 'Electronics' },
{ name: 'Shirt', price: 25, category: 'Clothing' },
{ name: 'Headphones', price: 80, category: 'Electronics' },
{ name: 'Shoes', price: 60, category: 'Clothing' },
];


const ProductCategory = (products) =>{
    // initialize an empty object
    const result = {}
    // Loop throu each product exracting the name,price, category
    for(let i = 0; i < products.length; i++){
        const { name, price, category} = products[i]
        // if the 'category' does not exist as a key in the 'result' object, we initiallize it as an empty array
        if(!result[category]){
            result[category] = []
        }
        // The function then pushes an object containing the name and price properties to the appropriate category array
        result[category].push({name, price})
    }
    return result
}

const groupedProducts = ProductCategory(products)

console.log(groupedProducts)