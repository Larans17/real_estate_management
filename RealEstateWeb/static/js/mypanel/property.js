$(document).ready(function () {
    $("#ddlfeature").select2({
        tags: true,
        placeholder: "Search and add",
    });
    binddata();


    $("#ddlfeature").on("change", function (e) {
        // Get the selected value
        var selectedValue = $(this).val();
        $("#hdFeature").val(selectedValue);
        });
});


function binddata(){
    $.ajax({
        method: 'GET',
        url: '/get-object-list/',
        type: 'json',
        data:{
            'obj_name':'property'
        }
    }).done((data) => {
        let list = "";
        if (data.length != 0) {
            getFeatures(data);
            $.each(data, function (index, val) {
                list += `
                    <tr>
                        <td>
                            <div>${index + 1}</div>
                        </td>
                        <td>
                            <div>${val.name}</div>
                        </td>
                        <td>
                            <div>${val.features}</div>
                        </td>
                       
                        <td>
                            <div>${val.location}</div>
                        </td>
                        <td>
                            <div>${val.address}</div>
                        </td>
                        </tr>`
            })
        } else {
            list += `
                    <tr>
                    <td colspan="5"><div class="d-flex justify-content-center align-items-center text-muted"> No Record Found </div></td>
                    </tr>
                    `
        }
        $("#property_table_data").html(list)
    })
}

function fromSubmit(from_id){
        let form_data = $("#"+from_id).serialize();
        let isValid = Validate('property_form_div');
        if(isValid == true){
            $.ajax({
                method: 'POST',
                url: '/create-property/',
                type: 'json',
                data:form_data
            }).done((data) => {
                console.log(data);
                if(data.status == 201){
                    showMsg(data.message,1,5000);
                    $("input").val("");
                }else{
                    showMsg(data.message,2,5000);
                }
                binddata();
            })
        }
}


function getFeatures(data) {
        $('#ddlfeature').html("<option value='0'>Search Features</option>")
        $.each(data, function (index, val) {
            $('#ddlfeature').append('<option value="' + val.features + '">' + val.features + '</option>');
        });
}
//     })
// }
