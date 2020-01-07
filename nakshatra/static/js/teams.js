$("body").flipLightBox();
wow = new WOW({}).init();

      function myFunction() {
      var x = document.getElementById("myTopnav");
      var rest = document.getElementsByClassName("container");
      if (x.className == "topnav") {
        x.className += " responsive";
        for (var i=0;i<rest.length; i++) {
          rest[i].style.display = 'none';
        }
        document.getElementById("nav-links").style.display = 'block';
      } else {
        for (var i=0;i<rest.length; i++) {
          rest[i].style.display = 'block';
        }
        document.getElementById("nav-links").style.display = 'none';
        x.className = "topnav";
      }
    }