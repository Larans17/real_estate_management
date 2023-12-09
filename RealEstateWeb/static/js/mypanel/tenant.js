var dateFormat = 'dd/mm/yy'
var startFromDate = new Date();
$(document).ready(function () {
    $("#ddlunit").select2();
    binddata();

    $('#datepicker1, #datepicker2').datepicker({
        dateFormat: dateFormat,
        minDate: startFromDate,
      });

})


function binddata(){
    $.ajax({
        method: 'GET',
        url: '/get-object-list/',
        type: 'json',
        data:{
            'obj_name':'tenant'
        }
    }).done((data) => {
        console.log(data);
        let list = "";
        if (data.length != 0) {
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
                            <a href="${val.doc_url}" target="blank">View</a>
                        </td>
                        <td>
                            <div>${val.address}</div>
                        </td>
                       
                        <td>
                            <div>${val.agreement_end_date}</div>
                        </td>
                        <td>
                            <div>${val.monthly_rent_date}</div>
                        </td>
                        </tr>`
            })
        } else {
            list += `
                    <tr>
                    <td colspan="6"><div class="d-flex justify-content-center align-items-center text-muted"> No Record Found </div></td>
                    </tr>
                    `
        }
        $("#tenant_table_data").html(list)
    })
}

function fromSubmit(form_id) {
    let form = document.getElementById(form_id);
    let formData = new FormData(form);
    
    let isValid = Validate('tenant_form_div');
    
    if (isValid == true) {
        $.ajax({
            method: 'POST',
            url: '/create-tenant/',
            processData: false,
            contentType: false,
            data: formData
        }).done((data) => {
            console.log(data);
            if (data.status == 201) {
                showMsg(data.message, 1, 5000);
                $("input").val("");
                $("select").val("0").trigger('change');
            } else {
                showMsg(data.message, 2, 5000);
            }
            binddata();
        });
    }
}
