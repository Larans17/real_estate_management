// For Remove Content from datatables

var dataTabledictionary = {
  sLengthMenu: "_MENU_", sInfo: "_START_ to _END_ of _TOTAL_",
  sInfoEmpty: "0 to 0 of 0", sInfoFiltered: "(filtered from _MAX_ total records)",
  sSearchPlaceholder: 'Search...',
  sSearch: '',
};


// ********* func for an Form Validations ***********

function Validate(divId) {

  var result = true;
  $("#" + divId + " :input").each(function (n, element) {
    var validateAttr = $(this).attr("validate");
    var elementId = $(this).attr("id");
    var dataName = $(this).attr("data-name");
    $(this).nextAll(".error-msg").remove();

    if (
      typeof validateAttr !== "undefined" &&
      validateAttr !== false &&
      ($.trim($(element).val()) == "" || $.trim($(element).val()) == "0")
    ) {
      //-----------select-----------
      if ($(element).is("select")) {
        $("#" + elementId).addClass("form-error");
        $("#select2-" + elementId + "-container").addClass("form-error");
        $(this)
          .parent()
          .append(
            "<span class='error-msg'>" +
            `Please select any one ${dataName}` +
            "</span>"
          );
        result = false;
      }
      //-----------input-----------
      else {
        if ($.trim($(element).val()).length <= 0) {
          if ($(this).parent().hasClass("input-group")) {
            $(this).parent().nextAll(".error-msg").remove();
            $(this)
              .parent()
              .parent()
              .append(
                "<span class='error-msg'>" +
                `${dataName} should not be empty` +
                "</span>"
              );
            $(this).addClass("form-error");
          } else {
            $(this)
              .parent()
              .append(
                "<span class='error-msg'>" +
                `${dataName} should not be empty` +
                "</span>"
              );
            $(this).addClass("form-error");
          }
          result = false;
        }
      }
    } else {
      if ($("#" + elementId).val() == "" && $("#" + elementId).val() == "0") {
        $(this).nextAll(".error-msg").remove();
        if (
          $(element).is("select") &&
          ($.trim($(element).val()) == "" || $.trim($(element).val()) == "0")
        ) {
          $("#" + elementId).removeClass("form-error");
          result = false;
        } else {
          $(this).removeClass("form-error");
          result = false;
        }
      }
    }
  });

  $("#" + divId + " :input").each(function (n, element) {
    var validateAttr = $(this).attr('validate');
    var ElementId = $(this).attr('id');
    if (typeof validateAttr !== 'undefined' && validateAttr !== false && (($.trim($(element).val()) == "") || ($.trim($(element).val()) == "0")) && $.trim($(element).val()).length == 0) {
      $('#' + ElementId).focus();
      return false;
    };
  });
  return result;
}

// ********* func for an Form Clear Validation ***********
function clearValidateMsg(element) {
  var elementId = $(element).attr("id");
  if (
    $("#" + elementId)
      .parent()
      .hasClass("input-group")
  ) {
    $("#" + elementId)
      .parent()
      .parent()
      .find("span.error-msg")
      .remove();
    $("#" + elementId)
      .parent()
      .parent()
      .find(".form-error")
      .removeClass("form-error");
  } else {
    $("#" + elementId)
      .parent()
      .find("span.error-msg")
      .remove();
    $("#" + elementId)
      .parent()
      .find(".form-error")
      .removeClass("form-error");
  }
}

// ********* func for an Form Clear ***********
$.fn.clearForm = function () {
  return this.each(function () {
    $(":input", this).each(function () {
      var type = this.type,
        tag = this.tagName.toLowerCase();
      if (
        !$(this).attr("readonly") &&
        (type == "text" ||
          type == "password" ||
          tag == "textarea" ||
          type == "email")
      ) {
        if ($(this).attr("control") == "date") {
          this.value = GetTodayDate("/");
        } else if ($(this).attr("control") == "time") {
          var now = new Date();
          var time = now.format("h:i A");
          this.value = time;
        } else this.value = "";
      } else if (tag == "select") {
        this.selectedIndex = 0;
        $(this).val("0").trigger("change");
      } else if (type == "checkbox") {
        $(this).prop("checked", false);
      }
    });

    // Remove validation error messages and control border colors
    $(this).find("span.error-msg").remove();
    $(this).find(".form-error").removeClass("form-error");
  });
};

// ********* func for an Email Validation ***********
function ValidateEmail(email) {
  var EmailRegistration = /^[A-Za-z0-9_!#$%&'*+\/=?`{|}~^.-]+@[A-Za-z0-9.-]+$/;
  if (!EmailRegistration.test(email)) {
    return false;
  } else {
    return true;
  }
}



