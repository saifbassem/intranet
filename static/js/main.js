

$(document).ready(function () {
    // start  Empower //
    $(window).scroll(function () {
        var sticky = $(".sticky"),
        scroll = $(window).scrollTop();
    
        // Adjust the scroll position (e.g., 1150) as needed
        if (scroll >= 150) {
            sticky.addClass("sticky-fixed");
        } else {
            sticky.removeClass("sticky-fixed");
        }
    });
    // End  Empower //

    // start  Hiring Request //
    $(window).scroll(function () {
        var sticky = $(".sticky"),
        scroll = $(window).scrollTop();
    
        // Adjust the scroll position (e.g., 1150) as needed
        if (scroll >= 150) {
            sticky.addClass("sticky-fixed");
        } else {
            sticky.removeClass("sticky-fixed");
        }
    });

    $('.box').on('click', function (e) {
        e.preventDefault();
        $('.popup_request').removeClass('active');
        $('#overlay').addClass('overlay_visible');
        $(this).next('.popup_request').addClass('active');
        ;$('html, body').css('overflow','hidden');
    });
    $('.popup__close').on('click', function () {
        $(this).closest('.popup_request').removeClass('active');
        $('#overlay').removeClass('overlay_visible');
        $('html, body').css('overflow','visible');
    });
    $('#overlay').on('click', function (e) {
        $('.popup_request').removeClass('active');
        $('#overlay').removeClass('overlay_visible');
        $('html, body').css('overflow','visible');
    });
    // End  Hiring Request //
});