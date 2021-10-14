$(function() {

    function handle_error(errm){
        alert('Error!')
        console.log(errm)
    }

    function include_new_person() {
        const person_name = $("#person-name").val();
        const person_email = $("#person-email").val();
        const person_phone = $("#person-phone").val();
        const request = JSON.stringify({nome : person_name, email: person_email, telefone: person_phone});

        $.ajax({
            url : 'http://localhost:5000/incluir/Pessoa',
            method : 'POST',
            dataType : 'json',
            contentType : 'application/json',
            data: request,
            success : get_person_data,
            error : handle_error
        });

    }

    
    function get_person_data() {
    
        $.ajax({
            url : 'http://localhost:5000/listar/Pessoa',
            method : 'GET',
            dataType : 'json',
            success : load_person_data_to_table,
            error : handle_error
        });
    
    }

    function load_person_data_to_table(data) {
        $("#table-person tr").remove(); 
        for(var i in data){
            reg = '<tr id="person_' + data[i].id + '">'
            +'<td>' + data[i].id + '</td>'
            +'<td>' + data[i].nome + '</td>'
            +'<td>' + data[i].email + '</td>'
            +'<td>' + data[i].telefone + '</td>'
            +'<td> <a href="#"  onclick="window.delete_person('+data[i].id+')">Excluir</a> </td>'
            + '</tr>'
            $('#table-person').append(reg);
        }
    }

    function after_remove_person(id) {
        $("#person_"+id).fadeOut(100, function() {
            $("#person_"+id).remove();
        });
    }

    window.delete_person = function delete_person(id) {
        console.log('teste ' + id)
        const request = JSON.stringify({id});

        $.ajax({
            url : 'http://localhost:5000/delete/Pessoa',
            method : 'DELETE',
            dataType : 'json',
            contentType : 'application/json',
            data: request,
            success : after_remove_person(id),
            error : handle_error
        });
    }

    $(document).on("click", "#btn-load-person-table", get_person_data);
    $(document).on("click", "#btn-include-person", include_new_person);    

});
