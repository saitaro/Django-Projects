console.log('connected');

var Blue = prompt('Player One: enter Your Name, you will be Blue');
var Red = prompt('Player One: enter Your Name, you will be Red');

var toggle = 'blue';
var player = Blue;
var play = true;

function order() {
    if (play) {
        $('#order').text(player + ": it is your turn, please pick a column to drop your " + toggle + " chip.");
    }
}

rows = [
    [null, null, null, null, null, null, null],
    [null, null, null, null, null, null, null],
    [null, null, null, null, null, null, null],
    [null, null, null, null, null, null, null],
    [null, null, null, null, null, null, null],
    [null, null, null, null, null, null, null],
];

function convert(rgb) {
    if (rgb === "0, 0, 255") {
        return 'blue';
    } else if (rgb === "255, 0, 0") {
        return 'red';
    } else {
        return 'gray';
    }
}

function win(vol, r, col, row) {
    console.log(1, vol.toString(), r.toString());
    var diag1 = $.makeArray($('.1').map(function () {
        var str = $(this).css('background');
        return convert(str.slice(4, str.search(/\) /)));
    }));
    var diag2 = $.makeArray($('.2').map(function () {
        var str = $(this).css('background');
        return convert(str.slice(4, str.search(/\) /)));
    }));
    var diag3 = $.makeArray($('.3').map(function () {
        var str = $(this).css('background');
        return convert(str.slice(4, str.search(/\) /)));
    }));
    var diag4 = $.makeArray($('.4').map(function () {
        var str = $(this).css('background');
        return convert(str.slice(4, str.search(/\) /)));
    }));
    var diag5 = $.makeArray($('.5').map(function () {
        var str = $(this).css('background');
        return convert(str.slice(4, str.search(/\) /)));
    }));
    var diag6 = $.makeArray($('.6').map(function () {
        var str = $(this).css('background');
        return convert(str.slice(4, str.search(/\) /)));
    }));
    var diag7 = $.makeArray($('.7').map(function () {
        var str = $(this).css('background');
        return convert(str.slice(4, str.search(/\) /)));
    }));
    var diag8 = $.makeArray($('.8').map(function () {
        var str = $(this).css('background');
        return convert(str.slice(4, str.search(/\) /)));
    }));
    var diag9 = $.makeArray($('.9').map(function () {
        var str = $(this).css('background');
        return convert(str.slice(4, str.search(/\) /)));
    }));
    var diagX = $.makeArray($('.X').map(function () {
        var str = $(this).css('background');
        return convert(str.slice(4, str.search(/\) /)));
    }));
    var diagY = $.makeArray($('.Y').map(function () {
        var str = $(this).css('background');
        return convert(str.slice(4, str.search(/\) /)));
    }));
    var diagZ = $.makeArray($('.Z').map(function () {
        var str = $(this).css('background');
        return convert(str.slice(4, str.search(/\) /)));
    }));

    if (play &&
        (/(red){4}|(blue){4}/.test(vol.toString().replace(/,/g, '')) ||
            /(red){4}|(blue){4}/.test(r.toString().replace(/,/g, ''))) ||
        /(red){4}|(blue){4}/.test(diag1.toString().replace(/,/g, '')) ||
        /(red){4}|(blue){4}/.test(diag2.toString().replace(/,/g, '')) ||
        /(red){4}|(blue){4}/.test(diag3.toString().replace(/,/g, '')) ||
        /(red){4}|(blue){4}/.test(diag4.toString().replace(/,/g, '')) ||
        /(red){4}|(blue){4}/.test(diag5.toString().replace(/,/g, '')) ||
        /(red){4}|(blue){4}/.test(diag6.toString().replace(/,/g, '')) ||
        /(red){4}|(blue){4}/.test(diag7.toString().replace(/,/g, '')) ||
        /(red){4}|(blue){4}/.test(diag8.toString().replace(/,/g, '')) ||
        /(red){4}|(blue){4}/.test(diag9.toString().replace(/,/g, '')) ||
        /(red){4}|(blue){4}/.test(diagX.toString().replace(/,/g, '')) ||
        /(red){4}|(blue){4}/.test(diagY.toString().replace(/,/g, '')) ||
        /(red){4}|(blue){4}/.test(diagZ.toString().replace(/,/g, ''))) {
        if (play) {
            $('#order').text(player + ' has won! Refresh your browser to play again!');
            play = false;
        }
        // console.log($.makeArray($('.6').map(function () {
        //     var str = $(this).css('background');
        //     return convert(str.slice(4, str.search(/\) /)));
        // })));
    };
}

order();

var col1 = 5,
    vol1 = [];
var col2 = 5,
    vol2 = [];
var col3 = 5,
    vol3 = [];
var col4 = 5,
    vol4 = [];
var col5 = 5,
    vol5 = [];
var col6 = 5,
    vol6 = [];
var col7 = 5,
    vol7 = [];

function toggleIt() {
    toggle = (toggle === 'red') ? 'blue' : 'red';
    player = (player === Blue) ? Red : Blue;
    order();
}

$('.col1').click(function () {
    if (col1 >= 0) {
        if (play) {
            $('.col1').eq(col1).css('background', toggle);
        }
        vol1.push(toggle);
        rows[col1][0] = toggle;
        win(vol1, rows[col1], 0, col1);
        toggleIt();
        col1--;
    }
});

$('.col2').click(function () {
    if (col2 >= 0) {
        if (play) {
            $('.col2').eq(col2).css('background', toggle);
        }
        vol2.push(toggle);
        rows[col2][1] = toggle;
        win(vol2, rows[col2], 1, col2);
        toggleIt();
        col2--;
    }
});

$('.col3').click(function () {
    if (col3 >= 0) {
        if (play) {
            $('.col3').eq(col3).css('background', toggle);
        }
        vol3.push(toggle);
        rows[col3][2] = toggle;
        win(vol3, rows[col3], 2, col3);
        toggleIt();
        col3--;
    }
});

$('.col4').click(function () {
    if (col4 >= 0) {
        if (play) {
            $('.col4').eq(col4).css('background', toggle);
        }
        vol4.push(toggle);
        rows[col4][3] = toggle;
        win(vol4, rows[col4], 3, col4);
        toggleIt();
        col4--;
    }
});

$('.col5').click(function () {
    if (col5 >= 0) {
        if (play) {
            $('.col5').eq(col5).css('background', toggle);
        }
        vol5.push(toggle);
        rows[col5][4] = toggle;
        win(vol5, rows[col5], 4, col5);
        toggleIt();
        col5--;
    }
});

$('.col6').click(function () {
    if (col6 >= 0) {
        if (play) {
            $('.col6').eq(col6).css('background', toggle);
        }
        vol6.push(toggle);
        rows[col6][5] = toggle;
        win(vol6, rows[col6], 5, col6);
        toggleIt();
        col6--;
    }
});

$('.col7').click(function () {
    if (col7 >= 0) {
        if (play) {
            $('.col7').eq(col7).css('background', toggle);
        }
        vol7.push(toggle);
        rows[col7][6] = toggle;
        win(vol7, rows[col7], 6, col7);
        toggleIt();
        col7--;
    }
});