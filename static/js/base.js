window.addEventListener("DOMContentLoaded", function () {
  console.log("DOM entièrement chargé et analysé");
    document.querySelectorAll('aside').forEach(function(domElement){
                domElement.style.height= window.innerHeight + 'px';
      })

      function reportWindowSize() {
            document.querySelectorAll('aside').forEach(function(domElement){
                domElement.style.height= window.innerHeight + 'px';
            })
      }
      window.onresize = reportWindowSize;

      let heigthWelcome
            document.querySelectorAll('#background').forEach(function(domElement){
                heigthWelcome = domElement.offsetHeight;
            })
            document.querySelectorAll('.bottom').forEach(function(domElement){
                domElement.style.marginTop = heigthWelcome + 'px';
            })


      function marginBottom() {
            document.querySelectorAll('#background').forEach(function(domElement){
                heigthWelcome = domElement.offsetHeight;
            })
            document.querySelectorAll('.bottom').forEach(function(domElement){
                domElement.style.marginTop= heigthWelcome + 'px';
            })
      }
      window.onresize = marginBottom;

  });