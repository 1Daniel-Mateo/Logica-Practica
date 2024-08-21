function anagrama(p1,p2) {
    //convertir en minusculas la palabras (toLowerCase()), despues en arreglo (.split('')), se ordena el arreglo (.sort()) y se vuelve a convertir en cadena(.join(''))
    let pal1 = p1.toLowerCase().split('').sort().join('');
    let pal2 = p2.toLowerCase().split('').sort().join('');
    
    // Devolver true si son anagramas, false en caso contrario
    return pal1 === pal2 && p1 !== p2;
}


document.getElementById('comprobar').addEventListener('click', function() {
    let palabra1 = document.getElementById('palabra1').value;
    let palabra2 = document.getElementById('palabra2').value;
    let resultado = anagrama(palabra1, palabra2);
    document.getElementById('resultado').innerHTML = resultado ? 'Si son anagramas': 'Boll';
});