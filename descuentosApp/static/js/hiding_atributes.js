function Hide() {


    if (document.getElementById("id_studentType").options[document.getElementById("id_studentType").selectedIndex].value == "1") {
        // NOT Displayed   
        document.getElementById("companyDiv").style.display = "none";
        // NOT Required
        document.getElementById("id_company").removeAttribute("required");
        // DISPLAYED
        document.getElementById("studiesDiv").style.display = "";
        // REQUIRED
        document.getElementById("id_studies").setAttribute("required", "");
        // DISPLAYED
        document.getElementById("courseDiv").style.display = "";
        // REQUIRED
        document.getElementById("id_course").setAttribute("required", "");
        // DISPLAYED
        document.getElementById("universityOriginDiv").style.display = "";
        // REQUIRED
        document.getElementById("id_universityOrigin").setAttribute("required", "");
        // DISPLAYED
        document.getElementById("universityDestinationDiv").style.display = "";
        // REQUIRED
        document.getElementById("id_universityDestination").setAttribute("required", "");

    }
    if (document.getElementById("id_studentType").options[document.getElementById("id_studentType").selectedIndex].value == "2") {
        document.getElementById("companyDiv").style.display = "none";
        // NOT Required
        document.getElementById("id_company").removeAttribute("required");
        // NOT Displayed   
        document.getElementById("studiesDiv").style.display = "none";
        // NOT Required
        document.getElementById("id_studies").removeAttribute("required");
        // NOT Displayed   
        document.getElementById("courseDiv").style.display = "none";
        // NOT Required
        document.getElementById("id_course").removeAttribute("required");
        // NOT Displayed   
        document.getElementById("universityOriginDiv").style.display = "none";
        // NOT Required
        document.getElementById("id_universityOrigin").removeAttribute("required");
        // NOT Displayed   
        document.getElementById("universityDestinationDiv").style.display = "none";
        // NOT Required
        document.getElementById("id_universityDestination").removeAttribute("required");
    }
    if (document.getElementById("id_studentType").options[document.getElementById("id_studentType").selectedIndex].value == "3") {
        // NOT Displayed   
        document.getElementById("companyDiv").style.display = "none";
        // NOT Required
        document.getElementById("id_company").removeAttribute("required");
        // NOT Displayed   
        document.getElementById("courseDiv").style.display = "none";
        // NOT Required
        document.getElementById("id_course").removeAttribute("required");
        // DISPLAYED
        document.getElementById("studiesDiv").style.display = "";
        // REQUIRED
        document.getElementById("id_studies").setAttribute("required", "");
        // DISPLAYED
        document.getElementById("universityOriginDiv").style.display = "";
        // REQUIRED
        document.getElementById("id_universityOrigin").setAttribute("required", "");
        // DISPLAYED
        document.getElementById("universityDestinationDiv").style.display = "";
        // REQUIRED
        document.getElementById("id_universityDestination").setAttribute("required", "");
    }
    if (document.getElementById("id_studentType").options[document.getElementById("id_studentType").selectedIndex].value == "4") {
        document.getElementById("companyDiv").style.display = "";
        // REQUIRED
        document.getElementById("id_company").setAttribute("required", "");
        // NOT Displayed  
        document.getElementById("courseDiv").style.display = "none";
        // NOT Required
        document.getElementById("id_course").removeAttribute("required");
        // NOT Displayed  
        document.getElementById("studiesDiv").style.display = "none";
        // NOT Required
        document.getElementById("id_studies").removeAttribute("required");
        // NOT Displayed  
        document.getElementById("universityOriginDiv").style.display = "none";
        // NOT Required
        document.getElementById("id_universityOrigin").removeAttribute("required");
        // NOT Displayed  
        document.getElementById("universityDestinationDiv").style.display = "none";
        // NOT Required
        document.getElementById("id_universityDestination").removeAttribute("required");
    }
}

function showForm() {

}

window.onload = function() {
    document.getElementById("id_studentType").onchange = Hide;
};