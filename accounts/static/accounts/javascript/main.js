window.addEventListener("load", function(){
    div=document.getElementById('id_username');
    div.setAttribute("placeholder", "Enter Username");
    document.getElementById('id_password1').setAttribute("placeholder", "Enter Password");
    document.getElementById('id_password2').setAttribute("placeholder", "Enter Password Again");
    document.getElementById('id_email').setAttribute("placeholder", "Enter Email");
    try{
        document.getElementById('id_password').setAttribute("placeholder", "Enter Password");
    }finally{}
});