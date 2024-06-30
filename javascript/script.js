 
// script.js
// function toggleDetails(button) {
//     var details = button.closest('.publication').querySelector('.details');
//     if (details.style.display === 'none') {
//         details.style.display = 'block';
//         button.textContent = '-';
//     } else {
//         details.style.display = 'none';
//         button.textContent = '+';
//     }
// }


function toggleDetails(button) {
    var details = button.closest('.publication').querySelector('.details');
    if (details.style.display === 'none') {
        details.style.display = 'block';
        button.innerHTML = '<i class="fa fa-minus-square"></i>'; // Ícono FontAwesome para "contraer"
    } else {
        details.style.display = 'none';
        button.innerHTML = '<i class="fa fa-plus-square"></i>'; // Ícono FontAwesome para "expandir"
    }
}
