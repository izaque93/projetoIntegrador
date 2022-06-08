$(document).ready(function() {

    $(".plus_roupas").click(function() {
        a = $(".num_roupas")[0].outerText
        a++
        a = (a < 10) ? "0" + a : a;
        $(".num_roupas").text(a)
    })

    $(".min_roupas").click(function() {
        a = $(".num_roupas")[0].outerText
        if (a > 1) {
            a--
            a = (a < 10) ? "0" + a : a;
            $(".num_roupas").text(a)
        }
    })

    $(".plus_objetos").click(function() {
        a = $(".num_objetos")[0].outerText
        a++
        a = (a < 10) ? "0" + a : a;
        $(".num_objetos").text(a)
    })

    $(".min_objetos").click(function() {
        a = $(".num_objetos")[0].outerText
        if (a > 1) {
            a--
            a = (a < 10) ? "0" + a : a;
            $(".num_objetos").text(a)
        }
    })

    $(".plus_calcados").click(function() {
        a = $(".num_calcados")[0].outerText
        a++
        a = (a < 10) ? "0" + a : a;
        $(".num_calcados").text(a)
    })

    $(".min_calcados").click(function() {
        a = $(".num_calcados")[0].outerText
        if (a > 1) {
            a--
            a = (a < 10) ? "0" + a : a;
            $(".num_calcados").text(a)
        }
    })

    $(".plus_brinquedos").click(function() {
        a = $(".num_brinquedos")[0].outerText
        a++
        a = (a < 10) ? "0" + a : a;
        $(".num_brinquedos").text(a)
    })

    $(".min_brinquedos").click(function() {
        a = $(".num_brinquedos")[0].outerText
        if (a > 1) {
            a--
            a = (a < 10) ? "0" + a : a;
            $(".num_brinquedos").text(a)
        }
    })

})

/*const plus_roupas = document.querySelector(".plus")
const minus_roupas = document.querySelector(".minus")
const num_roupas = document.querySelector(".num");
let a = 1;
plus_roupas.addEventListener("click", () => {
    a++;
    a = (a < 10) ? "0" + a : a;
    num_roupas.innerText = a;
});

minus_roupas.addEventListener("click", () => {
    if (a > 1) {
        a--;
        a = (a < 10) ? "0" + a : a;
        num_roupas.innerText = a;
    }
});*/