$(document).ready(function () {
    $("#btn-font").click(function () {
        $(this).css("color", "blue");
        $(this).css("font-size", "20px");
        $(this).css("font-family", "monospace");
    });

    $("#btn-font").dblclick(function () {
        $(this).css("color", "#27273c");
        $(this).css("font-size", "");
        $(this).css("font", "");
        $(this).hover(function () {
            $(this).css("color", "white")
        },)
    });


    $('.next').on('click', function () {
        let currentImg = $('.active')
        let nextImg = currentImg.next()
        if (nextImg.length !== 0) {
            currentImg.fadeOut(() => {
                currentImg.removeClass('active')
                nextImg.fadeIn()
                nextImg.addClass('active')
            })
        }

    })

    $('.prev').on('click', function () {
        let currentImg = $('.active')
        let prevImg = currentImg.prev()
        if (prevImg.length !== 0) {
            currentImg.fadeOut(() => {
                currentImg.removeClass('active')
                prevImg.fadeIn()
                prevImg.addClass('active')
            })
        }
    })

    $('.change-trs').click(function () {
        $('.table-main tr:nth-of-type(odd)').css("background-color", "#dddddd")
        $('.table-main tr:nth-of-type(1)').css({
            "font-size": "large",
            "color": "#FDA83D",
            "background": "#27273c",
            "white-space": "break-spaces"
        })
    })
    $('.recover-trs').click(function () {
        $('.table-main tr:nth-of-type(odd)').css("background-color", "white")
        $('.table-main tr:nth-of-type(1)').css({
            "font-size": "large",
            "color": "#FDA83D",
            "background": "#27273c",
            "white-space": "break-spaces"
        })
    })
})