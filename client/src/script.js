$(document).ready(function() {
    $.ajax({
        url : 'http://localhost:5000/listar/Pessoa',
        method : 'GET',
        dataType : 'json',
        success : load_data_to_tbl,
        error : function(errm){
            alert('Error!')
            console.log(errm)
        }
    });
});

function load_data_to_tbl(data) {
    for(var i in data){
        reg = '<tr>' 
        +'<td>' + data[i].id + '</td>'
        +'<td>' + data[i].nome + '</td>'
        +'<td>' + data[i].email + '</td>'
        +'<td>' + data[i].telefone + '</td>'
        + '</tr>'
        $('#tblPessoa').append(reg);
    }
}