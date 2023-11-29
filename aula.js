

const precoCombustivel = 5.79;
const kmPorLitros = 10;
const distanciaEmKm = 100;

const litrosConsumido = distanciaEmKm / kmPorLitros;
const valorGasto = litrosConsumido * precoCombustivel;
console.log(valorGasto);