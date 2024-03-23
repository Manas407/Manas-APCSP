<script>

let ri = document.querySelector('.ri');
ri.addEventListener('click', function() {
    ri.style.background = 'green';
    document.querySelector('#rw').innerHTML = 'Correct';
});


let wr = document.querySelectorAll('.wr');
for (let i = 0; i < wr.length; i++) {
wr[i].addEventListener('click', function (){
    this.style.background = 'red';
    document.querySelector('#rw').innerHTML = 'Wrong';
});
}


document.querySelector('#check').addEventListener('click', function() {
    let input = document.querySelector('input');
    if (input.value == '16')
    {    input. style.backgroundColor = 'green'
        document.querySelector('#feedback2'). innerHTML = 'Correct';
    }
    else
        {
        input.style.backgroundColor - 'red';
        document.querySelector('#insert').innerHTML = 'Incorrect';
        }



</script>