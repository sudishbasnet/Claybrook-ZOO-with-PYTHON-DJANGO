$(document).on('click', '.changeClassification', function (e) {
    var confirmation = confirm("Changing classification will delete current data. Are you sure?", '');
    if (confirmation == true) {
    }
    else{
        e.preventDefault();
        
    }
});


function filterAnimal() {
    const url = '/Claybrook-Zoo/animal'
    const delay_by_in_ms = 0
    let scheduled_function = false

    let ajax_call = function (url, req_param) {
        $.getJSON(url, req_param)
            .done(response => {
                $('#adata').fadeTo().promise().then(() => {
                    $('#adata').html(response['dataview'])
                    $('#adata').fadeTo()
                })
            })
    }

    const req_param = {
        a: $("#aname").val(),
        b: $("#aspecies").val(),
        c: $("#ahabitat").val(),
        d: $("#adiet").val(),
        e: $("#classification").val(),
        f: $("#sponsor").val(),
        g : $("#condition").val(),


    }
    if (scheduled_function) {
        clearTimeout(scheduled_function)
    }
    scheduled_function = setTimeout(ajax_call, delay_by_in_ms, url, req_param)
}




function filterUser() {
    const url = '/Claybrook-Zoo/adminpanel/user/none/0'
    const delay_by_in_ms = 0
    let scheduled_function = false

    let ajax_call = function (url, req_param) {
        $.getJSON(url, req_param)
            .done(response => {
                $('#tabledata').fadeTo().promise().then(() => {
                    $('#tabledata').html(response['dataview'])
                    $('#tabledata').fadeTo()
                })
            })
    }

    const req_param = {
        a: $("#username").val()
    }

    if (scheduled_function) {
        clearTimeout(scheduled_function)
    }
    scheduled_function = setTimeout(ajax_call, delay_by_in_ms, url, req_param)
}



function filterBooking() {
    const url = '/Claybrook-Zoo/adminpanel/booking/none/0'
    const delay_by_in_ms = 0
    let scheduled_function = false

    let ajax_call = function (url, req_param) {
        $.getJSON(url, req_param)
            .done(response => {
                $('#tabledata').fadeTo().promise().then(() => {
                    $('#tabledata').html(response['dataview'])
                    $('#tabledata').fadeTo()
                })
            })
    }

    const req_param = {
        a: $("#username").val()
    }

    if (scheduled_function) {
        clearTimeout(scheduled_function)
    }
    scheduled_function = setTimeout(ajax_call, delay_by_in_ms, url, req_param)
}






function filterWatchlist() {
    const url = '/Claybrook-Zoo/adminpanel/watchlist/none/0'
    const delay_by_in_ms = 0
    let scheduled_function = false

    let ajax_call = function (url, req_param) {
        $.getJSON(url, req_param)
            .done(response => {
                $('#tabledata').fadeTo().promise().then(() => {
                    $('#tabledata').html(response['dataview'])
                    $('#tabledata').fadeTo()
                })
            })
    }

    const req_param = {
        a: $("#username").val()
    }

    if (scheduled_function) {
        clearTimeout(scheduled_function)
    }
    scheduled_function = setTimeout(ajax_call, delay_by_in_ms, url, req_param)
}








function filterSponsor() {
    const url = '/Claybrook-Zoo/adminpanel/sponsor/none/0'
    const delay_by_in_ms = 0
    let scheduled_function = false

    let ajax_call = function (url, req_param) {
        $.getJSON(url, req_param)
            .done(response => {
                $('#tabledata').fadeTo().promise().then(() => {
                    $('#tabledata').html(response['dataview'])
                    $('#tabledata').fadeTo()
                })
            })
    }

    const req_param = {
        a: $("#username").val()
    }

    if (scheduled_function) {
        clearTimeout(scheduled_function)
    }
    scheduled_function = setTimeout(ajax_call, delay_by_in_ms, url, req_param)
}








function searchSponsor() {
    const url = '/Claybrook-Zoo/adminpanel/sponsor/filter/0'
    const delay_by_in_ms = 0
    let scheduled_function = false

    let ajax_call = function (url, req_param) {
        $.getJSON(url, req_param)
            .done(response => {
                $('#tabledata').fadeTo().promise().then(() => {
                    $('#tabledata').html(response['dataview'])
                    $('#tabledata').fadeTo()
                })
            })
    }

    const req_param = {
        a: $("#sponsor").val()
    }

    if (scheduled_function) {
        clearTimeout(scheduled_function)
    }
    scheduled_function = setTimeout(ajax_call, delay_by_in_ms, url, req_param)
}




function searchClassification() {
    const url = '/Claybrook-Zoo/adminpanel/animal/classification/0'
    const delay_by_in_ms = 0
    let scheduled_function = false

    let ajax_call = function (url, req_param) {
        $.getJSON(url, req_param)
            .done(response => {
                $('#classificationform').fadeTo().promise().then(() => {
                    $('#classificationform').html(response['dataview'])
                    $('#classificationform').fadeTo()
                })
            })
    }

    const req_param = {
        a: $("#classification").val()
    }

    if (scheduled_function) {
        clearTimeout(scheduled_function)
    }
    scheduled_function = setTimeout(ajax_call, delay_by_in_ms, url, req_param)
}




function searchAnimal() {
    const url = '/Claybrook-Zoo/adminpanel/animal/filter/0'
    const delay_by_in_ms = 0
    let scheduled_function = false

    let ajax_call = function (url, req_param) {
        $.getJSON(url, req_param)
            .done(response => {
                $('#tabledata').fadeTo().promise().then(() => {
                    $('#tabledata').html(response['dataview'])
                    $('#tabledata').fadeTo()
                })
            })
    }

    const req_param = {
        a: $("#visibility").val(),
        b: $("#species").val(),
        c: $("#animalname").val(),
        d: $("#classification").val(),
        e: $("#sponsor").val(),
        f: $("#condition").val(),

    }
    if (scheduled_function) {
        clearTimeout(scheduled_function)
    }
    scheduled_function = setTimeout(ajax_call, delay_by_in_ms, url, req_param)
}




$(document).on('click', '.deleteuser', function (e) {
    var confirmation = confirm("Do you want to delete this user ?", '');
    e.preventDefault();
    if (confirmation == true) {
        const div = '#user' + e.target.id;
        $.ajax({
            type: 'POST',
            url: "/Claybrook-Zoo/adminpanel/user/delete/0",
            data: {
                'id': e.target.id,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },  
            success: function (data) {
                $(div).fadeOut();
            }
        });
    }
});



$(document).on('click', '.deleteWatchlist', function (e) {
    var confirmation = confirm("Do you want to delete this watchlist ?", '');
    e.preventDefault();
    if (confirmation == true) {
        const div = '#watch' + e.target.id;
        $.ajax({
            type: 'POST',
            url: "/Claybrook-Zoo/adminpanel/watchlist/delete/"+e.target.id,
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function (data) {
                $(div).fadeOut();
            }
        });
    }
});





$(document).on('click', '.deleteupdate', function (e) {
    var confirmation = confirm("Do you want to delete this info ?", '');
    e.preventDefault();
    if (confirmation == true) {
        const id = e.target.id;
        $.ajax({
            type: 'POST',
            url: "/Claybrook-Zoo/adminpanel/dashboard/delete/0",
            data: {
                'id': id,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },     
            success: function (data) {
                $('#update'+id).fadeOut();
            },
        });
    }
});




$(document).on('click', '.deletebooking', function (e) {
    var confirmation = confirm("Do you want to cancel booking ?", '');
    e.preventDefault();
    if (confirmation == true) {
        const id = e.target.id;
        $.ajax({
            type: 'POST',
            url: "/Claybrook-Zoo/visitorpanel/booking/delete/0",
            data: {
                'id': id,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function (data) {
                $('#booking' + id).fadeOut();
            },
        });
    }
});




$(document).on('click', '.deletefeedback', function (e) {
    var confirmation = confirm("Do you want to delete this feedback ?", '');
    e.preventDefault();
    if (confirmation == true) {
        const id = e.target.id;
        $.ajax({
            type: 'POST',
            url: "/Claybrook-Zoo/visitorpanel/feedback/delete/0",
            data: {
                'id': id,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function (data) {
                $('#feedback' + id).fadeOut();
            },
        });
    }
});



$(document).on('click', '.admindelfeedback', function (e) {
    var confirmation = confirm("Do you want to delete this feedback ?", '');
    e.preventDefault();
    if (confirmation == true) {
        const id = e.target.id;
        $.ajax({
            type: 'POST',
            url: "/Claybrook-Zoo/adminpanel/feedback/delete/0",
            data: {
                'id': id,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function (data) {
                $('#feedback' + id).fadeOut();
            },
        });
    }
});





$(document).on('click', '.filteranimal', function (e) {
    $('#animalform').attr("style", "");
});


$(document).on('click', '.archiveanimal', function (e) {
    var confirmation = confirm("Do you want to take this action ?", '');
    e.preventDefault();
    if (confirmation == true) {
        const id = e.target.id;
        $.ajax({
            type: 'POST',
            url: "/Claybrook-Zoo/adminpanel/animal/archive/0",
            data: {
                'id': id,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function (data) {
                $('#arc' + id).html('<button id="' + id + '" class="archiveanimal btn-' + data.response +'" style="width:80px">'+data.action+'</button>');
            }
        });
    }
});






$(document).on('click', '.highlight', function (e) {
    var confirmation = confirm("Do you want to perform this action ?", '');
    e.preventDefault();
    if (confirmation == true) {
        const id = e.target.id;
        $.ajax({
            type: 'POST',
            url: "/Claybrook-Zoo/adminpanel/feedback/highlight/"+e.target.id,
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function (data) {
                $('#highlight' + id).html('<button id="' + id + '" class="highlight btn-' + data.response + '" style="width:150px">' + data.action + ' Highlight</button>');
            }
        });
    }
});





$(document).on('click', '.deletesponsor', function (e) {
    var confirmation = confirm("Do you want to delete this sponsor ?", '');
    e.preventDefault();
    if (confirmation == true) {
        const div = '#sponsor' + e.target.id;
        $.ajax({
            type: 'POST',
            url: "/Claybrook-Zoo/adminpanel/sponsor/delete/0",
            data: {
                'id': e.target.id,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function (data) {
                $(div).fadeOut();
            }
        });
    }
});


$(document).on('click', '.deleteImage', function (e) {
    var confirmation = confirm("Do you want to delete this image ?", '');
    e.preventDefault();
    if (confirmation == true) {
        var pk = e.target.id;
        var retrieve = pk.match(/(\d+)/);
        if (retrieve) {
            id = retrieve[0];
        } 
        const div = '#img'+id;
        const div1 = '#img1' + id;
        $.ajax({
            type: 'POST',
            url: "/Claybrook-Zoo/adminpanel/animal/delete/0",
            data: {
                'id':id,
                'image' : 'image',
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function (data) {
                $(div).fadeOut();
                $(div1).fadeOut();
            }
        });
    }
});






$(document).on('click', '.sendMessage', function (e) {
        var pk = e.target.id;
        var retrieve = pk.match(/(\d+)/);
        if (retrieve) 
            id = retrieve[0];
        const content = $('#content' + id).val();
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: "/Claybrook-Zoo/message",
            data: {
                'id': id,
                'content':content,
                'userid' :$('#userid').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function (data) {
                if ($('#content' + id).val() != ''){
                    $('#content' + id).val('');
                    $('#msg').append('<br><button class="btn" style="width:50%;float:right;min-height:50px;border:1px solid black">' + content + '</button><br><br>');
                }            
                
            }
        });
    
});




$(document).on('click', '.deleteAnimal', function (e) {
    var confirmation = confirm("Do you want to delete this image ? Deleting this animal can delete sponsor details too.", '');
    e.preventDefault();
    if (confirmation == true) {
        const div = '#animal' + e.target.id;
        $.ajax({
            type: 'POST',
            url: "/Claybrook-Zoo/adminpanel/animal/delete/0",
            data: {
                'id': e.target.id,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function (data) {
                $(div).fadeOut();
            }
        });
    }
});