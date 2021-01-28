function shuffle(arr) {
    var currentInt = arr.length;

    while (currentInt !== 0) {
        // get a random int within bound of the array size
        randomInt = Math.floor(Math.random() * currentInt);
        currentInt -= 1;
        // swap the values for the shuffle
        tempval = arr[currentInt];
        arr[currentInt] = arr[randomInt];
        arr[randomInt] = tempval;
    }

    return arr;
}

// calls the shuffle method above and shuffle the stock tickers.
$('#shuffle').on('click', () => {
    $('#tickers').html(shuffle($('.ticker-row')))
})