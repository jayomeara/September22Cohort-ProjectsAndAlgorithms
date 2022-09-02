// A class contains target parameters (columns) and corresponding data (rows)
// constructor is where we define the parameters
// this.name assigns those parameters to that (or this) instance
// static (this.hungerLevel = 1) means will not change on instance creation
// dynamic (this.name = name)  means will be different for each instance

class Pet {
    constructor(name, age, type) {
        this.name = name;
        this.age = age;
        this.type = type;
        this.hunger = 1 // This is static
    }
    increaseHungerLevel(amount) {
        // access hunger level for this instance
        this.hungerLevel += amount;
    }
    
}
// below is the constructor arguments of name age and type in order if you put dog, 13, fluffy on next line then console.log(fluffy would be printing that fluffy.name = dog not fluffy)
let fluffy = new Pet("fluffy", 13, "dog")
console.log(fluffy)
console.log(fluffy.name, fluffy.type, fluffy.hungerLevel)
fluffy.hungerLevel = 5 // This will no longer be needed once we created the increaseHungerLevel
fluffy.increaseHungerLevel(10)
console.log("fluffy new hunger level", fluffy.hungerLevel) 
let mazie = new Pet("Mazie", 8, "cat")
console.log(mazie)