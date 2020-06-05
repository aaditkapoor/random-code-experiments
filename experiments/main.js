function maxsub(array) {
    var current = array[0];
    var max = current;
    for (var i = 1; i < array.length; i++) {
        current = Math.max(array[i] + current, array[i]);
        max = Math.max(current, max);
    }
    return max;
}
console.log(maxsub(['l', 189]));
