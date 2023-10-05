// O que são vetores ou Arrays

//Como declarar um array

/*let array = ['string',1,true];
console.log.(array); */

//pode guardar varios tipos de dados 

let array= ['string',1,true,['array1'],['array2'],['array3'],['array4']];
console.log(array[3]);

//forEach
array.forEach(function(item,index){
    console.log(item,index)
}
)

/*array.push ([]);
console.log(array) */

/*array.pop();
console.log(array); */

/*array.shift();
console.log(array); */

/*array.unshift ('novo iteme no inicio');
console.log(array); */

console.log(array.indexof(true))