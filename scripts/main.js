let myImage = document.querySelector('img');

myImage.onclick = function() {
    let mySrc = myImage.getAttribute('src');
    if(mySrc === 'images/nox-cycle.png') {
      myImage.setAttribute ('src','images/hono-path.png');
    } else {
      myImage.setAttribute ('src','images/nox-cycle.png');
    }
}
