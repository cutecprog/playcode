function what_to_do(){
value = ($('#what').val());

    //if(value==)


switch(value){
    case "0":
        alert("Please select something!");
        break;
    case "1":
        richTextField.document.execCommand('removeformat',false,null);
        richTextField.document.execCommand('outdent',false,null);
        richTextField.document.execCommand('BackColor',false,"#008080");
        break;
    case "2":
        richTextField.document.execCommand('removeformat',false,null);
        richTextField.document.execCommand('outdent',false,null);
        richTextField.document.execCommand('BackColor',false,"#FFE4B5");
        break;
    case "3":
        richTextField.document.execCommand('RemoveFormat',false,null);
        richTextField.document.execCommand('indent',false,null);
        richTextField.document.execCommand('BackColor',false,"#B0E0E6");
        break;
    case "4":
        richTextField.document.execCommand('RemoveFormat',false,null);
        richTextField.document.execCommand('indent',false,null);
        richTextField.document.execCommand('BackColor',false,"#B0E0E6");
        break;
    case "5":
        alert('action');
        break;
    case "6":
        alert('action');
        break;
    case "7":
        alert('action');
        break;
    case "8":
        alert('action');
        break;
    default:
}
}
