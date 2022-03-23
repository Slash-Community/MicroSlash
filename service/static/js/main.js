$('document').ready(function () {
    var client = new WebSocket("ws://localhost:8889/");
    client.onopen = function(event) {
        client.send("0");
    };
    client.onmessage = function(event) {
        var data = JSON.parse(event.data);

        $('.count_of_rows_p').text(data["count_of_rows"]);
        $('.requests_p').text(data["reqests_lh"]);
        $('.answers_p').text(data["answers_lh"]);
        $('.new_users_p').text(data["new_entry_lh"]);
        $('.insert_count').text(data["count_of_insert"]+"%");
        $('.update_count').text(data["count_of_update"]+"%");
        $('.delete_count').text(data["count_of_delete"]+"%");

        $('.unit1').attr("stroke-dasharray", data["count_of_insert"] * 100 / data["reqests_lh"] + " 100");
        $('.unit2').attr("stroke-dasharray", data["count_of_update"] * 100 / data["reqests_lh"] + " 100");
        $('.unit3').attr("stroke-dasharray", data["count_of_delete"] * 100 / data["reqests_lh"] + " 100");
        alert("123");
    }

	$('.home_ico').on('click', function (e) {
		e.preventDefault;
        $('.workplace').css('display', 'block');
        $('.new_user').css('display', 'none');
        $('.register').css('display', 'none');
        $('.check_db').css('display', 'none');
	});

	$('.check_db_ico').on('click', function (e) {
		e.preventDefault;
        $('.workplace').css('display', 'none');
        $('.new_user').css('display', 'none');
        $('.register').css('display', 'none');
        $('.check_db').css('display', 'block');
	});

    $('.new_user_ico').on('click', function (e) {
		e.preventDefault;
        $('.workplace').css('display', 'none');
        $('.new_user').css('display', 'block');
        $('.register').css('display', 'none');
        $('.check_db').css('display', 'none');
	});

    $('.register_ico').on('click', function (e) {
		e.preventDefault;
        $('.workplace').css('display', 'none');
        $('.new_user').css('display', 'none');
        $('.register').css('display', 'block');
        $('.check_db').css('display', 'none');

        $.ajax({
            type: 'POST',
            url: "http://127.0.0.1:8888/api/logs",
            data: { name: "John", time: "2pm" },
            success: function(data) {
                $('#reg_text').text(data);
            },
        });


        jQuery('.reg_text').each(function() {
            var text = jQuery(this).text();
            text = text.replace(/\d{2,4}-\d{2,4}-\d{2,4}/g, '<mark>$&</mark>');
            jQuery(this).html(text);
        });
    });
});