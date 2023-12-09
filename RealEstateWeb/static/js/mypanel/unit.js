$(document).ready(function () {
    $("#ddlproperty").select2();
    $("#ddlunittype").select2({
        minimumResultsForSearch: -1
    });
    binddata();

})


function binddata(){
    $.ajax({
        method: 'GET',
        url: '/get-object-list/',
        type: 'jason',
        data:{
            'obj_name':'unit'
        }
    }).done((data) => {
        let list = "";
        if (data.length != 0) {
            $.each(data, function (index, val) {
                list += `
                    <tr>
                        <td>
                            <div>${index + 1}</div>
                        </td>
                        <td>
                            <div>${val.property_name}</div>
                        </td>
                        <td>
                            <div>${val.unit_type}</div>
                        </td>
                       
                        <td>
                            <div>₹${val.rent_cost}</div>
                        </td>
                        </tr>`
            })
        } else {
            list += `
                    <tr>
                    <td colspan="4"><div class="d-flex justify-content-center align-items-center text-muted"> No Record Found </div></td>
                    </tr>
                    `
        }
        $("#unit_table_data").html(list)
    })
}

function fromSubmit(from_id){
        let form_data = $("#"+from_id).serialize();
        let isValid = Validate('unit_form_div');
        if(isValid == true){
            $.ajax({
                method: 'POST',
                url: '/create-unit/',
                type: 'json',
                data:form_data
            }).done((data) => {
                console.log(data);
                if(data.status == 201){
                    showMsg(data.message,1,5000);
                    $("input").val("");
                    $("select").val("0").trigger('change');
                    // $("#ddlunittype").val("0");
                    
                }else{
                    showMsg(data.message,2,5000);
                }
                binddata();
            })
        }
}