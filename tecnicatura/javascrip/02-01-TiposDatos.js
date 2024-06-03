
var nombre = "Ariel"
console.log(typeof nombre); 
nombre = 7;
console.log(typeof nombre);
nombre = 12.3;
console.log(typeof nombre); 
//tipo numerico
var numero = 3000;
console.log(numero); 3000
//tipo object
var objeto = {
    nombre : "Ariel",
    apellido : "Bentancud",
    telefono : 2614547489 
}
console.log(typeof objeto);

//tipo de dato boleano
var bandera = true
console.log(bandera)
//Tipo de dato funcion
function miFuncion(){}
console.log(typeof miFuncion)
//tipo de dato simbol
var simbolo = Symbol("Mi simbolo");
console.log(typeof simbolo)
//tipo de dato clase
class persona{
    constructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido
    }
}
console.log(typeof persona)
//Tipo de ddato undefined
var x;
console.log(typeof x);
//null 
var y = null;
console.log(typeof y)
//Tipo de dato array u empty String
var autos = ["Citroen", "Audi","BMW", "Ford"]
console.log(autos);
console.log(typeof autos);

var z = "";
console.log(z);
console.log(typeof z)

