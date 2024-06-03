//ampliando el uso de var let u const
//con var puedes reasignar en cualquier momento este forma parte del ambito global. Un error es que se sobre escriba

var nombre = "Ariel";
nombre = "Osvaldo";
console.log (nombre)

function saludar (){
    var nombre = "NATALIA";
    console.log(nombre)
}
console.log(nombre); //el problema es que aqui no lee el dato de la funcion
if (true){
    var edad = 34;
    console.log(edad)
}
console.log(edad)//en la funcion funciono correctamente, en la estructura if fallo
/*
Let: esta puede ser reasignada en cualquier momento la diferencia es que su ambito es de bloque, solo disponible dentro de un bloque de llaves o dentro de una funcion 
 */
function saludar2(){
    let nombre2 ="Ariel "
    console.log (nombre2)
}
console.log(nombre2)

if(true){
    let edad2 = 33; 
    console.log(edad2);
}
//console.log(edad2)