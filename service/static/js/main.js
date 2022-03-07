$('document').ready(function () {

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