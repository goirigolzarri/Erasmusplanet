
    function Hide() {
        if(document.getElementById("id_studentType").options[document.getElementById("id_studentType").selectedIndex].value == "1") {
            document.getElementById("companyDiv").style.display = "none";
            document.getElementById("studiesDiv").style.display = "";
            document.getElementById("courseDiv").style.display = "";
            document.getElementById("universityOriginDiv").style.display = "";
            document.getElementById("universityDestinationDiv").style.display = "";
       
        }  
        if(document.getElementById("id_studentType").options[document.getElementById("id_studentType").selectedIndex].value == "2")  {
            document.getElementById("companyDiv").style.display = "none";
            document.getElementById("studiesDiv").style.display = "none";
            document.getElementById("courseDiv").style.display = "none";
            document.getElementById("universityOriginDiv").style.display = "none";
            document.getElementById("universityDestinationDiv").style.display = "none";
        }
        if(document.getElementById("id_studentType").options[document.getElementById("id_studentType").selectedIndex].value == "3")  {
            document.getElementById("companyDiv").style.display = "none";
            document.getElementById("courseDiv").style.display = "none";
            document.getElementById("studiesDiv").style.display = "";
            document.getElementById("universityOriginDiv").style.display = "";
            document.getElementById("universityDestinationDiv").style.display = "";
        }
        if(document.getElementById("id_studentType").options[document.getElementById("id_studentType").selectedIndex].value == "4")  {
            document.getElementById("companyDiv").style.display = "";
            document.getElementById("courseDiv").style.display = "none";
            document.getElementById("studiesDiv").style.display = "none";
            document.getElementById("universityOriginDiv").style.display = "none";
            document.getElementById("universityDestinationDiv").style.display = "none";
        }
    }
    
    window.onload = function() {
    document.getElementById("id_studentType").onchange = Hide;
    };
  