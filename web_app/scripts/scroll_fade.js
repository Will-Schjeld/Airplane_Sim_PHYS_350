$(window).scroll(function(){
    var scrollVar = 
$(window).scrollTop();
    $(".scroll").css("opacity", 1 - scrollVar/300);
})