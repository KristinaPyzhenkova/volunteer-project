function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            document.getElementById('ava-img').src = e.target.result;
        }
        reader.readAsDataURL(input.files[0]);
    }
}

document.getElementById('form-edit-info-b').addEventListener('click', function(){
    var myElement = document.getElementById('id_info');
    var newStr = myElement.value.substring(0, myElement.selectionStart) +
        '<b></b>' +
        myElement.value.substring(myElement.selectionEnd, myElement.length)
    myElement.value = newStr
});

document.getElementById('form-edit-info-p').addEventListener('click', function(){
    var myElement = document.getElementById('id_info');
    var newStr = myElement.value.substring(0, myElement.selectionStart) +
        '<p></p>' +
        myElement.value.substring(myElement.selectionEnd, myElement.length)
    myElement.value = newStr
});
