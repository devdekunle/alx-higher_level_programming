$(function() {

    $('DIV#add_item').on('click', function() {

        let ul = $('UL.my_list');
        ul.append('<li>Item</li>');

    });


});
