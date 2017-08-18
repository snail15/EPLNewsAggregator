function getCookie(c_name)
{
    if (document.cookie.length > 0)
    {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1)
        {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
 }

function activate_carousel(){

     $('.carousel').carousel({
        interval: 4000
    })
}

$(document).ready(function () {
    
    activate_carousel;

    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });
 

    $('.js-team-news-link').click(function(){
        console.log('clicked1');
        $('.js-team-news-link').attr('id','');
        $(this).attr('id', 'underline');
        $.ajax({
            url: 'team_news',
            method: 'POST',
            data: {
                'team_name': $(this).attr('linkteam')
            },
            success: function(serverResponse){
                console.log('clicked2')
                $('.news-content-row').html(serverResponse)
                activate_carousel;
            }
        })
    })
});

