

function formValidaion() {
  var userid = document.regis.userid;
  var pass = document.regis.pass;
  var uname = document.regis.uname;
  var uaddress = document.regis.uaddress;
  var ucountry = document.regis.country;
  var zip = document.regis.zip;
  var uemail = document.regis.uemail;
  var mg = document.regis.mg;
  var fg = document.regis.fg;

  if(userValidation(userid,5,12)){
    if(passValidation(pass,7,12)){
        if(nameValidation(uname)){
            if(addressValidation(uaddress)){
                if(countryValdidation(ucountry)){
                    if(zipValidation(zip)){
                        if(emailValidation(uemail)){
                            if(genderValidation(mg,fg)){
                                
                            }
                        }
                    }
                }
            }
        }
    }
  }
  return false;
}

function userValidation(uid, x, y) {
  var l = uid.value.length;
  if (l == 0 || l <= 5 || l >= 12) {
    alert("Enter valid user id between 5 and 12 ");
    uid.focus();
    return false;
  }
  return true;
}

function passValidation(pass, x, y) {
  var l = pass.value.length;
  if (l == 0 || l < 7 || l > 12) {
    alert("Enter valid passoword between length 7 and 12");
    pass.focus();
    return false;
  }
  return true;
}

function nameValidation(uname) {
  var letters = /^[A-Za-z]+$/;
  if (uname.value.match(letters)) {
    return true;
  }
  alert("Name can be only letters");
  uname.focus();
  return false;
}

function addressValidation(uaddress) {
  var abc = /^[0-9a-zA-Z]+$/;
  if (uaddress.value.match(abc)) {
    return true;
  }
  alert("Address should contain AlphaNumeric values ");
  uaddress.focus();
  return false;
}

function countryValdidation(ucountry) {
  if ((ucountry.value == "Default")) {
    alert("Please select a country ");
    ucountry.focus();
    return false;
  }
  return true;
}

function zipValidation(zip) {
  var abc = /^[0-9]+$/;
  if (zip.value.match(abc)) {
    return true;
  }
  alert("Zip code should be all numbers ");
  zip.foucs();
  return false;
}

function emailValidation(uemail) {
  var abc = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (uemail.value.match(abc)) {
    return true;
  }
  alert("Enter valid Email ");
  uemail.focus();
  return false;
}

function genderValidation(mg,fg){
    var a=0;
    if(mg.checked){
            a++;
    }
    if(fg.checked){
        a++;
    }
    if(a==1){
         alert("Form submitted successfully");
        //  window.location.reload;
         return true;
    }
    alert("Please select gender")
    gender.focus();
    return false;
}
