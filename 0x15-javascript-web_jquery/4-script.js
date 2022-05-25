$('div#toggle_header').click(function(){
    if ($('header').attr('class') == 'red') {
        $('header').toggleClass('red green')        
    } else {
        $('header').toggleClass('green red')
    }
})
