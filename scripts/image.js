let myImage = document.querySelector('img');

myImage.onclick = function() {
    let mySrc = myImage.getAttribute('src');
    if(mySrc === 'images/nox-cycle.png') {
      myImage.setAttribute ('src','images/hono-path.png');
    } else if (mySrc === 'images/hono-path.png') {
      myImage.setAttribute ('src','images/PES_CH3_HONO_1_lumpHONO.png');
    } else if (mySrc === 'images/PES_CH3_HONO_1_lumpHONO.png') {
      myImage.setAttribute ('src','images/nox-cycle.png');
    }
}
