function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            document.getElementById('ava-img').src = e.target.result;
        }
        reader.readAsDataURL(input.files[0]);
    }
}

document.getElementById('form-edit-info-b1').addEventListener('click', function(){
    var myElement = document.getElementById('id_description');
    var newStr = myElement.value.substring(0, myElement.selectionStart) +
        '<b></b>' +
        myElement.value.substring(myElement.selectionEnd, myElement.length)
    myElement.value = newStr
});

document.getElementById('form-edit-info-p1').addEventListener('click', function(){
    var myElement = document.getElementById('id_description');
    var newStr = myElement.value.substring(0, myElement.selectionStart) +
        '<p></p>' +
        myElement.value.substring(myElement.selectionEnd, myElement.length)
    myElement.value = newStr
});

document.getElementById('form-edit-info-b2').addEventListener('click', function(){
    var myElement = document.getElementById('id_task');
    var newStr = myElement.value.substring(0, myElement.selectionStart) +
        '<b></b>' +
        myElement.value.substring(myElement.selectionEnd, myElement.length)
    myElement.value = newStr
});

document.getElementById('form-edit-info-p2').addEventListener('click', function(){
    var myElement = document.getElementById('id_task');
    var newStr = myElement.value.substring(0, myElement.selectionStart) +
        '<p></p>' +
        myElement.value.substring(myElement.selectionEnd, myElement.length)
    myElement.value = newStr
});

document.getElementById('form-edit-info-b3').addEventListener('click', function(){
    var myElement = document.getElementById('id_condition');
    var newStr = myElement.value.substring(0, myElement.selectionStart) +
        '<b></b>' +
        myElement.value.substring(myElement.selectionEnd, myElement.length)
    myElement.value = newStr
});

document.getElementById('form-edit-info-p3').addEventListener('click', function(){
    var myElement = document.getElementById('id_condition');
    var newStr = myElement.value.substring(0, myElement.selectionStart) +
        '<p></p>' +
        myElement.value.substring(myElement.selectionEnd, myElement.length)
    myElement.value = newStr
});
