const copyBtns = [...document.getElementsByClassName('copy-btn')]

let previous = null

copyBtns.forEach(btn => btn.addEventListener('click', () => {
    const color = btn.getAttribute('data-hex')
    navigator.clipboard.writeText(color)

    navigator.clipboard.readText().then(clipText => {
        btn.textContent = `url copied`
    })

    if (previous) {
        previous.textContent = 'click'
    }
    previous = btn
}))



// Get the modal



// const modal = document.getElementById("myModal");

// Get the button that opens the modal
// const btn = document.getElementById("myBtn{{image.id}}");

// Get the <span> element that closes the modal
// const span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal 
// btn.onclick = function () {
//     modal.style.display = "block";
// }

// When the user clicks on <span> (x), close the modal
// span.onclick = function () {
//     modal.style.display = "none";
// }

// When the user clicks anywhere outside of the modal, close it
// window.onclick = function (event) {
//     if (event.target == modal) {
//         modal.style.display = "none";
//     }
// }
